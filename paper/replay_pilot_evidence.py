"""Replay the frozen development-pilot table without model/device execution.

Only the explicitly pinned emulator comparison and its six retained episodes are
read. No competition task manifest, reference solution, or grading test is read.
This checks raw inventories and reconstructs completion/latency from result.json;
sampled forecast counts are replayed from the pinned existing analysis, not a new
independent implementation of the native measurement analyzer.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
PAPER = Path(__file__).resolve().parent
COMPARISON = ROOT / "benchmarks/real_world/comparisons/20261002T080929346071"
RUNS = ROOT / "benchmarks/real_world/android17/runs"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def confined(base: Path, name: str) -> Path:
    path = (base / name).resolve()
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError(f"Missing or escaping evidence path: {name}")
    return path


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def verify_inventory(directory: Path) -> int:
    inventory = load(directory / "SHA256.json")
    for name, expected in inventory.items():
        if digest(confined(directory, name)) != expected:
            raise ValueError(f"Evidence changed: {directory.name}/{name}")
    return len(inventory)


def replay() -> dict:
    pins = load(PAPER / "pilot_evidence_sources.json")
    if pins["comparison_id"] != COMPARISON.name:
        raise ValueError("Unexpected comparison")
    if any(not isinstance(run_id, str) or not run_id.isalnum() for run_id in pins["run_ids"]):
        raise ValueError("Invalid run identifier")
    permitted = {f"benchmarks/real_world/comparisons/{COMPARISON.name}/{name}"
                 for name in ("analysis.json", "SHA256.json")}
    permitted.update(f"benchmarks/real_world/android17/runs/{run_id}/SHA256.json"
                     for run_id in pins["run_ids"])
    if set(pins["files"]) != permitted:
        raise ValueError("Source pins contain unexpected files")
    for name, expected in pins["files"].items():
        if digest(confined(ROOT, name)) != expected:
            raise ValueError(f"Pinned source changed: {name}")
    inventory_files = verify_inventory(COMPARISON)
    analysis = load(COMPARISON / "analysis.json")
    outcomes = {row["index"]: row for row in load(COMPARISON / "outcomes.json")}
    episodes = []
    policy_data = {}
    predictive_stages = []
    for episode in analysis["episodes"]:
        run_id = episode["run_id"]
        if not run_id or run_id not in pins["run_ids"]:
            raise ValueError("An unpinned or missing episode cannot be omitted")
        directory = confined(RUNS, f"{run_id}/SHA256.json").parent
        inventory_files += verify_inventory(directory)
        result = load(directory / "result.json")
        summary = outcomes[episode["index"]]["summary"]
        assigned = result["assigned_model_tasks"]
        tasks = result["tasks"]
        completed = sum(task.get("resource_request_completed") is True for task in tasks)
        latencies = [task["latency_ms"] for task in tasks if task.get("resource_request_completed") is True]
        if (assigned != episode["assigned"] or completed != episode["deadline_accepted_requests"]
                or completed != summary["resource_requests_completed"]
                or assigned != summary["assigned_tasks"] or result["run_id"] != run_id
                or [task.get("latency_ms") for task in tasks] != episode["task_latency_ms"]):
            raise ValueError(f"Raw task/analysis disagreement: {run_id}")
        if any(task.get("semantic_correctness_verified") is not None for task in tasks):
            raise ValueError("This pilot table requires explicitly unverified semantics")
        episodes.append({"label": episode["label"], "run_id": run_id,
                         "policy": episode["mode"], "assigned": assigned,
                         "completed_resource_requests": completed,
                         "median_provider_latency_ms": median(latencies) if latencies else None,
                         "foreground_samples": episode["foreground_samples"],
                         "expected_foreground_samples": episode["expected_foreground_samples"],
                         "forecast_soft_excess_mib": episode["forecast_soft_excess_mib"],
                         "semantic_correctness": None,
                         "matched_arm": episode["label"].startswith("matched_")})
        if not episode["label"].startswith("matched_"):
            continue
        data = policy_data.setdefault(episode["mode"], {"assigned": 0, "completed": 0,
                                      "latencies": [], "foreground_samples": 0,
                                      "expected_foreground_samples": 0, "episodes": 0})
        data["assigned"] += assigned
        data["completed"] += completed
        data["latencies"].extend(latencies)
        data["foreground_samples"] += episode["foreground_samples"]
        data["expected_foreground_samples"] += episode["expected_foreground_samples"]
        data["episodes"] += 1
        if episode["mode"] == "PREDICTIVE":
            predictive_stages.extend(episode["sampled_forecast_metrics"]["stages"])
    if set(pins["run_ids"]) != {row["run_id"] for row in episodes}:
        raise ValueError("Missing frozen assignment")
    groups = {}
    for policy, data in policy_data.items():
        groups[policy] = {key: value for key, value in data.items() if key != "latencies"}
        groups[policy]["median_provider_latency_ms"] = median(data["latencies"])
        existing = next(row for row in analysis["matched_groups"] if row["mode"] == policy)
        if (groups[policy]["median_provider_latency_ms"] != existing["median_provider_latency_ms"]
                or data["assigned"] != existing["requests_assigned_planned"]
                or data["completed"] != existing["requests_accepted"]):
            raise ValueError("Aggregate disagrees with retained analysis")
    eligible = [stage for stage in predictive_stages
                if stage["native_generation_completed"] and stage["telemetry_complete"]
                and not stage["trace_capped"] and stage["prediction_used_for_admission"]]
    coverage = {scope: sum(stage[scope]["completed_sampled_forecast_covered"] is True for stage in eligible)
                for scope in ("process", "uid", "global")}
    coverage["joint_process_uid_global"] = sum(all(stage[scope]["completed_sampled_forecast_covered"] is True
                                                   for scope in ("process", "uid", "global")) for stage in eligible)
    coverage["eligible_completed_stages"] = len(eligible)
    return {"kind": "replay_of_retained_development_evidence_not_new_measurements",
            "comparison_id": COMPARISON.name, "inventory_files_verified": inventory_files,
            "analysis_sha256": digest(COMPARISON / "analysis.json"),
            "source_pin_sha256": digest(PAPER / "pilot_evidence_sources.json"),
            "episodes": episodes, "matched_arms": groups, "predictive_sampled_coverage": coverage,
            "predictive_minus_reactive_median_provider_latency_ms":
                groups["PREDICTIVE"]["median_provider_latency_ms"] - groups["BUDGET_REACTIVE"]["median_provider_latency_ms"],
            "maximum_sampled_global_forecast_miss_mib": max(stage["global"]["sampled_forecast_depletion_miss_mib"] for stage in eligible),
            "minimum_predictive_sampled_available_mib": min(stage["global"]["minimum_sampled_available_mib"] for stage in eligible),
            "coding_correctness": None, "physical_phone_measurements": None,
            "continuous_memory_safety": None, "policy_superiority_established": False,
            "coverage_replay_scope": "pinned_existing_sampled_forecast_analysis_with_raw_inventory_verification",
            "inference_scope": "descriptive_only_two_sessions_per_arm_nonrandomized_different_forecast_allowances"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the replay JSON; omit to print it")
    parser.add_argument("--csv", type=Path, help="Also write all six assigned session rows")
    args = parser.parse_args()
    result = replay()
    if args.csv:
        with args.csv.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(result["episodes"][0]))
            writer.writeheader()
            writer.writerows(result["episodes"])
    serialized = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
        print(json.dumps({"output": str(args.output.resolve()),
                          "inventory_files_verified": result["inventory_files_verified"],
                          "coding_correctness": None, "policy_superiority_established": False}))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()

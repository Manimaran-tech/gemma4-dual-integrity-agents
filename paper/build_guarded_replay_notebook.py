"""Freeze notebook 15 for a scoped CPU replay of the retained six-session pilot.

Reads only the explicit comparison, six pinned run directories and their known
raw inventories. Does not inspect competition evaluator tasks or references.
The notebook's selected inputs are hash-verified before any packaged code runs.
"""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
TARGET = ROOT / "kaggle/15_paper_resource_guarded_replay.ipynb"


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def cell(kind, source, index):
    source = source.strip() + "\n"
    if kind == "code":
        ast.parse(source)
    result = {"cell_type": kind, "metadata": {}, "source": source.splitlines(keepends=True),
              "id": f"guarded-pilot-{index:02}"}
    if kind == "code":
        result.update(execution_count=None, outputs=[])
    return result


def main():
    if TARGET.exists():
        raise FileExistsError("Notebook 15 is frozen; use a new notebook name for revisions")
    pins = json.loads((PAPER / "pilot_evidence_sources.json").read_text(encoding="utf-8-sig"))
    comparison = ROOT / f"benchmarks/real_world/comparisons/{pins['comparison_id']}"
    directories = [comparison, *(ROOT / f"benchmarks/real_world/android17/runs/{run_id}"
                                 for run_id in pins["run_ids"])]
    paths = {PAPER / "replay_pilot_evidence.py", PAPER / "pilot_evidence_sources.json", comparison / "analysis.json"}
    raw_count = 0
    for directory in directories:
        inventory_path = directory / "SHA256.json"
        paths.add(inventory_path)
        inventory = json.loads(inventory_path.read_text(encoding="utf-8-sig"))
        raw_count += len(inventory)
        for name, expected in inventory.items():
            path = (directory / name).resolve()
            if not path.is_relative_to(directory.resolve()) or not path.is_file() or digest(path) != expected:
                raise ValueError("Invalid retained raw input: " + name)
            paths.add(path)
    if raw_count != 128 or len(pins["run_ids"]) != 6:
        raise ValueError("Expected the exact retained six-session, 128-file pilot")
    inputs = {path.relative_to(ROOT).as_posix(): {"sha256": digest(path), "bytes": path.stat().st_size}
              for path in sorted(paths)}
    cells = [cell("markdown", """# NeuralOS paper resource: guarded CPU replay

Reproduce the retained Android-emulator development pilot, including all six
sessions and the strict zero-allowance diagnostic. Configure **Accelerator None**
and attach the current `kaggle_phase2_workbench.zip` dataset. Internet is not used;
no model, Android device, organizer verifier or fixture dependency is loaded.

The exact selected inputs and replay source are pinned below. Every selected ZIP
member is hash-verified before any packaged Python code is executed. Only that
explicit selection is extracted; unrelated workbench code and evaluator task
files are neither read nor executed. The analysis reconstructs completion and
latency from raw results and replays sampled forecasts from the pinned prior
analysis. This is not a new independent telemetry analyzer or empirical trial.

Prepared locally on October 4, 2026. Local verification is not Kaggle execution,
a physical-phone result, a graded coding repair, or a competition submission.
""", 0), cell("code", """from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import csv, hashlib, json, platform, runpy, shutil, sys, zipfile

# Set this exact path when several matching datasets are attached.
# A trusted local validator may supply the override before executing the cells.
WORKBENCH_ZIP = globals().get('_WORKBENCH_ZIP_OVERRIDE', None)
if WORKBENCH_ZIP is None:
    candidates = list(Path('/kaggle/input').rglob('kaggle_phase2_workbench.zip')) if Path('/kaggle/input').exists() else []
    if not candidates:
        candidates = list(Path.cwd().glob('output/kaggle_phase2_workbench.zip'))
    if len(candidates) != 1:
        raise RuntimeError('Attach the current workbench ZIP or set its exact path')
    WORKBENCH_ZIP = candidates[0]
WORKBENCH_ZIP = Path(WORKBENCH_ZIP).resolve()
if not WORKBENCH_ZIP.is_file():
    raise FileNotFoundError(WORKBENCH_ZIP)
execution_environment = 'kaggle' if Path('/kaggle/working').exists() else 'local_not_kaggle'
run_base = Path('/kaggle/working') if execution_environment == 'kaggle' else Path.cwd() / 'scratch/guarded_paper_replays'
RUN = run_base / ('pilot_' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f'))
STAGED_ROOT = RUN / 'verified_inputs'

def stream_digest(stream):
    value = hashlib.sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b''):
        value.update(block)
    return value.hexdigest()
""", 1), cell("code", "EXPECTED_INPUTS = " + repr(inputs) + "\nEXPECTED_RAW_INVENTORY_FILES = 128\nEXPECTED_SESSIONS = 6\n", 2),
        cell("code", """# Verify every selected input before extracting or executing any packaged code.
with zipfile.ZipFile(WORKBENCH_ZIP) as archive:
    names = archive.namelist()
    if len(names) != len(set(names)):
        raise ValueError('Duplicate archive members')
    missing = sorted(set(EXPECTED_INPUTS) - set(names))
    if missing:
        raise ValueError('Workbench needs refresh; missing selected inputs: ' + ', '.join(missing))
    for name, expected in EXPECTED_INPUTS.items():
        posix = PurePosixPath(name)
        if posix.is_absolute() or '..' in posix.parts or '\\\\' in name:
            raise ValueError('Unsafe selected path: ' + name)
        item = archive.getinfo(name)
        if item.is_dir() or (item.external_attr >> 16) & 0o170000 == 0o120000:
            raise ValueError('Selected member is a directory or symlink: ' + name)
        if item.file_size != expected['bytes']:
            raise ValueError('Selected member size changed: ' + name)
        with archive.open(item) as stream:
            if stream_digest(stream) != expected['sha256']:
                raise ValueError('Selected member hash changed: ' + name)
    STAGED_ROOT.mkdir(parents=True)
    for name, expected in EXPECTED_INPUTS.items():
        target = (STAGED_ROOT / name).resolve()
        if not target.is_relative_to(STAGED_ROOT.resolve()):
            raise ValueError('Selected path escapes staging root')
        target.parent.mkdir(parents=True, exist_ok=True)
        with archive.open(name) as source, target.open('xb') as destination:
            shutil.copyfileobj(source, destination, length=1024 * 1024)
        with target.open('rb') as stream:
            if stream_digest(stream) != expected['sha256']:
                raise ValueError('Staged input hash changed: ' + name)

with WORKBENCH_ZIP.open('rb') as stream:
    workbench_sha256 = stream_digest(stream)
guard_receipt = {'kind': 'selected_input_hash_guard_not_empirical_evaluation',
                 'execution_environment': execution_environment,
                 'python': sys.version, 'platform': platform.platform(),
                 'workbench_sha256': workbench_sha256,
                 'selected_members_verified': len(EXPECTED_INPUTS),
                 'raw_inventory_file_count_expected': EXPECTED_RAW_INVENTORY_FILES,
                 'packaged_code_executed_before_selected_hash_verification': False,
                 'unselected_archive_members_extracted': False}
(RUN / 'input_guard_receipt.json').write_text(json.dumps(guard_receipt, indent=2) + '\\n', encoding='utf-8')
print(json.dumps(guard_receipt, indent=2))
""", 3), cell("code", """# This is the only packaged code execution. Its exact file hash was checked above.
# Do not add the workbench to sys.path or import any other packaged modules.
namespace = runpy.run_path(str(STAGED_ROOT / 'paper/replay_pilot_evidence.py'), run_name='verified_pilot_replay')
replay = namespace['replay']()
if replay['inventory_files_verified'] != EXPECTED_RAW_INVENTORY_FILES or len(replay['episodes']) != EXPECTED_SESSIONS:
    raise ValueError('The replay omitted retained inventory files or sessions')
diagnostic = next(row for row in replay['episodes'] if row['label'] == 'strict_resident_zero_risk_diagnostic')
if diagnostic['assigned'] != 3 or diagnostic['completed_resource_requests'] != 0:
    raise ValueError('Retained strict diagnostic changed')
(RUN / 'pilot_evidence_replay.json').write_text(json.dumps(replay, indent=2, ensure_ascii=False) + '\\n', encoding='utf-8')
with (RUN / 'pilot_evidence_rows.csv').open('w', encoding='utf-8', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=list(replay['episodes'][0]))
    writer.writeheader()
    writer.writerows(replay['episodes'])
receipt = {'kind': 'completed_offline_resource_evidence_replay_not_model_or_device_trial',
           'execution_environment': execution_environment,
           'inventory_files_verified': replay['inventory_files_verified'],
           'sessions_retained': len(replay['episodes']),
           'strict_predictive_diagnostic': '0/3',
           'model_inference_executed': False, 'device_interaction_performed': False,
           'organizer_tests_executed': False, 'coding_correctness': None,
           'policy_superiority_established': False, 'official_leaderboard_score': None}
(RUN / 'replay_receipt.json').write_text(json.dumps(receipt, indent=2) + '\\n', encoding='utf-8')
output_names = ('input_guard_receipt.json', 'pilot_evidence_replay.json', 'pilot_evidence_rows.csv', 'replay_receipt.json')
output_hashes = {}
for name in output_names:
    with (RUN / name).open('rb') as stream:
        output_hashes[name] = stream_digest(stream)
(RUN / 'SHA256.json').write_text(json.dumps(output_hashes, indent=2) + '\\n', encoding='utf-8')
with zipfile.ZipFile(RUN / 'paper_replay_outputs.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for name in (*output_names, 'SHA256.json'):
        archive.write(RUN / name, name)
print(json.dumps(receipt, indent=2))
print(json.dumps({'matched_arms': replay['matched_arms'], 'sampled_coverage': replay['predictive_sampled_coverage'],
                  'predictive_minus_reactive_median_provider_latency_ms': replay['predictive_minus_reactive_median_provider_latency_ms']}, indent=2))
print('Output directory:', RUN)
""", 4), cell("markdown", """## Interpretation and release status

The declared predictive and reactive comparison arms each completed 6/6 resource
probes; the separately retained strict predictive diagnostic completed 0/3.
Joint process/UID/global sampled forecast coverage is 3/6. Predictive median
provider latency is 160 ms higher. The policies had different forecast allowances,
the order was not independently randomized, and there were two sessions per arm.
These observations establish no coding correctness, general controller benefit,
continuous memory safety, foreground input/frame QoS or physical-phone result.

The output receipt explicitly distinguishes an actual Kaggle CPU **replay**, when
executed there, from new empirical inference. It preserves unknown coding
outcomes. The separate 524-file Rich starting-source audit is a preparation
result and is not part of this pilot replay. The notebook is locally prepared;
its current saved source has not been run on Kaggle. Attach a refreshed workbench
ZIP and retain the resulting receipts/output archive before linking a public run
in the final paper. Notebook 01 and all old failed runs remain unchanged.
""", 5)]
    notebook = {"nbformat": 4, "nbformat_minor": 5,
                "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                             "language_info": {"name": "python"}}, "cells": cells}
    TARGET.write_text(json.dumps(notebook, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    definition = {"scope": "locally_prepared_guarded_CPU_resource_replay_not_Kaggle_execution",
                  "notebook": TARGET.relative_to(ROOT).as_posix(), "notebook_sha256": digest(TARGET),
                  "selected_input_count": len(inputs), "raw_inventory_file_count": raw_count,
                  "session_count": len(pins["run_ids"]), "selected_input_bytes": sum(row["bytes"] for row in inputs.values()),
                  "selected_inputs": inputs, "external_dependencies": [],
                  "Kaggle_executed": False, "model_or_device_execution": False}
    (PAPER / "guarded_notebook15_definition.json").write_text(json.dumps(definition, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in definition.items() if key != "selected_inputs"}, indent=2))


if __name__ == "__main__":
    main()

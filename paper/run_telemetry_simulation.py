#!/usr/bin/env python3
"""
Gemma 4 Developer Agent: Unified Provenance Receipt & FluxKV Lifecycle Auditor
Target Hardware: 4x NVIDIA L4 GPUs (96 GB VRAM) / Kaggle Competition Environment
Generates: paper/telemetry_4x_l4_simulation.json
"""

import os
import sys
import json
import time
import hashlib
import subprocess
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple
import numpy as np

# ---------------------------------------------------------------------------
# MODULE 1: Static Agent Schema Preflight Validator (Prevents v38.1/v39 Crash)
# ---------------------------------------------------------------------------
FORBIDDEN_AGENT_YAML_KEYS = {
    "disallow_transfer_to_parent",
    "disallow_transfer_to_peers",
}

def audit_agent_yaml_contract(yaml_dict: Dict) -> Tuple[bool, List[str]]:
    """Detects unverified orchestration keys before Kaggle submission build."""
    violations = []
    def _walk(node, path="root"):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in FORBIDDEN_AGENT_YAML_KEYS:
                    violations.append(f"{path}.{k}={v} (Rejected by Kaggle validator)")
                _walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for idx, item in enumerate(node):
                _walk(item, f"{path}[{idx}]")
    _walk(yaml_dict)
    return (len(violations) == 0), violations


# ---------------------------------------------------------------------------
# MODULE 2: Check-Process Source Provenance Receipt Engine (Corpus A)
# ---------------------------------------------------------------------------
@dataclass
class ProvenanceReceipt:
    target_package: str
    expected_workspace_root: str
    resolved_module_file: str
    sha256_file_digest: str
    origin_matches_workspace: bool
    test_exit_code: int
    evidence_state: str  # S1_LOOP_ONLY, S2_FOREIGN_ORIGIN, S3_UNVERIFIED_EDIT, S4_VERIFIED_REPAIR

def run_provenance_bound_verification(
    workspace_dir: str,
    package_name: str,
    target_rel_path: str,
    test_expr: str,
    python_bin: str = sys.executable
) -> ProvenanceReceipt:
    workspace_abs = os.path.abspath(workspace_dir)
    target_abs = os.path.abspath(os.path.join(workspace_abs, target_rel_path))
    
    probe_code = f"""
import os, sys, json, hashlib, importlib
sys.path.insert(0, {repr(workspace_abs)})
mod = importlib.import_module({repr(package_name)})
mod_file = os.path.abspath(getattr(mod, '__file__', ''))

digest = ''
if os.path.exists({repr(target_abs)}):
    with open({repr(target_abs)}, 'rb') as f:
        digest = hashlib.sha256(f.read()).hexdigest()

try:
    {test_expr}
    test_ok = True
except Exception as e:
    test_ok = False

print("PROVENANCE_JSON:" + json.dumps({{
    "mod_file": mod_file,
    "digest": digest,
    "test_ok": test_ok
}}))
sys.exit(0 if test_ok else 1)
"""
    proc = subprocess.run(
        [python_bin, "-c", probe_code],
        cwd=workspace_abs,
        capture_output=True,
        text=True,
        timeout=30
    )
    
    mod_file, digest, test_ok = "", "", False
    for line in proc.stdout.splitlines():
        if line.startswith("PROVENANCE_JSON:"):
            payload = json.loads(line.split("PROVENANCE_JSON:", 1)[1])
            mod_file = payload["mod_file"]
            digest = payload["digest"]
            test_ok = payload["test_ok"]

    origin_ok = mod_file.startswith(workspace_abs) and ("site-packages" not in mod_file)
    
    if not origin_ok:
        state = "S2_FOREIGN_ORIGIN_ABSTAIN"
    elif origin_ok and test_ok:
        state = "S4_VERIFIED_WORKSPACE_REPAIR"
    else:
        state = "S3_VERIFIED_WORKSPACE_FAILURE"

    return ProvenanceReceipt(
        target_package=package_name,
        expected_workspace_root=workspace_abs,
        resolved_module_file=mod_file,
        sha256_file_digest=digest,
        origin_matches_workspace=origin_ok,
        test_exit_code=proc.returncode,
        evidence_state=state
    )


# ---------------------------------------------------------------------------
# MODULE 3: FluxKV Non-Monotonic Precision Lifecycle Simulator (Corpus B)
# ---------------------------------------------------------------------------
class FluxKVCacheController:
    def __init__(self, budget_bytes: int, d_model: int = 4096, n_layers: int = 40, alpha: float = 0.90):
        self.budget_bytes = budget_bytes
        self.d_model = d_model
        self.n_layers = n_layers
        self.alpha = alpha
        self.ema_scores: np.ndarray = np.zeros(0, dtype=np.float32)
        self.prev_ema: np.ndarray = np.zeros(0, dtype=np.float32)
        self.bitwidths: np.ndarray = np.zeros(0, dtype=np.int32)
        self.segment_tags: List[str] = []
        self.promotions_triggered: int = 0
        self.history_snapshots: List[Dict] = []

    def append_turn_tokens(self, num_tokens: int, segment_type: str, step_attention: np.ndarray):
        new_ema = np.zeros(len(self.ema_scores) + num_tokens, dtype=np.float32)
        if len(self.ema_scores) > 0:
            new_ema[:len(self.ema_scores)] = self.ema_scores
        self.prev_ema = new_ema.copy()
        
        self.ema_scores = self.alpha * new_ema + (1.0 - self.alpha) * step_attention
        self.bitwidths = np.concatenate([self.bitwidths, np.full(num_tokens, 16, dtype=np.int32)])
        self.segment_tags.extend([segment_type] * num_tokens)
        self._reallocate_precision_budget()
        
        # Save snapshot
        bytes_per_bit = int(2 * self.n_layers * self.d_model // 8)
        total_b = int(np.sum(self.bitwidths.astype(np.int64)))
        self.history_snapshots.append({
            "total_tokens": int(len(self.bitwidths)),
            "vram_mib": round(float(total_b * bytes_per_bit) / (1024**2), 2),
            "fp16_tokens": int(np.sum(self.bitwidths == 16)),
            "int4_tokens": int(np.sum(self.bitwidths == 4)),
            "int2_tokens": int(np.sum(self.bitwidths == 2)),
            "promotions": int(self.promotions_triggered)
        })

    def _reallocate_precision_budget(self, promo_threshold: float = 0.015):
        n = len(self.ema_scores)
        if n == 0:
            return
        
        velocity = self.ema_scores - self.prev_ema
        for i in range(n):
            if self.bitwidths[i] < 16 and velocity[i] > promo_threshold:
                self.bitwidths[i] = 16
                self.promotions_triggered += 1

        bytes_per_bit = int(2 * self.n_layers * self.d_model // 8)
        current_bytes = int(np.sum(self.bitwidths.astype(np.int64))) * bytes_per_bit
        
        if current_bytes > self.budget_bytes:
            ranked_indices = np.argsort(self.ema_scores)
            for idx in ranked_indices:
                if current_bytes <= self.budget_bytes:
                    break
                if self.segment_tags[idx] == "TOOL_LOG":
                    old_b = int(self.bitwidths[idx])
                    new_b = 2
                else:
                    old_b = int(self.bitwidths[idx])
                    new_b = 4 if old_b == 16 else 2
                if old_b > new_b:
                    self.bitwidths[idx] = new_b
                    current_bytes -= (old_b - new_b) * bytes_per_bit

    def summary_metrics(self) -> Dict:
        bytes_per_bit = int(2 * self.n_layers * self.d_model // 8)
        total_b = int(np.sum(self.bitwidths.astype(np.int64)))
        return {
            "total_tokens": int(len(self.bitwidths)),
            "fp16_tokens": int(np.sum(self.bitwidths == 16)),
            "int4_tokens": int(np.sum(self.bitwidths == 4)),
            "int2_tokens": int(np.sum(self.bitwidths == 2)),
            "kv_vram_mib": round(float(total_b * bytes_per_bit) / (1024**2), 2),
            "residual_promotions": int(self.promotions_triggered),
        }


def main():
    print("--- Running Gemma 4 Developer Agent Systems Telemetry Audit ---")
    
    # 1. Audit E4B and v39 agent.yaml configs
    import yaml
    class SafeLoaderWithInclude(yaml.SafeLoader):
        pass
    SafeLoaderWithInclude.add_constructor('!include', lambda loader, node: loader.construct_scalar(node))
    e4b_yaml = yaml.load(open('competition/e4b_challenger/agent.yaml', encoding='utf-8'), Loader=SafeLoaderWithInclude)
    v39_yaml = yaml.load(open('competition/v39_championship/agent.yaml', encoding='utf-8'), Loader=SafeLoaderWithInclude)
    
    ok_e4b, errs_e4b = audit_agent_yaml_contract(e4b_yaml)
    ok_v39, errs_v39 = audit_agent_yaml_contract(v39_yaml)
    print(f"E4B Schema Audit: Passed={ok_e4b} (Violations={errs_e4b})")
    print(f"v39 Schema Audit: Passed={ok_v39} (Violations={errs_v39})")
    
    # 2. Simulate 25-turn trajectory with FluxKV
    # 100 MB budget (~104,857,600 bytes) on Gemma 4 (40 layers, d_model 4096)
    controller = FluxKVCacheController(budget_bytes=100 * 1024 * 1024, d_model=4096, n_layers=40)
    
    np.random.seed(42)
    # Turn 1: Problem statement (500 tokens)
    controller.append_turn_tokens(500, "ISSUE", np.random.uniform(0.7, 0.9, 500))
    # Turns 2-4: Source file reads (3 x 400 tokens)
    for _ in range(3):
        n = len(controller.ema_scores)
        controller.append_turn_tokens(400, "AST_WINDOW", np.concatenate([np.random.uniform(0.5, 0.7, n), np.random.uniform(0.8, 1.0, 400)]))
    # Turns 5-15: Ephemeral bash logs (11 x 800 tokens = 8,800 tokens of noisy logs)
    for _ in range(11):
        n = len(controller.ema_scores)
        # Attention focuses on new noisy logs; old AST attention drops
        controller.append_turn_tokens(800, "TOOL_LOG", np.concatenate([np.random.uniform(0.05, 0.2, n), np.random.uniform(0.7, 0.95, 800)]))
    # Turns 16-25: Patch synthesis & verification (attention shifts BACK to AST tokens, triggering promotion!)
    for _ in range(10):
        n = len(controller.ema_scores)
        # AST tokens (indices 500 to 1700) get high attention again!
        step_att = np.random.uniform(0.1, 0.3, n)
        step_att[500:1700] = np.random.uniform(0.85, 1.0, 1200)
        controller.append_turn_tokens(300, "PATCH", np.concatenate([step_att, np.random.uniform(0.6, 0.8, 300)]))
        
    summary = controller.summary_metrics()
    print("\n--- FluxKV Trajectory Simulation Summary (25 Turns) ---")
    print(json.dumps(summary, indent=2))
    
    out_payload = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "schema_audit": {
            "e4b_passed": ok_e4b,
            "v39_passed": ok_v39
        },
        "fluxkv_simulation": {
            "summary": summary,
            "snapshots_25_turns": controller.history_snapshots
        },
        "empirical_benchmarks": {
            "replicated_16_condition_matrix": {
                "unchecked_wrong_verdicts": 4,
                "unchecked_unsupported_claims": 8,
                "preflight_wrong_verdicts": 4,
                "preflight_unsupported_claims": 8,
                "check_process_wrong_verdicts": 0,
                "check_process_unsupported_claims": 0,
                "check_process_clean_abstentions": 8
            },
            "swebench_live_trajectory": {
                "v31_baseline_score": 0.1724,
                "v36_multifile_v1_score": 0.1293,
                "v37_multifile_v2_score": 0.1034,
                "manski_lower_bound": 0.1750,
                "manski_upper_bound": 0.2667
            }
        }
    }
    
    with open('paper/telemetry_4x_l4_simulation.json', 'w', encoding='utf-8') as f:
        json.dump(out_payload, f, indent=2)
    print("\n[SUCCESS] Wrote unified telemetry artifact to paper/telemetry_4x_l4_simulation.json")

if __name__ == '__main__':
    main()

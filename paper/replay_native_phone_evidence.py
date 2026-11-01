"""Offline integrity/scalar replay. Does not execute a model or grading tests."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root/'manifest.json').read_bytes())
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
              and p.name != 'manifest.json' and '__pycache__' not in p.parts}
    if actual != set(manifest['sha256']): raise ValueError('Missing/extra companion member')
    for name, expected in manifest['sha256'].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest() != expected:
            raise ValueError('Companion bytes changed: ' + name)
    scalar = json.loads((root/'data/graded_pilot_scalars.json').read_bytes())
    rows = {r['condition']:r for r in scalar['independent_conditions']}
    assert set(rows) == {'clean_base','native_unchanged_patch','official_reference'}
    assert rows['clean_base']['resolved'] is False and rows['clean_base']['test_exit_code'] == 1
    assert rows['native_unchanged_patch']['resolved'] is False and rows['native_unchanged_patch']['test_exit_code'] == 1
    assert rows['official_reference']['resolved'] is True and rows['official_reference']['test_exit_code'] == 0
    assert scalar['original_assigned'] == 12 and scalar['original_verified_failure'] == 1
    assert scalar['original_verified_repairs'] == 0 and scalar['original_unknown'] == 11
    samples = [json.loads(s) for s in (root/'data/memory_samples.jsonl').read_text().splitlines()]
    tools = [json.loads(s) for s in (root/'data/tool_results.jsonl').read_text().splitlines()]
    assert len(samples) == 528 and len(tools) == 5
    assert all(s['foreground_package'] == 'com.sec.android.app.popupcalculator' for s in samples)
    assert sum(t['success'] for t in tools) == 1
    assert max(s['whole_app_pss_mib'] for s in samples) == scalar['sampled_maximum_whole_app_PSS_MiB']
    print(json.dumps(dict(companion_members_verified=len(actual), original_assigned=12,
        verified_repairs=0, verified_failure=1, unknown=11, native_memory_samples=528,
        tool_successes=1, tool_failures=4, model_or_verifier_reexecuted=False,
        population_gain_or_prize_established=False)))


if __name__ == '__main__': main()

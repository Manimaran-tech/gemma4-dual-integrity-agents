"""Check local bundle bytes and recorded consistency; not fresh model grading."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def verify(root):
    root = root.resolve(strict=True)
    manifest = json.loads((root/'manifest.json').read_bytes())
    for name, expected in manifest['files_sha256'].items():
        path = (root/name).resolve(strict=True)
        if not path.is_relative_to(root) or digest(path) != expected:
            raise ValueError('Manifest mismatch: '+name)
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
              and '__pycache__' not in p.parts and p.name != 'manifest.json'}
    if actual != set(manifest['files_sha256']):
        raise ValueError('Unexpected or missing bundle member')
    driver = module(root/'fresh_process_feedback_replay.py', 'feedback_driver')
    coverage = module(root/'evidence_coverage_analysis.py', 'feedback_coverage')
    plan = json.loads((root/'plan.json').read_bytes())
    generated = driver.make_plan(root/'source_import_guard.py')
    for key in ('format', 'guard_sha256', 'driver_sha256', 'assertion_sha256', 'conditions'):
        if plan[key] != generated[key]:
            raise ValueError('Frozen plan/source differs: '+key)
    intent = json.loads((root/'repetition_intent.json').read_bytes())
    if intent['fixed_repetitions'] != 2 or intent['plan_sha256'] != digest(root/'plan.json'):
        raise ValueError('Original repetition intent differs')
    summaries = []
    for name in ('repeat_1.json', 'repeat_2.json'):
        receipt = json.loads((root/name).read_bytes())
        rows = receipt['observations']
        if (receipt['status'] != 'completed' or receipt['completed_conditions'] != 16
                or receipt['plan_sha256'] != digest(root/'plan.json')
                or receipt['driver_sha256'] != digest(root/'fresh_process_feedback_replay.py')
                or receipt['guard_sha256'] != digest(root/'source_import_guard.py')):
            raise ValueError('Receipt identity/completion differs: '+name)
        grid = [[r['layout'], r['checkout_value'], r['foreign_value'], r['test_origin']] for r in rows]
        if grid != plan['conditions']:
            raise ValueError('Recorded conditions differ')
        for row in rows:
            origin = row['test_origin'] == 'workspace'
            selected = row['checkout_value'] if origin else row['foreign_value']
            code = 0 if selected == 'after!' else 1
            if (not row['preflight_imports_intended_source']
                    or row['test_process_imports_intended_source'] != origin
                    or row['intended_checkout_assertion_passes'] != (row['checkout_value'] == 'after!')
                    or row['test_exit_code'] != code or row['identical_version'] != '0.0.1'
                    or not row['tracked_source_unchanged_by_probe_and_test']
                    or row['assertion_sha256'] != plan['assertion_sha256']
                    or row['policy_verdicts'] != driver.policies(code, True, origin, True)):
                raise ValueError('Recorded observation differs')
        calculated = driver.summarize(rows)
        if calculated != receipt['policy_summary']:
            raise ValueError('Recorded policy summary differs')
        summaries.append(calculated)
    data = json.loads((root/'model_evidence_scalars.json').read_bytes())
    if len(data['studies']) != 10 or any(len(s['assignments']) != 12 for s in data['studies']):
        raise ValueError('All ten planned twelve-slot studies required')
    sensitivity = coverage.compare(data['studies'])
    if sensitivity != json.loads((root/'model_missing_result_sensitivity.json').read_bytes()):
        raise ValueError('Recorded sensitivity differs')
    return dict(status='passed', manifest_members_verified=len(actual),
                original_repetitions_verified=2, policy_summaries_match=summaries[0] == summaries[1],
                model_assigned_slots=sensitivity['total_assigned'],
                scope='Byte identity and recorded consistency only; no fresh inference, native grading or phone work.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).parent)
    a = p.parse_args()
    print(json.dumps(verify(a.root), indent=2))

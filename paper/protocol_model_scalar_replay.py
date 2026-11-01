"""Recompute four recorded studies while keeping unavailable grades unknown."""
import hashlib
import json
from pathlib import Path


def summarize(study):
    arms = study['arms']
    outcomes = {arm: dict(assigned=0, completed=0, unattempted=0, verified_repairs=0,
        known_verifier_results=0, unknown_verifier_results=0, empty_patches=0,
        protected_test_conflicts=0) for arm in arms}
    pairs, seen = {}, set()
    for row in study['assignments']:
        key = row['arm'], row['task_id']
        if key in seen or row['arm'] not in outcomes:
            raise ValueError('Duplicate or undeclared assignment')
        seen.add(key)
        counts = outcomes[row['arm']]
        counts['assigned'] += 1
        pairs.setdefault(row['task_id'], {})[row['arm']] = row
        if row['status'] == 'unattempted':
            if any(row[k] is not None for k in ('verified_repair', 'test_exit_code', 'patch_bytes', 'known_verifier_result')):
                raise ValueError('Unattempted assignment carries an observed result')
            counts['unattempted'] += 1
        elif row['status'] == 'completed':
            counts['completed'] += 1
            if type(row['test_exit_code']) is not int or type(row['verified_repair']) is not bool:
                raise ValueError('Completed receipt lacks outcome scalars')
            known = row['test_exit_code'] >= 0
            if row['known_verifier_result'] != known:
                raise ValueError('Unknown verifier reclassified')
            if row['verified_repair'] and (not known or row['test_exit_code'] != 0 or not row['patch_bytes']):
                raise ValueError('Verified repair requires zero native exit and nonempty patch')
            counts['verified_repairs'] += row['verified_repair']
            counts['known_verifier_results'] += known
            counts['unknown_verifier_results'] += not known
            counts['empty_patches'] += row['patch_bytes'] == 0
            counts['protected_test_conflicts'] += row['protected_test_conflict']
        else:
            raise ValueError('Only completed or unattempted terminal assignments allowed')
    if len(seen) != 12 or len(pairs) != 6 or any(set(p) != set(arms) for p in pairs.values()):
        raise ValueError('Assigned six-case paired denominator differs')
    paired = dict(complete_execution_pairs=0, both_verifiers_known_pairs=0,
        first_only_verified_success=0, second_only_verified_success=0,
        shared_verified_success=0, neither_verified_success=0,
        execution_pairs_with_unavailable_verifier=0)
    for pair in pairs.values():
        a, b = (pair[arm] for arm in arms)
        if a['status'] != 'completed' or b['status'] != 'completed':
            continue
        paired['complete_execution_pairs'] += 1
        both_known = a['known_verifier_result'] and b['known_verifier_result']
        paired['both_verifiers_known_pairs'] += both_known
        paired['execution_pairs_with_unavailable_verifier'] += not both_known
        left, right = a['verified_repair'], b['verified_repair']
        key = ('shared_verified_success' if left and right else 'first_only_verified_success' if left
               else 'second_only_verified_success' if right else 'neither_verified_success')
        paired[key] += 1
    return dict(arms=outcomes, paired=paired,
        neither_verified_success_does_not_mean_both_known_failures=True)


def replay(root):
    manifest = json.loads((root / 'manifest.json').read_bytes())
    for row in manifest['files']:
        path = (root / row['path']).resolve(strict=True)
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Manifest escapes resource')
        raw = path.read_bytes()
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError('Resource member differs')
    data = json.loads((root / 'protocol_model_scalars.json').read_bytes())
    summaries = {study['name']: summarize(study) for study in data['studies']}
    expected = json.loads((root / 'protocol_model_expected.json').read_bytes())
    if summaries != expected:
        raise ValueError('Recomputed outcome denominators differ')
    return dict(scope='Recorded scalar recomputation; no inference, grader or independent authentication',
        summaries=summaries, missing_or_unknown_outcomes_imputed=False,
        model_improvement_established=False, leaderboard_prediction=None)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent), indent=2))

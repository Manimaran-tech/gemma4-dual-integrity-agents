"""Recompute retained development denominators; no model, task or grader execution."""
import hashlib
import json
from pathlib import Path


def replay(root):
    root = Path(root)
    manifest = json.loads((root / 'manifest.json').read_bytes())
    for row in manifest['files']:
        payload = (root / row['path']).read_bytes()
        if len(payload) != row['bytes'] or hashlib.sha256(payload).hexdigest() != row['sha256']:
            raise ValueError('Supplement member changed: ' + row['path'])
    data = json.loads((root / 'terminal_model_scalars.json').read_bytes())
    summaries = {}
    for study in data['studies']:
        arms = study['arms']
        if len(arms) != 2:
            raise ValueError('Expected exactly two preassigned arms')
        seen, outcomes = set(), {a: dict(assigned=0, completed=0, unattempted=0, verified_repairs=0,
                                         validation_unavailable=0) for a in arms}
        pairs = {}
        for row in study['assignments']:
            key = (row['arm'], row['task_id'])
            if key in seen or row['arm'] not in outcomes:
                raise ValueError('Duplicate or undeclared assignment')
            seen.add(key)
            arm = outcomes[row['arm']]
            arm['assigned'] += 1
            pairs.setdefault(row['task_id'], {})[row['arm']] = row
            if row['status'] == 'unattempted':
                arm['unattempted'] += 1
                if row.get('verified_resolved') is not None or row.get('test_exit_code') is not None:
                    raise ValueError('Missing assignment cannot carry an observed outcome')
            elif row['status'] == 'completed':
                arm['completed'] += 1
                if type(row['verified_resolved']) is not bool or type(row['test_exit_code']) is not int:
                    raise ValueError('Invalid native outcome scalar')
                repaired = row['verified_resolved'] and row['test_exit_code'] == 0 and row['patch_bytes'] > 0
                if repaired != row['verified_resolved']:
                    raise ValueError('Repair requires native resolved, zero exit and nonempty patch')
                arm['verified_repairs'] += repaired
                arm['validation_unavailable'] += row['test_exit_code'] == -1
            else:
                raise ValueError('Unexpected observation status')
        if len(seen) != 12 or len(pairs) != 6 or any(set(p) != set(arms) for p in pairs.values()):
            raise ValueError('Assigned denominators differ')
        paired = dict(complete_cases=0, first_arm_only=0, second_arm_only=0, both_repair=0, neither_repair=0)
        for pair in pairs.values():
            a, b = (pair[name] for name in arms)
            if a['status'] != 'completed' or b['status'] != 'completed':
                continue
            paired['complete_cases'] += 1
            left, right = a['verified_resolved'], b['verified_resolved']
            key = 'both_repair' if left and right else 'first_arm_only' if left else 'second_arm_only' if right else 'neither_repair'
            paired[key] += 1
        summaries[study['name']] = dict(arms=outcomes, paired=paired)
    expected = json.loads((root / 'terminal_model_expected.json').read_bytes())
    if summaries != expected:
        raise ValueError('Recomputed retained scalar summary differs')
    return dict(scope='Recorded scalar recomputation, not fresh inference or independent execution authentication',
                summaries=summaries, candidate_superiority_established=False, leaderboard_estimate=None)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent), indent=2))

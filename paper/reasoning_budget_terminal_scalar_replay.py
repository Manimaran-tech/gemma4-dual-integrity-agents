"""Recompute recorded ninth-study outcomes and censored tool counts."""
import json
from pathlib import Path

from protocol_model_scalar_replay import summarize as summarize_model


def replay(root):
    data = json.loads((root / 'protocol_model_scalars.json').read_bytes())
    extra = json.loads((root / 'reasoning_budget_terminal_scalars.json').read_bytes())
    studies = [s for s in data['studies'] if s['name'] == extra['study_name']]
    if len(studies) != 1:
        raise ValueError('Require exactly one recorded ninth study')
    study = studies[0]
    model = summarize_model(study)
    expected_keys = {(r['arm'], r['task_id']) for r in study['assignments']}
    rows = extra['tool_observations']
    if len(rows) != 12 or {(r['arm'], r['task_id']) for r in rows} != expected_keys:
        raise ValueError('Tool observations omit an assignment')
    total, completed, missing = 0, 0, 0
    for row in rows:
        original = next(r for r in study['assignments']
            if (r['arm'], r['task_id']) == (row['arm'], row['task_id']))
        if row['calls'] != sum(original['tool_calls_by_name'].values()):
            raise ValueError('Call denominator differs from native trace')
        if row['completed_calls'] + row['unreturned_calls'] != row['calls']:
            raise ValueError('Censored observations were dropped or imputed')
        total += row['calls']
        completed += row['completed_calls']
        missing += row['unreturned_calls']
    if (total, completed, missing) != (219, 218, 1):
        raise ValueError('Recorded tool completion counts differ')
    native = extra['synthetic_native_local_timeout_recovery']
    if (native['completed_checks'] != 4 or not native['recovery_verified']
            or native['unchanged_command_timeout_seconds'] != 300
            or native['model_inference_executed'] or native['verified_repairs'] is not None):
        raise ValueError('Synthetic integration was relabeled as model evidence')
    if (not extra['timing_components_unseparated']
            or extra['local_replay_is_issue_repair']
            or extra['hidden_score_failure_attributed']):
        raise ValueError('Interpretation boundaries changed')
    return dict(scope='Recorded scalar consistency, not independent grading or inference',
        model=model, observed_calls=total, completed_calls=completed,
        unreturned_calls=missing, missing_observations_imputed=False,
        synthetic_native_local_timeout_recovery=native)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent), indent=2))

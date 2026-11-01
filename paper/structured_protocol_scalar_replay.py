"""Recompute recorded structured-skill uptake; no model or native grader runs."""
from collections import Counter
import json
from pathlib import Path

from protocol_model_scalar_replay import replay as model_replay


def summarize(data):
    arms = data['arms']
    observed, kinds, statuses = {}, Counter(), Counter()
    for row in data['assignments']:
        key = row['arm'], row['task_id']
        if key in observed or row['arm'] not in arms:
            raise ValueError('Duplicate or undeclared assignment')
        observed[key] = row
        if row['verified_repair'] and (row['test_exit_code'] != 0 or not row['patch_bytes']):
            raise ValueError('Verified repair lacks native patch/grade evidence')
        for call in row['actual_skill_receipts']:
            if call['response_kind'] not in ('native_argument_rejection','script_argument_rejection',
                    'script_response','unclassified_or_unavailable_response','unparsed_script_response'):
                raise ValueError('Unknown response classification')
            if call['response_kind'] != 'script_response' and call['actual_script_status'] is not None:
                raise ValueError('Non-script response claims a script result')
            if call['elapsed_s'] is not None and call['elapsed_s'] < 0:
                raise ValueError('Negative elapsed time')
            if row['arm'] == data['candidate_arm']:
                kinds[call['response_kind']] += 1
                if call['actual_script_status'] is not None:
                    statuses[call['actual_script_status']] += 1
    cases = {case for _,case in observed}
    if len(observed) != 12 or len(cases) != 6 or any((a,c) not in observed for a in arms for c in cases):
        raise ValueError('Six paired exposed-case denominator differs')
    candidate_rows = [row for (arm,_),row in observed.items() if arm == data['candidate_arm']]
    candidate_success = [r for r in candidate_rows if r['verified_repair']]
    equal = all(r['source_sha256']['patch'] == observed[(data['baseline_arm'],r['task_id'])]['source_sha256']['patch']
                for r in candidate_success)
    counts = dict(assigned=12,completed_model_executions=len(observed),exposed_cases=len(cases),
        verified_repairs={a:sum(r['verified_repair'] for (arm,_),r in observed.items() if arm==a) for a in arms},
        unknown_verifiers={a:sum(r['test_exit_code']<0 for (arm,_),r in observed.items() if arm==a) for a in arms},
        candidate_skill_calls=sum(kinds.values()),candidate_response_kinds=dict(kinds),
        candidate_script_statuses=dict(statuses),
        candidate_native_or_CLI_argument_rejections=kinds['native_argument_rejection']+kinds['script_argument_rejection'],
        candidate_unclassified_responses=kinds['unclassified_or_unavailable_response'],
        candidate_empty_patches=sum(r['patch_bytes']==0 for r in candidate_rows),
        candidate_success_patches_equal_paired_parent=equal,
        unknown_results_imputed=False,independent_holdout=False,repair_gain_established=False)
    return counts


def replay(root):
    model_replay(root)  # Includes every manifest byte and all five model studies.
    data = json.loads((root/'structured_protocol_scalars.json').read_bytes())
    actual = summarize(data)
    expected = json.loads((root/'structured_protocol_expected.json').read_bytes())
    if actual != expected:
        raise ValueError('Recorded structured-protocol summary differs')
    return dict(scope='Recorded scalar recomputation; no new inference, native execution or independent authentication',
        structured_protocol=actual,model_inference_rerun=False,native_grader_rerun=False,
        official_score_prediction=None)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent),indent=2))

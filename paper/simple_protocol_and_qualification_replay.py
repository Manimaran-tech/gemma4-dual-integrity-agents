"""Recompute recorded tool-friction and qualification scalars without inference."""
from collections import Counter
import json
from pathlib import Path

from protocol_model_scalar_replay import replay as model_replay, summarize as summarize_model


def summarize(data, model_study):
    summary = summarize_model(model_study)
    candidate = data['candidate_arm']
    completed = {r['task_id']:r for r in model_study['assignments']
                 if r['arm'] == candidate and r['status'] == 'completed'}
    rows = data['candidate_protocol_rows']
    if len(rows) != len(completed) or len({r['task_id'] for r in rows}) != len(rows):
        raise ValueError('Candidate protocol denominator differs')
    operations, errors, responses = Counter(), Counter(), Counter()
    edits, checks, submits, unregistered, empty = 0, 0, 0, 0, 0
    success_times = []
    for row in rows:
        actual = completed[row['task_id']]
        if (row['verified_repair'] != actual['verified_repair'] or row['patch_bytes'] != actual['patch_bytes']
                or row['patch_sha256'] != actual['source_sha256']['patch']):
            raise ValueError('Protocol scalars differ from model evidence')
        operations.update(row['requested_operations'])
        errors.update(row['observed_error_categories'])
        empty += row['patch_bytes'] == 0
        checks += row['source_checked_assertion_calls']
        submits += row['explicit_submit_calls']
        unregistered += row['unregistered_tool_calls']
        for event in row['successful_edit_operations']:
            if event['operation'] != 'replace' or event['elapsed_s'] < 0:
                raise ValueError('Invalid successful edit scalar')
            edits += 1
            success_times.append(event['elapsed_s'])
        for call in row['actual_skill_receipts']:
            responses[call['response_kind']] += 1
            if call['elapsed_s'] is not None and call['elapsed_s'] < 0:
                raise ValueError('Negative tool elapsed time')
    if sum(operations.values()) != sum(responses.values()):
        raise ValueError('Operation requests and actual response count differ')
    cases = data['additional_qualification']['cases']
    if len(cases) != 8 or len({r['task_id'] for r in cases}) != 8:
        raise ValueError('Retain all eight qualification cases')
    qualified, classifications, repositories = [], Counter(), {}
    for row in cases:
        clean, reference = row['clean_base'], row['official_reference_patch']
        if clean['status'] != 'completed' or reference['status'] != 'completed':
            raise ValueError('Qualification control incomplete')
        if any(type(r['test_exit_code']) is not int or type(r['resolved']) is not bool for r in (clean,reference)):
            raise ValueError('Missing native control outcome')
        # Match the frozen fixture classifier: a command timeout (124) does not
        # establish an ordinary nonpassing clean base, even if its reference passes.
        valid = clean['test_exit_code'] in (1,2) and not clean['resolved'] and reference['test_exit_code'] == 0 and reference['resolved']
        if (row['classification'] == 'clean_base_nonpassing_reference_verified') != valid:
            raise ValueError('Qualification classification contradicts retained controls')
        if valid:
            qualified.append(row['task_id'])
        classifications[row['classification']] += 1
        repo = repositories.setdefault(row['repo'], dict(assigned=0,qualified=0))
        repo['assigned'] += 1
        repo['qualified'] += valid
    if qualified != data['additional_qualification']['qualified_case_ids_in_assigned_order']:
        raise ValueError('Qualified case order differs')
    paired = summary['paired']
    paired_successes = []
    observed = {(r['arm'],r['task_id']):r for r in model_study['assignments']}
    for task,row in completed.items():
        if row['verified_repair']:
            parent = observed[(data['baseline_arm'],task)]
            paired_successes.append(parent['status'] == 'completed' and parent['verified_repair']
                and parent['source_sha256']['patch'] == row['source_sha256']['patch'])
    return dict(model_summary=summary,candidate_completed=len(rows),candidate_empty_patches=empty,
        actual_skill_calls=sum(responses.values()),requested_operations=dict(operations),response_kinds=dict(responses),
        observed_error_categories=dict(errors),successful_edit_calls=edits,successful_edit_elapsed_s=success_times,
        source_checked_assertion_calls=checks,explicit_submit_calls=submits,unregistered_tool_calls=unregistered,
        candidate_success_patches_equal_verified_parent=all(paired_successes) if paired_successes else None,
        candidate_only_verified_repairs=paired['second_only_verified_success'],
        additional_qualification=dict(assigned_cases=8,completed_native_checks=16,qualified_cases=len(qualified),
            classifications=dict(classifications),repositories=repositories,qualified_case_ids_in_assigned_order=qualified),
        unknown_verifiers_imputed=False,unattempted_slots_imputed=False,
        qualification_is_model_repair=False,independent_holdout=False,repair_gain_established=False)


def replay(root):
    model_replay(root)
    models = json.loads((root/'protocol_model_scalars.json').read_bytes())
    study = next(s for s in models['studies'] if s['name'] == 'source_validation_vs_simple_interface')
    data = json.loads((root/'simple_protocol_and_qualification_scalars.json').read_bytes())
    actual = summarize(data,study)
    expected = json.loads((root/'simple_protocol_and_qualification_expected.json').read_bytes())
    if actual != expected:
        raise ValueError('Recomputed simple-protocol/qualification summary differs')
    return dict(scope='Recorded scalar recomputation; no new inference, grader, native execution or independent authentication',
        summary=actual,model_inference_rerun=False,native_grader_rerun=False,official_score_prediction=None)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent),indent=2))

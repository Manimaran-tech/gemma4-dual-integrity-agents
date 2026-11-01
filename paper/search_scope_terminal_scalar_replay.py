"""Recompute the eighth recorded study, bounded uptake and exploratory timing.

These are consistency checks on published scalars, not fresh inference, native
grading, independent authentication or a causal attribution of elapsed time.
"""
import hashlib
import json
import math
from pathlib import Path

from protocol_model_scalar_replay import summarize as summarize_model


def close(a, b):
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-8)


def summarize(extra, study):
    model = summarize_model(study)
    baseline, candidate = study['arms']
    assignments = {(r['arm'], r['task_id']): r for r in study['assignments']}
    rows = extra['assignment_observations']
    if len(rows) != 12 or {(r['arm'], r['task_id']) for r in rows} != set(assignments):
        raise ValueError('All twelve source-bound observations must be retained')
    seen, sums, gaps, edits = set(), [], [], []
    total_calls = 0
    for row in rows:
        key = row['arm'], row['task_id']
        if key in seen:
            raise ValueError('Duplicate observation')
        seen.add(key)
        original = assignments[key]
        if not row['original_compilation_matches']:
            raise ValueError('Original compilation identity not verified')
        if row['ordinary_agent_timeout']:
            if original['patch_bytes'] != 0 or original['known_verifier_result']:
                raise ValueError('Ordinary empty timeout must retain its unknown grade')
        if original['verified_repair'] and (not row['clean_production_diff'] or row['protected_paths_present']):
            raise ValueError('Verified delivery must retain its clean production diff')
        calls = row['tool_intervals']
        if len(calls) != sum(original['tool_calls_by_name'].values()):
            raise ValueError('Trace and assignment tool counts differ')
        durations, per_tool, row_gaps = [], {}, []
        for index, call in enumerate(calls):
            if call['group_size'] != 1 or call['start_s'] < 0 or call['end_s'] < call['start_s']:
                raise ValueError('A valid single-call interval is required')
            if not close(call['duration_s'], call['end_s'] - call['start_s']):
                raise ValueError('Recorded interval duration differs')
            durations.append(call['duration_s'])
            per_tool[call['tool']] = per_tool.get(call['tool'], 0) + 1
            if index:
                previous = calls[index - 1]
                if call['start_s'] < previous['start_s']:
                    raise ValueError('Intervals are not ordered by observed call time')
                row_gaps.append(max(0.0, call['start_s'] - previous['end_s']))
        if per_tool != original['tool_calls_by_name']:
            raise ValueError('Observed tool names differ')
        summed, largest_gap = sum(durations), max(row_gaps, default=0.0)
        if not close(summed, row['recorded_summed_tool_seconds']) or not close(largest_gap, row['recorded_largest_gap_seconds']):
            raise ValueError('Exploratory timing summary differs')
        sums.append(summed)
        gaps.append(largest_gap)
        total_calls += len(calls)
        if original['verified_repair'] and row['first_native_production_edit_s'] is not None:
            edits.append(row['first_native_production_edit_s'])
    uptake = extra['bounded_partial_uptake']
    if len(set(uptake['case_ids'])) != 3:
        raise ValueError('Uptake must remain limited to the first three case pairs')
    for task in uptake['case_ids']:
        for arm in study['arms']:
            r = assignments[arm, task]
            if r['status'] != 'completed' or r['patch_bytes'] or r['known_verifier_result']:
                raise ValueError('Partial uptake cases must retain their six unknown empty outcomes')
    for arm in study['arms']:
        counts = uptake['by_arm'][arm]
        if not 0 <= counts['explicit_path_calls'] <= counts['observed_rg_calls']:
            raise ValueError('Invalid bounded search denominator')
    if not 0 <= uptake['candidate_cases_calling_rg'] <= len(uptake['case_ids']):
        raise ValueError('Invalid bounded case denominator')
    if (not extra['search_input_descriptor_not_captured_in_GPU']
            or not extra['latency_components_not_separately_measured']
            or not extra['shell_source_edits_not_automatically_classified']
            or not extra['exposed_development_not_holdout']):
        raise ValueError('Required interpretation limits were removed')
    return dict(model=model, baseline_arm=baseline, candidate_arm=candidate,
        total_single_call_intervals=total_calls,
        summed_tool_seconds_per_task_min=min(sums), summed_tool_seconds_per_task_max=max(sums),
        largest_response_to_next_call_gap_seconds=max(gaps),
        latest_first_native_edit_seconds_among_verified_repairs=max(edits),
        bounded_partial_uptake=uptake, missing_or_unknown_outcomes_imputed=False,
        timing_is_post_outcome_exploratory=True, pure_model_thinking_time_measured=False,
        GPU_input_descriptor_verified=False, model_repair_improvement_established=False,
        official_score_prediction=None)


def replay(root):
    root = root.resolve()
    manifest = json.loads((root / 'manifest.json').read_bytes())
    for row in manifest['files']:
        path = (root / row['path']).resolve(strict=True)
        raw = path.read_bytes()
        if not path.is_relative_to(root) or len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError('Supplement bytes differ')
    data = json.loads((root / 'protocol_model_scalars.json').read_bytes())
    extra = json.loads((root / 'search_scope_terminal_scalars.json').read_bytes())
    matches = [s for s in data['studies'] if s['name'] == extra['study_name']]
    if len(matches) != 1:
        raise ValueError('Exactly one declared eighth study required')
    actual = summarize(extra, matches[0])
    expected = json.loads((root / 'search_scope_terminal_expected.json').read_bytes())
    if actual != expected:
        raise ValueError('Recomputed eighth-study evidence differs')
    return dict(scope='Recorded scalar replay; no inference, native grader or independent authentication', **actual)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent), indent=2))

"""Recompute recorded pipeline/search controls without model or grader inference."""
import hashlib
import json
from pathlib import Path

from protocol_model_scalar_replay import summarize as summarize_model


def summarize(data, study):
    model = summarize_model(study)
    if set(model['arms']) != {data['baseline_arm'], data['candidate_arm']}:
        raise ValueError('Pipeline arm identities differ')
    assignments = {(r['arm'], r['task_id']): r for r in study['assignments']}
    extra = data['pipeline_assignment_rows']
    if len(extra) != 12 or {(r['arm'], r['task_id']) for r in extra} != set(assignments):
        raise ValueError('Preserve all twelve pipeline assignments')
    clean_repairs, delivery = {arm: 0 for arm in study['arms']}, []
    cases = {}
    for row in extra:
        native = assignments[row['arm'], row['task_id']]
        if row['patch_sha256'] != native['source_sha256']['patch']:
            raise ValueError('Patch scalar identity differs')
        if not row['original_compilation_matches'] or row['planner_tool_calls']:
            raise ValueError('Compiled child boundary or planner tools differ')
        paths = row['patch_paths']
        module = 'fastapi/' if row['task_id'].startswith('fastapi_') else 'rich/'
        clean = bool(paths) and all(p.startswith(module) for p in paths)
        clean = clean and not row['ambiguous_paths'] and not row['protected_paths'] and not row['scratch_paths']
        if clean != row['clean_production_diff']:
            raise ValueError('Production-path classification differs')
        clean_repairs[row['arm']] += native['verified_repair'] and clean
        if row['ordinary_agent_timeout'] and (native['test_exit_code'] != -1 or native['patch_bytes']):
            raise ValueError('Ordinary timeout must retain an unknown verifier and empty patch')
        cases.setdefault(row['task_id'], {})[row['arm']] = (native, row)
    for task_id, arms in cases.items():
        baseline, candidate = (arms[data[name]] for name in ('baseline_arm', 'candidate_arm'))
        if candidate[0]['verified_repair'] and not baseline[0]['verified_repair'] and baseline[1]['ordinary_agent_timeout']:
            delivery.append(task_id)
    scope = data['native_search_controls']
    if len(scope['cases']) != 2 or scope['assigned_cases'] != 2:
        raise ValueError('Native search denominator differs')
    false_absence = []
    for case in scope['cases']:
        rows = case['conditions']
        if (len(rows) != 12 or case['charged_tool_calls'] != 12 or case['returned_patch_bytes'] != 0
                or not case['source_hashes_unchanged'] or not case['fd0_is_fifo']
                or not case['source_contains_query'] or not case['original100_sources_verified']):
            raise ValueError('Native read-only search boundary differs')
        for name in ('explicit_dot', 'explicit_file', 'empty_pipe_explicit_dot', 'devnull_no_path'):
            if rows[name]['exit_code'] != 0 or not rows[name]['query_in_stdout']:
                raise ValueError('Explicit/native positive search control differs')
        for name in ('empty_pipe_no_path', 'absent_pattern_explicit_dot'):
            if rows[name]['exit_code'] != 1 or rows[name]['stdout_lines']:
                raise ValueError('Native negative input/source control differs')
        if rows['matching_pipe_no_path']['exit_code'] != 0 or not rows['matching_pipe_no_path']['stdin_only_match']:
            raise ValueError('Native stdin-only control differs')
        inherited = rows['inherited_no_path']
        if inherited['exit_code'] == 1 and inherited['stdout_lines'] == 0:
            false_absence.append(case['task_id'])
    return dict(model=model, verified_clean_production_repairs=clean_repairs,
        candidate_verified_delivery_advantages=sorted(delivery),
        native_search_cases=2, native_charged_commands=24,
        inherited_no_path_false_absence_cases=sorted(false_absence),
        all_native_source_hashes_unchanged=True,
        CPU_controls_are_not_model_repairs=True, GPU_fd0_recorded=False,
        main_score_causality_established=False, held_out=False,
        whole12h_Stage1_runtime_established=False, prize_result_claimed=False)


def replay(root):
    manifest = json.loads((root / 'manifest.json').read_bytes())
    for member in manifest['files']:
        path = (root / member['path']).resolve(strict=True)
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Manifest escaped resource')
        raw = path.read_bytes()
        if len(raw) != member['bytes'] or hashlib.sha256(raw).hexdigest() != member['sha256']:
            raise ValueError('Resource member changed')
    data = json.loads((root / 'pipeline_and_search_scope_scalars.json').read_bytes())
    model = json.loads((root / 'protocol_model_scalars.json').read_bytes())
    study = next(s for s in model['studies'] if s['name'] == data['pipeline_study_name'])
    actual = summarize(data, study)
    if actual != json.loads((root / 'pipeline_and_search_scope_expected.json').read_bytes()):
        raise ValueError('Recorded pipeline/search scalar replay differs')
    return dict(scope='Recorded source-bound scalar recomputation, not independent model/grader authentication',
                summary=actual, unknown_or_missing_results_imputed=False)


if __name__ == '__main__':
    print(json.dumps(replay(Path(__file__).resolve().parent), indent=2))

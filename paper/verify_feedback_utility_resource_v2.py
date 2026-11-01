"""Byte verification, recorded decisions, and optional fresh API controls.

This never reruns a model or private organizer grader. Authored code: MIT.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile


def sha(raw):return hashlib.sha256(raw).hexdigest()


def library_scalars(actual):
    rows=actual['observations']
    if actual['status']!='completed' or len(rows)!=288 or actual['unknown_conditions']!=0:
        raise ValueError('Recorded library assignments incomplete')
    counts={name:dict(decisions=0,correct_supported_decisions=0,wrong_checkout_verdicts=0,
                     unsupported_source_claims=0,unknown=0) for name in actual['policy_summary']}
    for row in rows:
        off,on=(row['checks'][m] for m in ('observer_off','observer_on'))
        if on['exit_code'] not in (0,1) or off['exit_code']!=on['exit_code']:
            raise ValueError('API check incomplete or altered by observation')
        supported=row['selected_origin']=='workspace';verdict=on['exit_code']==0
        state=row['workspace_state'] if supported else row['foreign_state']
        if verdict!=(state=='original'):raise ValueError('Frozen assertion/source state differs')
        policy=dict(exit_only=verdict,version_and_exit=verdict,preflight_origin_and_exit=verdict,
                    actual_API_process_origin_and_exit=verdict if supported else None,always_unknown=None)
        if policy!=row['policy_verdicts']:raise ValueError('Recorded decision differs')
        for name,value in policy.items():
            c=counts[name]
            if value is None:c['unknown']+=1;continue
            wrong=value!=(row['workspace_state']=='original')
            c['decisions']+=1;c['wrong_checkout_verdicts']+=wrong
            c['unsupported_source_claims']+=not supported;c['correct_supported_decisions']+=not wrong and supported
    if counts!=actual['policy_summary']:raise ValueError('Recorded aggregate differs')
    return counts


def verify(root,fresh):
    root=root.resolve();manifest=json.loads((root/'manifest.json').read_bytes())
    names=set(manifest['files'])
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='manifest.json'}
    # Nested historical manifests are themselves pinned outer members.
    actual.update(p.relative_to(root).as_posix() for p in root.rglob('manifest.json') if p.parent!=root)
    if actual!=names:raise ValueError('Resource inventory differs')
    for name,record in manifest['files'].items():
        relative=PurePosixPath(name);p=root/name
        if relative.is_absolute() or '..' in relative.parts or '\\' in name or p.is_symlink() or not p.resolve().is_relative_to(root):
            raise ValueError('Unsafe member')
        raw=p.read_bytes()
        if len(raw)!=record['bytes'] or sha(raw)!=record['sha256']:raise ValueError('Member changed: '+name)
    windows=json.loads((root/'feedback_utility/windows_actual_public.json').read_bytes())
    linux=json.loads((root/'feedback_utility/linux_actual_public.json').read_bytes())
    ws,ls=library_scalars(windows),library_scalars(linux)
    if ws!=ls:raise ValueError('Retained OS results differ')
    audit=json.loads((root/'data/model_failure_census.json').read_bytes())
    assignments=audit['assignments'];counts={s:sum(r['grade_state']==s for r in assignments) for s in ('verified_repair','verified_failure','unknown')}
    if len(assignments)!=120 or counts!=audit['aggregate']['grade_states']:
        raise ValueError('Ten-study conservative denominator differs')
    phone=json.loads((root/'data/adaptive_phone_negative.json').read_bytes())
    if phone['patch_bytes']!=0 or phone['native_result']['repair'] is not False:
        raise ValueError('Retained negative phone result differs')
    memory=[json.loads(line) for line in (root/'data/adaptive_phone_memory.jsonl').read_text(encoding='utf-8').splitlines()]
    responses=json.loads((root/'data/adaptive_phone_response_scalars.json').read_bytes())
    tools=json.loads((root/'data/adaptive_phone_tool_scalars.json').read_bytes())
    health=json.loads((root/'data/adaptive_phone_health_scalars.json').read_bytes())
    if len(memory)!=phone['memory_samples'] or max(r['whole_app_pss_mib'] for r in memory)!=phone['sampled_maximum_whole_app_PSS_MiB']:
        raise ValueError('Actual recorded phone memory scalar differs')
    if len(responses)!=phone['model_responses'] or sum(r['success'] for r in tools)!=phone['successful_tools']:
        raise ValueError('Actual completed phone response/tool count differs')
    if [min(r['battery_temperature_C'] for r in health),max(r['battery_temperature_C'] for r in health)]!=phone['temperature_range_C']:
        raise ValueError('Actual phone thermal observations differ')
    if [min(r['thermal_status'] for r in health),max(r['thermal_status'] for r in health)]!=phone['thermal_status_range']:
        raise ValueError('Actual recorded thermal status differs')
    checks=[]
    for folder,script in [('legacy_v12','verify_provenance_resource.py'),('native_phone_original','replay_native_phone_evidence.py'),('process_feedback_original','verify_process_feedback_bundle.py')]:
        path=root/folder/script
        if not path.exists():continue
        p=subprocess.run([sys.executable,str(path)],cwd=path.parent,stdin=subprocess.DEVNULL,capture_output=True,timeout=240,check=False)
        if p.returncode:raise RuntimeError('Historical recorded replay failed: '+folder)
        checks.append(dict(name=folder,role='recorded_scalar_and_bytes_not_new_inference',exit_code=0,stdout_sha256=sha(p.stdout)))
    fresh_summary=None
    if fresh:
        with tempfile.TemporaryDirectory(prefix='fresh_public_api_') as temporary:
            output=Path(temporary)/'actual.json'
            p=subprocess.run([sys.executable,str(root/'feedback_utility/feedback_utility_replay.py'),
                '--snapshot-root',str(root/'feedback_utility'),'--plan',str(root/'feedback_utility/plan.json'),
                '--output',str(output)],stdin=subprocess.DEVNULL,capture_output=True,timeout=1200,check=False)
            if p.returncode or not output.exists():raise RuntimeError('Fresh packaged API controls failed')
            fresh_actual=json.loads(output.read_bytes());fresh_summary=library_scalars(fresh_actual)
            if fresh_summary!=ws:raise ValueError('Fresh packaged invariants differ')
            checks.append(dict(name='fresh_three_library_288_conditions',role='new_model_free_API_controls',
                exit_code=0,actual_sha256=sha(output.read_bytes()),stdout_sha256=sha(p.stdout)))
    return dict(observed_utc=datetime.now(timezone.utc).isoformat(),status='verified',
        manifest_members_verified=len(names),per_OS_recorded_library_conditions=288,
        retained_OS_policy_counts_identical=True,policy_summary=ws,model_audit_grade_states=counts,
        historical_replays=checks,fresh_API_controls_executed=fresh,fresh_policy_summary=fresh_summary,
        model_or_private_grader_reexecuted=False,physical_phone_executed=False,award_or_population_gain_established=False)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--fresh',action='store_true');a=p.parse_args()
    print(json.dumps(verify(Path(__file__).resolve().parent,a.fresh),indent=2))

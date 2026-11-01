"""Frozen API/source-selection controls on real library snapshots; no model repairs."""
import argparse
from datetime import datetime, timezone
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

GRID = list(itertools.product(('flat','src'), ('faulty','original'), ('faulty','original'),
    ('workspace','foreign'), ('fresh_same_interpreter','fresh_other_interpreter','nested_worker_other_interpreter')))

OBSERVER = '''import hashlib,json,os,pathlib,sys
evidence=[]
for name in json.loads(os.environ["OBSERVED_MODULES"]):
    m=sys.modules.get(name)
    f=getattr(m,"__file__",None)
    p=pathlib.Path(f).resolve() if f else None
    evidence.append({"module":name,"path":str(p) if p else None,
        "sha256":hashlib.sha256(p.read_bytes()).hexdigest() if p and p.is_file() else None})
root=sys.modules.get(os.environ["ROOT_MODULE"])
print("ACTUAL_API_PROCESS="+json.dumps({"pid":os.getpid(),"executable":sys.executable,
    "version":getattr(root,"__version__",None),"modules":evidence}),flush=True)
'''


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


def call(args, env, cwd, timeout=20):
    started=time.monotonic()
    try:
        r=subprocess.run([str(a) for a in args],stdin=subprocess.DEVNULL,capture_output=True,
            cwd=cwd,env=env,timeout=timeout,check=False)
        return dict(exit_code=r.returncode,stdout=r.stdout.decode('utf-8','replace'),
            stderr=r.stderr.decode('utf-8','replace'),elapsed_seconds=time.monotonic()-started,timeout=False)
    except subprocess.TimeoutExpired as e:
        return dict(exit_code=None,stdout=(e.stdout or b'').decode('utf-8','replace'),
            stderr=(e.stderr or b'').decode('utf-8','replace'),elapsed_seconds=time.monotonic()-started,timeout=True)


def receipt(record, marker):
    values=[]
    for line in record['stdout'].splitlines():
        if line.startswith(marker):
            values.append(json.loads(line[len(marker):]))
    return values[0] if len(values)==1 else None


def correct_origin(value, expected, version):
    return bool(value and value['version']==version and len(value['modules'])==len(expected)
        and all(r['path']==p and r['sha256']==d for r,(p,d) in zip(value['modules'],expected)))


def policy_summary(rows):
    names=('exit_only','version_and_exit','preflight_origin_and_exit','actual_API_process_origin_and_exit','always_unknown')
    result={name:dict(decisions=0,correct_supported_decisions=0,wrong_checkout_verdicts=0,unsupported_source_claims=0,unknown=0) for name in names}
    for row in rows:
        for name,verdict in row['policy_verdicts'].items():
            c=result[name]
            if verdict is None:
                c['unknown']+=1;continue
            wrong=verdict!=row['intended_assertion_passes']
            supported=row['actual_API_process_origin_matches_intended']
            c['decisions']+=1;c['wrong_checkout_verdicts']+=wrong
            c['unsupported_source_claims']+=not supported
            c['correct_supported_decisions']+=not wrong and supported
    return result


def make_plan(snapshot_root, repetitions=2):
    manifest=json.loads((snapshot_root/'snapshot_manifest.json').read_bytes())
    return dict(format='real_library_feedback_utility_v1',created_utc=datetime.now(timezone.utc).isoformat(),
        driver_sha256=sha(Path(__file__).read_bytes()),snapshot_manifest_sha256=sha((snapshot_root/'snapshot_manifest.json').read_bytes()),
        projects=manifest['projects'],conditions=[list(x) for x in GRID],repetitions=repetitions,
        assigned_conditions=len(manifest['projects'])*len(GRID)*repetitions,
        observer_on_and_off_checks_per_condition=2,assertions_unchanged=True,
        intervention='Controlled same-length source faults; same-version foreign copies; direct and nested fresh processes in two isolated interpreters.',
        selected_projects_fixed_before_execution=True,source_hashes_are_post_check_file_observations=True,
        no_source_or_assertion_mutation_between_preflight_and_check=True,
        no_claim_about_exact_executed_bytes_or_all_imports=True,
        comparison_is_constructed_mechanism_not_natural_fault_prevalence=True,
        network_or_dependency_installation_required=False,models_or_phone_accessed=False,
        regression_faults_are_not_natural_issues_or_agent_repairs=True,
        stop_rule='Preserve all assignments and setup exceptions; no project replacement or selective reruns.')


def run(snapshot_root, plan_path, output):
    plan=json.loads(plan_path.read_bytes()); expected=make_plan(snapshot_root,plan['repetitions'])
    for key in ('format','driver_sha256','snapshot_manifest_sha256','projects','conditions','assigned_conditions'):
        if plan[key]!=expected[key]:
            raise ValueError('Frozen protocol changed: '+key)
    manifest=json.loads((snapshot_root/'snapshot_manifest.json').read_bytes())
    for name,digest in manifest['files'].items():
        if sha((snapshot_root/name).read_bytes())!=digest:
            raise ValueError('Source/license snapshot changed')
    if output.exists():
        raise FileExistsError('Preserve the original run')
    report=dict(created_utc=datetime.now(timezone.utc).isoformat(),status='started',
        plan_sha256=sha(plan_path.read_bytes()),driver_sha256=sha(Path(__file__).read_bytes()),
        runtime=dict(system=platform.system(),python=sys.version,executable=sys.executable),
        assigned_conditions=plan['assigned_conditions'],completed_conditions=0,unknown_conditions=0,
        observations=[],qualification=[],model_inference_executed=False,phone_accessed=False)
    def save():
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    save()
    try:
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1',PIP_NO_INDEX='1')
        env.pop('PYTHONPATH',None)
        with tempfile.TemporaryDirectory(prefix='paper_real_feedback_') as temporary:
            root=Path(temporary).resolve()
            interpreters=[]
            for n in range(2):
                v=root/('env'+str(n))
                result=call([sys.executable,'-m','venv','--without-pip',v],env,root,timeout=60)
                if result['exit_code']!=0:
                    raise RuntimeError('Isolated interpreter setup failed: '+json.dumps(result))
                interpreters.append(v/('Scripts/python.exe' if os.name=='nt' else 'bin/python'))
            for project in plan['projects']:
                name=project['name']; module_paths=[name+'/__init__.py',project['edited_path']]
                source=snapshot_root/'sources'/name
                correct=(source/project['edited_path']).read_bytes()
                old,new=project['fault']['old'].encode(),project['fault']['new'].encode()
                if correct.count(old)!=1 or len(old)!=len(new):
                    raise ValueError('Fault selector/length differs')
                faulty=correct.replace(old,new)
                script=root/(name+'_check.py')
                # Assertions execute before the observer; it never preloads the target.
                body="import sys\nexit_code=0\ntry:\n    exec(compile("+repr(project['assertion'])+", 'frozen_API_assertion', 'exec'))\nexcept AssertionError:\n    exit_code=1\nexcept Exception:\n    import traceback\n    traceback.print_exc()\n    exit_code=2\n"
                observer_script=body+OBSERVER+'\nsys.exit(exit_code)\n'
                plain_script=body+'\nsys.exit(exit_code)\n'
                probe=root/(name+'_probe.py')
                probe.write_text('import importlib\n'+'\n'.join('importlib.import_module('+repr(m)+')' for m in project['observed_modules'])+'\n'+OBSERVER,encoding='utf-8')
                repos={}
                for layout in ('flat','src'):
                    for origin in ('workspace','foreign'):
                        repo=root/name/layout/origin; imports=repo/('src' if layout=='src' else '')
                        shutil.copytree(source/name,imports/name)
                        repos[(layout,origin)]=imports
                process_env=dict(env,ROOT_MODULE=name,OBSERVED_MODULES=json.dumps(project['observed_modules']))
                qualification=[]
                qroot=repos[('flat','workspace')]
                for state,payload in [('faulty',faulty),('original',correct)]:
                    (qroot/project['edited_path']).write_bytes(payload)
                    script.write_text(observer_script,encoding='utf-8')
                    record=call([interpreters[0],script],dict(process_env,PYTHONPATH=str(qroot)),root)
                    qualification.append(dict(project=name,state=state,record=record))
                qualified=qualification[0]['record']['exit_code']==1 and qualification[1]['record']['exit_code']==0
                report['qualification'].extend(qualification);save()
                for repetition in range(1,plan['repetitions']+1):
                    for layout,wstate,fstate,selected,boundary in plan['conditions']:
                        workspace,foreign=repos[(layout,'workspace')],repos[(layout,'foreign')]
                        for folder,state in [(workspace,wstate),(foreign,fstate)]:
                            (folder/project['edited_path']).write_bytes(correct if state=='original' else faulty)
                        intended=[(str((workspace/p).resolve()),sha((workspace/p).read_bytes())) for p in module_paths]
                        before={str(folder/p):sha((folder/p).read_bytes()) for folder in (workspace,foreign) for p in module_paths}
                        preflight=call([interpreters[0],probe],dict(process_env,PYTHONPATH=str(workspace)),root)
                        pre=receipt(preflight,'ACTUAL_API_PROCESS=')
                        observed=None; outcomes={}
                        for mode,code in [('observer_off',plain_script),('observer_on',observer_script)]:
                            script.write_text(code,encoding='utf-8')
                            selected_root=workspace if selected=='workspace' else foreign
                            selected_env=dict(process_env,PYTHONPATH=str(selected_root))
                            python=interpreters[0] if boundary=='fresh_same_interpreter' else interpreters[1]
                            command=[python,script]
                            if boundary=='nested_worker_other_interpreter':
                                # Parent preloads intended source, but worker has its own selected path.
                                parent=root/(name+'_parent.py')
                                parent_code='import importlib,os,subprocess,sys\n'+'\n'.join('importlib.import_module('+repr(m)+')' for m in project['observed_modules'])+'\n'
                                parent_code+= 'e=dict(os.environ,PYTHONPATH='+repr(str(selected_root))+')\nr=subprocess.run(['+repr(str(python))+','+repr(str(script))+'],env=e,stdin=subprocess.DEVNULL)\nsys.exit(r.returncode)\n'
                                parent.write_text(parent_code,encoding='utf-8')
                                command=[interpreters[0],parent];selected_env=dict(process_env,PYTHONPATH=str(workspace))
                            result=call(command,selected_env,root)
                            outcomes[mode]=result
                            if mode=='observer_on':
                                observed=receipt(result,'ACTUAL_API_PROCESS=')
                        if any(sha(Path(p).read_bytes())!=h for p,h in before.items()):
                            raise ValueError('Source changed between preflight and check')
                        match=correct_origin(observed,intended,project['version'])
                        observer_same=outcomes['observer_on']['exit_code']==outcomes['observer_off']['exit_code']
                        code=outcomes['observer_on']['exit_code']
                        verdict=bool(code==0) if qualified and observer_same and code in (0,1) else None
                        policies=dict(exit_only=verdict,
                            version_and_exit=verdict if observed and observed['version']==project['version'] else None,
                            preflight_origin_and_exit=verdict if correct_origin(pre,intended,project['version']) else None,
                            actual_API_process_origin_and_exit=verdict if match else None,always_unknown=None)
                        report['observations'].append(dict(project=name,repetition=repetition,layout=layout,
                            workspace_state=wstate,foreign_state=fstate,selected_origin=selected,boundary=boundary,
                            intended_assertion_passes=wstate=='original',project_fixture_qualified=qualified,
                            actual_API_process_origin_matches_intended=match,observer_exit_unchanged=observer_same,
                            preflight=preflight,actual_origin=observed,checks=outcomes,policy_verdicts=policies))
                        report['completed_conditions']+=1;report['unknown_conditions']+=verdict is None
                        save()
            report['policy_summary']=policy_summary(report['observations'])
            report['observer_exit_changes']=sum(not r['observer_exit_unchanged'] for r in report['observations'])
            report['status']='completed'
    except Exception as error:
        report.update(status='failed',error_type=type(error).__name__,error=str(error))
        raise
    finally:
        report['unattempted_conditions']=report['assigned_conditions']-report['completed_conditions'];save()
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot-root',type=Path,required=True)
    parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=run(args.snapshot_root,args.plan,args.output)
    print(json.dumps({k:result[k] for k in ('status','assigned_conditions','completed_conditions','unknown_conditions','observer_exit_changes','policy_summary')}))

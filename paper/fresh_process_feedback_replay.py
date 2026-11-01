"""Test whether a successful preflight proves the origin used by a later check.

Two layouts of one synthetic package, fixed assertion/version, no network,
dependency installation, competition inputs, model or phone commands.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

MODULE = 'process_feedback_control'
CHECK = '''import hashlib,importlib,json,pathlib
m=importlib.import_module("process_feedback_control")
p=pathlib.Path(m.__file__).resolve()
print("TEST_PROCESS_ORIGIN="+json.dumps({"origin":str(p),"version":m.__version__,
    "value":m.VALUE,"source_sha256":hashlib.sha256(p.read_bytes()).hexdigest()}),flush=True)
assert m.VALUE == "after!"
'''
GRID = list(itertools.product(('flat', 'src'), ('before', 'after!'), ('before', 'after!'), ('workspace', 'foreign')))


def sha(data): return hashlib.sha256(data).hexdigest()


def call(args, **kwargs):
    return subprocess.run([str(a) for a in args], capture_output=True, timeout=45, check=True, **kwargs)


def make_plan(guard):
    return dict(format='fresh_process_feedback_plan_v1', created_utc=datetime.now(timezone.utc).isoformat(),
        guard_sha256=sha(guard.read_bytes()), driver_sha256=sha(Path(__file__).read_bytes()),
        assertion_sha256=sha(CHECK.encode()), conditions=[list(c) for c in GRID],
        intervention='Preflight always imports intended source; subsequent test receives the frozen selected source path.',
        source_or_assertion_mutation_between_probe_and_test=False,
        scope='Sixteen conditions on two layouts of one synthetic package, not16 repair tasks.')


def policies(exit_code, preflight_ok, actual_origin_ok, version_ok):
    verdict = True if exit_code == 0 else False if exit_code == 1 else None
    return dict(exit_only=verdict, version_and_exit=verdict if version_ok else None,
        preflight_origin_and_exit=verdict if preflight_ok else None,
        test_process_origin_and_exit=verdict if actual_origin_ok else None, always_unknown=None)


def summarize(observations):
    counts={name:dict(decisions=0, wrong_checkout_verdicts=0, unsupported_source_claims=0, unknown=0)
            for name in ('exit_only','version_and_exit','preflight_origin_and_exit','test_process_origin_and_exit','always_unknown')}
    for row in observations:
        for name, verdict in row['policy_verdicts'].items():
            c=counts[name]
            if verdict is None: c['unknown']+=1; continue
            c['decisions']+=1
            c['wrong_checkout_verdicts']+=verdict != row['intended_checkout_assertion_passes']
            c['unsupported_source_claims']+=not row['test_process_imports_intended_source']
    return counts


def run(guard, plan):
    frozen=json.loads(plan.read_bytes())
    expected=make_plan(guard)
    for key in ('format','guard_sha256','driver_sha256','assertion_sha256','conditions'):
        if frozen[key]!=expected[key]:raise ValueError('Frozen experiment changed: '+key)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1',PIP_NO_INDEX='1')
    env.pop('PYTHONPATH',None)
    observations=[]
    temporary_base=Path(tempfile.gettempdir()).resolve()
    with tempfile.TemporaryDirectory(prefix='paper_process_feedback_',dir=temporary_base) as temporary:
        root=Path(temporary).resolve()
        if not root.is_relative_to(temporary_base) or not root.name.startswith('paper_process_feedback_'):
            raise ValueError('Temporary workspace boundary differs')
        virtual=root/'environment'
        call([sys.executable,'-m','venv','--without-pip',virtual],env=env)
        python=virtual/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        foreign=root/'foreign'; foreign.mkdir()
        foreign_source=foreign/(MODULE+'.py')
        assertion=root/'fixed_assertion.py';assertion.write_bytes(CHECK.encode())
        repos={}
        for layout in ('flat','src'):
            repo=root/layout
            folder=repo/('src' if layout=='src' else '')/MODULE;folder.mkdir(parents=True)
            source=folder/'__init__.py';source.write_bytes(b'__version__="0.0.1"\nVALUE="before"\n')
            call(['git','init','-q',repo]);call(['git','-C',repo,'add','.'])
            call(['git','-C',repo,'-c','user.name=Process Feedback Control','-c','user.email=control@example.invalid','commit','-qm','synthetic fixture'])
            repos[layout]=(repo,source)
        for layout, checkout_value, foreign_value, selected in GRID:
            repo,source=repos[layout]
            source.write_bytes(f'__version__="0.0.1"\nVALUE="{checkout_value}"\n'.encode())
            foreign_source.write_bytes(f'__version__="0.0.1"\nVALUE="{foreign_value}"\n'.encode())
            intended_path=repo/'src' if layout=='src' else repo
            preflight_env=dict(env,PYTHONPATH=str(intended_path))
            before_diff=call(['git','-C',repo,'diff','--binary','HEAD']).stdout
            inspected=subprocess.run([str(python),str(guard),'--workspace',str(repo),'--module',MODULE],
                cwd=repo,env=preflight_env,capture_output=True,timeout=30)
            lines=[l for l in inspected.stdout.decode().splitlines() if l.startswith('SOURCE_IMPORT_GUARD=')]
            if len(lines)!=1:raise ValueError('Preflight did not emit one receipt')
            preflight=json.loads(lines[0].split('=',1)[1])
            if inspected.returncode!=0 or preflight['success'] is not True or preflight['installation_attempted']:
                raise ValueError('Frozen preflight did not select intended source')
            test_path=intended_path if selected=='workspace' else foreign
            actual=subprocess.run([str(python),'-B','-s',str(assertion)],cwd=repo,
                env=dict(env,PYTHONPATH=str(test_path)),capture_output=True,timeout=15)
            lines=[l for l in actual.stdout.decode().splitlines() if l.startswith('TEST_PROCESS_ORIGIN=')]
            if len(lines)!=1:raise ValueError('Missing test-process source inventory')
            tested=json.loads(lines[0].split('=',1)[1])
            expected_source=source if selected=='workspace' else foreign_source
            expected_value=checkout_value if selected=='workspace' else foreign_value
            if (Path(tested['origin']).resolve()!=expected_source.resolve() or tested['source_sha256']!=sha(expected_source.read_bytes())
                    or tested['value']!=expected_value or tested['version']!='0.0.1'
                    or actual.returncode!=(0 if expected_value=='after!' else 1)
                    or assertion.read_bytes()!=CHECK.encode() or before_diff!=call(['git','-C',repo,'diff','--binary','HEAD']).stdout):
                raise ValueError('Fixed assertion, expected origin, bytes or source preservation differs')
            origin_ok=Path(tested['origin']).resolve()==source.resolve()
            observations.append(dict(layout=layout,checkout_value=checkout_value,foreign_value=foreign_value,
                test_origin=selected,preflight_imports_intended_source=True,test_process_imports_intended_source=origin_ok,
                identical_version='0.0.1',test_exit_code=actual.returncode,
                intended_checkout_assertion_passes=checkout_value=='after!',
                policy_verdicts=policies(actual.returncode,True,origin_ok,True),
                preflight_receipt_sha256=sha(inspected.stdout),test_stdout_sha256=sha(actual.stdout),
                test_stderr_sha256=sha(actual.stderr),assertion_sha256=sha(CHECK.encode()),
                imported_source_sha256=tested['source_sha256'],tracked_source_unchanged_by_probe_and_test=True))
    return dict(created_utc=datetime.now(timezone.utc).isoformat(),status='completed',scope=frozen['scope'],
        assigned_conditions=16,completed_conditions=len(observations),python_version=platform.python_version(),platform=platform.platform(),
        plan_sha256=sha(plan.read_bytes()),driver_sha256=frozen['driver_sha256'],guard_sha256=frozen['guard_sha256'],
        observations=observations,policy_summary=summarize(observations),source_guard_implementation_changed=False,
        actual_model_phone_or_native_competition_verifier_executed=False,natural_fault_prevalence_established=False,
        general_repair_accuracy_improvement_established=False)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--guard',type=Path,required=True)
    p.add_argument('--plan',type=Path,required=True)
    p.add_argument('--freeze',action='store_true')
    p.add_argument('--output',type=Path)
    a=p.parse_args();guard=a.guard.resolve(strict=True)
    if a.freeze:
        a.plan.open('x',encoding='utf-8').write(json.dumps(make_plan(guard),indent=2)+'\n')
        print(json.dumps({'plan_frozen':True,'experiment_executed':False}))
    else:
        result=run(guard,a.plan.resolve(strict=True))
        if a.output:a.output.open('x',encoding='utf-8').write(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result['policy_summary'],indent=2))

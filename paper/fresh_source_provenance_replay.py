"""Run fresh offline controls in disposable repositories, without Kaggle data.

Usage: python fresh_source_provenance_replay.py --guard source_import_guard.py
Requires Python 3.11+, Git, pip and locally installed setuptools/wheel.
The script creates isolated environments and never downloads dependencies.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile


def command(args, **kwargs):
    return subprocess.run([str(arg) for arg in args], capture_output=True, text=True,
                          timeout=90, check=True, **kwargs)


def make_repo(root, name, layout):
    repo = root / name
    package = repo / layout / name
    package.mkdir(parents=True)
    source = package / '__init__.py'
    source.write_text('VALUE = "before"\n', encoding='utf-8')
    (repo / 'pyproject.toml').write_text(
        '[build-system]\nrequires=["setuptools","wheel"]\n'
        'build-backend="setuptools.build_meta"\n'
        f'[project]\nname="{name}"\nversion="0.0.1"\n', encoding='utf-8')
    command(['git','init','-q',repo])
    command(['git','-C',repo,'add','.'])
    command(['git','-C',repo,'-c','user.name=Provenance Control',
             '-c','user.email=control@example.invalid','commit','-qm','synthetic baseline'])
    return repo, source


def guard_call(python, guard, repo, name, env, ensure):
    args = [str(python),str(guard),'--workspace',str(repo),'--module',name]
    if ensure:
        args.append('--ensure')
    result = subprocess.run(args, cwd=repo.parent, env=env, capture_output=True,
                            text=True, timeout=90, check=False)
    lines = [line for line in result.stdout.splitlines() if line.startswith('SOURCE_IMPORT_GUARD=')]
    if len(lines) != 1:
        raise ValueError('Missing guard receipt')
    return result.returncode, json.loads(lines[0].split('=',1)[1])


def value_check(python, repo, name, env):
    code = f'import {name}; assert {name}.VALUE == "after!"'
    with tempfile.TemporaryDirectory(prefix='fresh_replay_cache_') as cache:
        result = subprocess.run([str(python),'-B','-s','-X','pycache_prefix='+cache,'-c',code],
            cwd=repo,env=env,capture_output=True,text=True,timeout=15,check=False)
    return result.returncode


def run(guard):
    # Check prerequisites before interpreting any missing import as a behavior failure.
    prerequisites = {name:importlib.metadata.version(name) for name in ('pip','setuptools','wheel')}
    git_version = command(['git','--version']).stdout.strip()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1',
               PIP_NO_INDEX='1', PIP_DISABLE_PIP_VERSION_CHECK='1')
    env.pop('PYTHONPATH',None)
    observations = []
    with tempfile.TemporaryDirectory(prefix='fresh_source_provenance_') as temporary:
        root = Path(temporary)
        venv_root = root / 'environment'
        command([sys.executable,'-m','venv','--system-site-packages',venv_root], env=env)
        python = venv_root / ('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        for layout, name in [('', 'replay_flat_control'), ('src', 'replay_src_control')]:
            repo, source = make_repo(root,name,layout)
            _, inspected = guard_call(python,guard,repo,name,env,False)
            exit_code, ensured = guard_call(python,guard,repo,name,env,True)
            if exit_code or not ensured['success']:
                raise ValueError('Fresh source setup did not qualify: '+ensured['status'])
            before = value_check(python,repo,name,env)
            source.write_text('VALUE = "after!"\n',encoding='utf-8')
            after = value_check(python,repo,name,env)
            _, repeated = guard_call(python,guard,repo,name,env,True)
            if before!=1 or after!=0 or repeated['installation_attempted']:
                raise ValueError('Fixed assertion or conditional installation control failed')
            observations.append({'layout':layout or 'flat',
                'before_workspace_import':inspected['before']['imports_expected_source'],
                'after_workspace_import':ensured['after']['imports_expected_source'],
                'installation_attempted':ensured['installation_attempted'],
                'tracked_diff_unchanged_by_setup':ensured['tracked_diff_unchanged'],
                'same_assertion_before_exit_code':before,'same_assertion_after_exit_code':after,
                'repeat_installation_skipped':not repeated['installation_attempted']})
        name = 'replay_shadow_control'
        repo, _ = make_repo(root,name,'src')
        foreign = root / 'foreign'
        foreign.mkdir()
        (foreign / (name+'.py')).write_text('VALUE="foreign"\n',encoding='utf-8')
        shadow_env = dict(env, PYTHONPATH=str(foreign))
        exit_code, shadow = guard_call(python,guard,repo,name,shadow_env,True)
        if exit_code!=2 or shadow['status']!='installation_did_not_select_source':
            raise ValueError('Foreign import negative control was incorrectly qualified')
        observations.append({'layout':'src_with_foreign_pythonpath',
            'reported_status':shadow['status'],'success':shadow['success'],
            'after_workspace_import':shadow['after']['imports_expected_source'],
            'tracked_diff_unchanged_by_setup':shadow['tracked_diff_unchanged']})
    return {'created_utc':datetime.now(timezone.utc).isoformat(),'status':'completed',
        'scope':'Fresh repository-independent synthetic provenance controls, not repair tasks',
        'python_version':platform.python_version(),'platform':platform.platform(),
        'prerequisites':prerequisites,'git_version':git_version,
        'guard_sha256':hashlib.sha256(guard.read_bytes()).hexdigest(),
        'replay_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'observations':observations,'assigned_controls':3,
        'fresh_processes_and_source_edits_executed':True,
        'network_or_dependency_resolution_enabled':False,
        'competition_input_model_or_verifier_used':False,
        'repair_gain_or_private_scoring_equivalence_established':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--guard',type=Path,default=Path(__file__).with_name('source_import_guard.py'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run(args.guard.resolve(strict=True))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as stream:
            stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

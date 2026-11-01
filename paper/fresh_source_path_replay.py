"""Fresh missing-backend control; explicit environment is required for validation."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from fresh_source_provenance_replay import command, make_repo, value_check


def run(guard):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1',PIP_NO_INDEX='1')
    env.pop('PYTHONPATH',None)
    with tempfile.TemporaryDirectory(prefix='fresh_source_path_') as temporary:
        root=Path(temporary)
        virtual=root/'environment'
        command([sys.executable,'-m','venv','--system-site-packages',virtual],env=env)
        python=virtual/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        name='replay_missing_backend_control'
        repo,source=make_repo(root,name,'src')
        (repo/'pyproject.toml').write_text('[build-system]\nrequires=[]\nbuild-backend="missing_provenance_backend"\n')
        command(['git','-C',repo,'add','pyproject.toml'])
        command(['git','-C',repo,'-c','user.name=Provenance Control','-c',
                 'user.email=control@example.invalid','commit','-qm','missing backend control'])
        args=[str(python),str(guard),'--workspace',str(repo),'--module',name,'--ensure']
        base=subprocess.run(args,env=env,capture_output=True,text=True,timeout=90)
        base_result=json.loads(base.stdout.split('SOURCE_IMPORT_GUARD=',1)[1])
        fixed=subprocess.run(args+['--allow-source-path'],env=env,capture_output=True,text=True,timeout=90)
        fixed_result=json.loads(fixed.stdout.split('SOURCE_IMPORT_GUARD=',1)[1])
        if base.returncode!=2 or base_result['status']!='build_backend_unavailable_offline' or fixed.returncode!=0:
            raise ValueError('Missing-backend control did not retain its original failure')
        verified_env={**env,**fixed_result['validation_environment']}
        before=value_check(python,repo,name,verified_env)
        source.write_text('VALUE = "after!"\n')
        after=value_check(python,repo,name,verified_env)
        omitted=value_check(python,repo,name,env)
        if before!=1 or after!=0 or omitted==0 or fixed_result['installation_attempted']:
            raise ValueError('Environment or fixed-assertion boundary changed')
        observation={'default_guard_status':base_result['status'],
            'explicit_guard_status':fixed_result['status'],
            'default_imports_fixed':fixed_result['default_imports_fixed'],
            'installation_attempted':fixed_result['installation_attempted'],
            'tracked_diff_unchanged_by_setup':fixed_result['tracked_diff_unchanged'],
            'same_assertion_before_exit_code':before,'same_assertion_after_exit_code':after,
            'same_assertion_without_explicit_environment_exit_code':omitted,
            'source_import_verified_in_explicit_environment':fixed_result['validation_inventory']['imports_expected_source']}
    return {'created_utc':datetime.now(timezone.utc).isoformat(),'status':'completed',
        'scope':'Fresh synthetic source-path validation control without installing a missing backend',
        'guard_sha256':hashlib.sha256(guard.read_bytes()).hexdigest(),
        'replay_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'observation':observation,'assigned_controls':1,
        'network_competition_input_model_or_verifier_used':False,
        'repair_gain_or_private_scoring_equivalence_established':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--guard',type=Path,default=Path(__file__).with_name('source_validation_guard.py'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run(args.guard.resolve(strict=True))
    if args.output:
        with args.output.open('x',encoding='utf-8') as stream:stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

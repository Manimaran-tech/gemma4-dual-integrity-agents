"""Fresh eight-condition import/feedback experiment, without competition data.

Usage: python fresh_import_feedback_replay.py --guard source_import_guard.py
Requires Python 3.11+ and Git; creates an isolated local interpreter without
installing packages. The same assertion runs in every condition.
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

MODULE = 'fresh_feedback_control'
CHECK = '''import hashlib,importlib,json,pathlib
m=importlib.import_module("fresh_feedback_control")
p=pathlib.Path(m.__file__).resolve()
print("FRESH_FEEDBACK="+json.dumps({"origin":str(p),"version":m.__version__,
    "value":m.VALUE,"source_sha256":hashlib.sha256(p.read_bytes()).hexdigest()}))
assert m.VALUE == "after!"
'''


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def source(value):
    return f'__version__ = "0.0.1"\nVALUE = "{value}"\n'.encode()


def run_checked(args, **kwargs):
    return subprocess.run([str(a) for a in args], capture_output=True,
                          timeout=45, check=True, **kwargs)


def run(guard, plan=None):
    grid = list(itertools.product(('before', 'after!'), ('before', 'after!'),
                                  ('foreign', 'workspace')))
    if plan:
        frozen = json.loads(plan.read_bytes())
        if (frozen['guard_sha256'] != digest(guard.read_bytes())
                or frozen['driver_sha256'] != digest(Path(__file__).read_bytes())
                or frozen['assertion_sha256'] != digest(CHECK.encode())
                or frozen['conditions'] != [list(c) for c in grid]):
            raise ValueError('Frozen experiment identity changed')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1',
               PIP_NO_INDEX='1', PIP_DISABLE_PIP_VERSION_CHECK='1')
    env.pop('PYTHONPATH', None)
    observations = []
    with tempfile.TemporaryDirectory(prefix='fresh_import_feedback_') as temporary:
        root = Path(temporary)
        virtual = root / 'environment'
        run_checked([sys.executable, '-m', 'venv', '--without-pip', virtual], env=env)
        python = virtual / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        repo = root / 'checkout'
        package = repo / 'src' / MODULE
        package.mkdir(parents=True)
        local_file = package / '__init__.py'
        local_file.write_bytes(source('before'))
        run_checked(['git', 'init', '-q', repo])
        run_checked(['git', '-C', repo, 'add', '.'])
        run_checked(['git', '-C', repo, '-c', 'user.name=Feedback Control',
                     '-c', 'user.email=control@example.invalid',
                     'commit', '-qm', 'synthetic baseline'])
        foreign = root / 'foreign'
        foreign.mkdir()
        foreign_file = foreign / (MODULE + '.py')
        check_path = root / 'fixed_assertion.py'
        check_path.write_bytes(CHECK.encode())
        for checkout_value, foreign_value, selected in grid:
            local_file.write_bytes(source(checkout_value))
            foreign_file.write_bytes(source(foreign_value))
            selected_path = foreign if selected == 'foreign' else repo / 'src'
            condition_env = dict(env, PYTHONPATH=str(selected_path))
            before_diff = run_checked(['git', '-C', repo, 'diff', '--binary', 'HEAD']).stdout
            inspected = subprocess.run([str(python), str(guard), '--workspace', str(repo),
                '--module', MODULE], env=condition_env, capture_output=True, timeout=30)
            lines = [l for l in inspected.stdout.decode().splitlines()
                     if l.startswith('SOURCE_IMPORT_GUARD=')]
            if len(lines) != 1:
                raise ValueError('Missing unique native guard receipt')
            report = json.loads(lines[0].split('=', 1)[1])
            with tempfile.TemporaryDirectory(prefix='feedback_cache_') as cache:
                checked = subprocess.run([str(python), '-B', '-s', '-X',
                    'pycache_prefix=' + cache, str(check_path)], cwd=repo,
                    env=condition_env, capture_output=True, timeout=15)
            rows = [l for l in checked.stdout.decode().splitlines()
                    if l.startswith('FRESH_FEEDBACK=')]
            if len(rows) != 1:
                raise ValueError('Test process failed before its import inventory')
            actual = json.loads(rows[0].split('=', 1)[1])
            expected_file = foreign_file if selected == 'foreign' else local_file
            expected_value = foreign_value if selected == 'foreign' else checkout_value
            expected_exit = 0 if expected_value == 'after!' else 1
            checkout_passes = checkout_value == 'after!'
            after_diff = run_checked(['git', '-C', repo, 'diff', '--binary', 'HEAD']).stdout
            if (Path(actual['origin']) != expected_file.resolve()
                    or actual['source_sha256'] != digest(expected_file.read_bytes())
                    or actual['version'] != '0.0.1' or actual['value'] != expected_value
                    or checked.returncode != expected_exit
                    or report['success'] != (selected == 'workspace')
                    or inspected.returncode != (0 if selected == 'workspace' else 2)
                    or report['installation_attempted']
                    or not report['tracked_diff_unchanged'] or before_diff != after_diff
                    or check_path.read_bytes() != CHECK.encode()):
                raise ValueError('Origin, assertion, or unchanged-source control failed')
            observations.append(dict(checkout_value=checkout_value,
                foreign_value=foreign_value, imported_origin=selected,
                identical_version='0.0.1', test_exit_code=checked.returncode,
                expected_checkout_test_pass=checkout_passes,
                misleading_feedback=(checked.returncode == 0) != checkout_passes,
                false_accept=checked.returncode == 0 and not checkout_passes,
                false_reject=checked.returncode != 0 and checkout_passes,
                guard_accepts_provenance=report['success'],
                guard_status=report['status'], tracked_diff_unchanged_by_guard=True,
                imported_source_sha256=actual['source_sha256'],
                fixed_assertion_sha256=digest(CHECK.encode()),
                test_stderr_sha256=digest(checked.stderr)))
    return dict(created_utc=datetime.now(timezone.utc).isoformat(), status='completed',
        scope='Eight factorial conditions on one synthetic repository; not eight repair tasks',
        python_version=platform.python_version(), platform=platform.platform(),
        git_version=run_checked(['git', '--version']).stdout.decode().strip(),
        guard_sha256=digest(guard.read_bytes()),
        driver_sha256=digest(Path(__file__).read_bytes()),
        plan_sha256=digest(plan.read_bytes()) if plan else None,
        observations=observations, assigned_conditions=8, completed_conditions=len(observations),
        false_accept_conditions=sum(r['false_accept'] for r in observations),
        false_reject_conditions=sum(r['false_reject'] for r in observations),
        foreign_origins_rejected=sum(not r['guard_accepts_provenance'] for r in observations),
        all_same_assertion_version_and_interpreter=True,
        environment_installations=0, network_competition_data_model_or_verifier_used=False,
        model_repair_improvement_established=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--guard', type=Path, default=Path(__file__).with_name('source_import_guard.py'))
    parser.add_argument('--plan', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run(args.guard.resolve(strict=True), args.plan.resolve(strict=True) if args.plan else None)
    if args.output:
        with args.output.open('x', encoding='utf-8') as stream:
            stream.write(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

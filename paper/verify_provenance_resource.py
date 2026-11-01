"""Verify supplement bytes and run recorded or fresh reproducibility checks."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import shutil
import subprocess
import sys


def verify(root, fresh=False):
    manifest = json.loads((root / 'manifest.json').read_bytes())
    for row in manifest['files']:
        path = (root / row['path']).resolve(strict=True)
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError('Manifest member escapes supplement')
        raw = path.read_bytes()
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError('Manifest member changed: ' + row['path'])
    scripts = [('replay.py', 'recorded_scalars'),
               ('terminal_model_scalar_replay.py', 'recorded_scalars')]
    if fresh:
        if not shutil.which('git'):
            raise RuntimeError('Git missing; fresh controls have not executed')
        for name in ('pip', 'setuptools', 'wheel'):
            importlib.metadata.version(name)
        scripts += [('fresh_source_provenance_replay.py', 'fresh_three_layout_controls'),
                    ('fresh_source_path_replay.py', 'fresh_missing_backend_control'),
                    ('fresh_import_feedback_replay.py', 'fresh_eight_factorial_conditions')]
    results = []
    linux_path = root / 'fresh_import_feedback_linux_actual.json'
    if linux_path.exists():
        linux = json.loads(linux_path.read_bytes())
        expected = json.loads((root / 'fresh_import_feedback_expected.json').read_bytes())
        projected = [{k:r[k] for k in expected['observation_keys']} for r in linux['observations']]
        if linux['completed_conditions'] != 8 or projected != expected['observations']:
            raise ValueError('Recorded Linux factorial invariants differ from Windows')
        results.append(dict(script='fresh_import_feedback_linux_actual.json',
                            role='recorded_portability_invariant_comparison',exit_code=0,
                            output_sha256=hashlib.sha256(linux_path.read_bytes()).hexdigest()))
    for name, role in scripts:
        args = [sys.executable, str(root / name)]
        if name == 'fresh_import_feedback_replay.py':
            args += ['--plan', str(root / 'fresh_import_feedback_plan.json')]
        proc = subprocess.run(args, cwd=root, capture_output=True, text=True, timeout=180)
        if proc.returncode:
            raise RuntimeError('Reproduction failed: ' + name + '\n' + proc.stderr[-1500:])
        actual = json.loads(proc.stdout)
        if name == 'fresh_source_provenance_replay.py':
            expected = json.loads((root / 'fresh_expected.json').read_bytes())
            if actual['observations'] != expected['observations']:
                raise ValueError('Layout observations differ from recorded invariant expectations')
        if name == 'fresh_source_path_replay.py':
            expected = json.loads((root / 'fresh_source_path_expected.json').read_bytes())
            if actual['observation'] != expected['observation']:
                raise ValueError('Explicit environment observations differ from expectations')
        if name == 'fresh_import_feedback_replay.py':
            expected = json.loads((root / 'fresh_import_feedback_expected.json').read_bytes())
            projected = [{k: r[k] for k in expected['observation_keys']}
                         for r in actual['observations']]
            if projected != expected['observations']:
                raise ValueError('Factorial observations differ from frozen expectations')
        results.append(dict(script=name, role=role, exit_code=proc.returncode,
                            output_sha256=hashlib.sha256(proc.stdout.encode()).hexdigest()))
    return dict(created_utc=datetime.now(timezone.utc).isoformat(), status='completed',
                manifest_members_verified=len(manifest['files']), checks=results,
                fresh_experiments_executed=fresh,
                native_grader_or_model_rerun=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fresh', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = verify(Path(__file__).resolve().parent, args.fresh)
    if args.output:
        with args.output.open('x', encoding='utf-8') as stream:
            stream.write(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

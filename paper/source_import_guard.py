"""Budgeted, offline source provenance check executed by an agent skill.

This standalone file uses ordinary subprocesses inside the supplied sandbox.
It never imports or changes an evaluator, a reference patch, or test assertions.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], capture_output=True,
                          timeout=10, check=False)


def discover_workspace(explicit=None):
    if explicit and (str(explicit) != '/workspace' or Path(explicit).is_dir()):
        candidates = [Path(explicit)]
    else:
        candidates = [Path.cwd(), Path('/workspace'),
                      Path(tempfile.gettempdir()).parent / 'workspace']
        candidates.extend(Path(p) for p in os.environ.get('PYTHONPATH', '').split(os.pathsep) if p)
    roots = set()
    for candidate in candidates:
        if not candidate.is_dir():
            continue
        result = git(candidate, 'rev-parse', '--show-toplevel')
        if result.returncode == 0:
            roots.add(Path(result.stdout.decode().strip()).resolve(strict=True))
    if len(roots) != 1:
        raise ValueError('Cannot identify one Git workspace; pass --workspace')
    return roots.pop()


def source_location(root, module):
    if not re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*', module):
        raise ValueError('Expected an existing Python import name')
    parts = module.split('.')
    found = []
    for layout in (root, root / 'src'):
        package = layout.joinpath(*parts)
        for candidate in (package / '__init__.py', package.with_suffix('.py')):
            if candidate.is_file():
                resolved = candidate.resolve(strict=True)
                if not resolved.is_relative_to(root):
                    raise ValueError('Source symlink leaves workspace')
                found.append(resolved)
    if len(found) != 1:
        raise ValueError('Import must identify one source file in flat or src layout')
    return found[0]


def clean_env():
    env = dict(os.environ)
    env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1',
               PIP_NO_INDEX='1', PIP_DISABLE_PIP_VERSION_CHECK='1')
    return env


def inventory(root, module, expected):
    # A fresh cache prefix prevents old .pyc files from hiding rapid source edits.
    code = '''import importlib,json,sys
try:
 m=importlib.import_module(sys.argv[1]); origin=getattr(m,"__file__",None)
 result={"import_succeeded":True,"origin":origin,"version":str(getattr(m,"__version__",""))}
except Exception as e:
 result={"import_succeeded":False,"error_type":type(e).__name__,"error":str(e)[:500]}
result.update(executable=sys.executable,prefix=sys.prefix,base_prefix=sys.base_prefix)
print("SOURCE_IMPORT_INVENTORY="+json.dumps(result))
'''
    with tempfile.TemporaryDirectory(prefix='source_guard_cache_') as cache:
        proc = subprocess.run([sys.executable, '-B', '-s', '-X', 'pycache_prefix=' + cache,
                               '-c', code, module], cwd=root, env=clean_env(),
                              capture_output=True, timeout=15, check=False)
    lines = [line for line in proc.stdout.decode(errors='replace').splitlines()
             if line.startswith('SOURCE_IMPORT_INVENTORY=')]
    if proc.returncode != 0 or len(lines) != 1:
        raise ValueError('Fresh interpreter import inventory failed')
    result = json.loads(lines[0].split('=', 1)[1])
    origin = result.get('origin')
    result['imports_expected_source'] = bool(origin and Path(origin).resolve() == expected)
    result['isolated_venv'] = result['prefix'] != result['base_prefix']
    return result


def backend_available(root):
    backend = 'setuptools.build_meta'
    metadata = root / 'pyproject.toml'
    if metadata.is_file():
        import tomllib
        config = tomllib.loads(metadata.read_text(encoding='utf-8'))
        build = config.get('build-system', {})
        if build.get('backend-path'):
            raise ValueError('In-tree build backend requires manual review')
        backend = build.get('build-backend', backend).split(':', 1)[0]
    elif not (root / 'setup.py').is_file():
        raise ValueError('No declared editable project metadata')
    try:
        available = importlib.util.find_spec(backend) is not None
    except (ImportError, ValueError):
        available = False
    return backend, available


def generated_metadata(root):
    return {p.resolve() for base in (root, root / 'src') if base.is_dir()
            for p in base.glob('*.egg-info') if p.is_dir() and not p.is_symlink()}


def ensure_source(root, module, *, install=False, timeout=45):
    started = time.monotonic()
    expected = source_location(root, module)
    before_diff = git(root, 'diff', '--binary', 'HEAD')
    if before_diff.returncode:
        raise ValueError('Cannot inspect source diff')
    report = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'workspace': str(root), 'module': module, 'expected_source': str(expected),
              'scope': 'Agent-side import provenance, not repair correctness or grader equivalence',
              'network_or_dependency_resolution_enabled': False,
              'installation_attempted': False, 'before': inventory(root, module, expected)}
    if report['before']['imports_expected_source']:
        report.update(status='already_imports_source', after=report['before'])
    elif not install:
        report['status'] = 'source_not_imported'
    elif not report['before']['isolated_venv']:
        report['status'] = 'installation_refused_nonisolated_interpreter'
    else:
        backend, available = backend_available(root)
        report.update(build_backend=backend, build_backend_available=available)
        if not available:
            report['status'] = 'build_backend_unavailable_offline'
        else:
            existing = generated_metadata(root)
            command = [sys.executable, '-m', 'pip', 'install', '--no-index',
                       '--no-build-isolation', '--no-deps', '-e', str(root)]
            report.update(installation_attempted=True, installation_command=command)
            try:
                proc = subprocess.run(command, cwd=root, env=clean_env(), capture_output=True,
                                      timeout=timeout, check=False)
                report.update(pip_exit_code=proc.returncode,
                              pip_stdout_sha256=hashlib.sha256(proc.stdout).hexdigest(),
                              pip_stderr_sha256=hashlib.sha256(proc.stderr).hexdigest())
                if proc.returncode:
                    report['pip_error_tail'] = proc.stderr.decode(errors='replace')[-1200:]
                report['status'] = 'installation_failed' if proc.returncode else 'installed'
            except subprocess.TimeoutExpired:
                report['status'] = 'installation_timeout'
            # Remove only new build-generated metadata absent from tracked source.
            cleaned = []
            for path in generated_metadata(root) - existing:
                resolved = path.resolve(strict=True)
                if not resolved.is_relative_to(root) or resolved.suffix != '.egg-info':
                    raise ValueError('Generated metadata cleanup leaves workspace')
                tracked = git(root, 'ls-files', '--', path.relative_to(root).as_posix())
                if tracked.returncode != 0 or tracked.stdout:
                    continue
                shutil.rmtree(resolved)
                cleaned.append(path.relative_to(root).as_posix())
            report['new_generated_metadata_removed'] = sorted(cleaned)
            report['after'] = inventory(root, module, expected)
            if report['status'] == 'installed':
                report['status'] = ('source_import_verified' if report['after']['imports_expected_source']
                                    else 'installation_did_not_select_source')
    after_diff = git(root, 'diff', '--binary', 'HEAD')
    report['tracked_diff_unchanged'] = after_diff.returncode == 0 and after_diff.stdout == before_diff.stdout
    report['elapsed_seconds'] = round(time.monotonic() - started, 4)
    if not report['tracked_diff_unchanged']:
        report['status'] = 'setup_changed_tracked_source'
    report['success'] = (report['status'] in ('already_imports_source', 'source_import_verified')
                         and report['tracked_diff_unchanged'])
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path)
    parser.add_argument('--module', required=True)
    parser.add_argument('--ensure', action='store_true')
    parser.add_argument('--install-timeout', type=int, default=45, choices=range(1, 61))
    args = parser.parse_args(argv)
    try:
        root = discover_workspace(args.workspace)
        report = ensure_source(root, args.module, install=args.ensure, timeout=args.install_timeout)
    except Exception as error:
        report = {'status': 'environment_check_failed', 'success': False,
                  'error_type': type(error).__name__, 'error': str(error)[:700]}
    print('SOURCE_IMPORT_GUARD=' + json.dumps(report, sort_keys=True))
    return 0 if report['success'] else 2


if __name__ == '__main__':
    raise SystemExit(main())

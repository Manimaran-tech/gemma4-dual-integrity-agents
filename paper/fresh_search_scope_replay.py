"""Independent search-input controls using synthetic source and an installed rg."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile


def replay():
    executable = shutil.which('rg')
    if not executable:
        raise ValueError('An installed ripgrep executable is required')
    environment = dict(os.environ)
    configuration_override_removed = environment.pop('RIPGREP_CONFIG_PATH', None) is not None
    version = subprocess.run([executable, '--version'], capture_output=True, text=True,
                             timeout=15, env=environment, check=True).stdout.splitlines()[0]
    token = 'NEURAL_SWE_SCOPE_SENTINEL_e28ff29769a64ef5ba0d79238ab94719'
    with tempfile.TemporaryDirectory(prefix='fresh_search_scope_') as temporary:
        root = Path(temporary)
        source = root / 'src/demo.py'
        source.parent.mkdir()
        source.write_bytes((token + '\n').encode())
        before = hashlib.sha256(source.read_bytes()).hexdigest()
        base = [executable, '--no-ignore', '-n', '-F', '--', token]
        specifications = [
            ('empty_pipe_no_path', base, '', False),
            ('empty_pipe_explicit_dot', base + ['.'], '', False),
            ('empty_pipe_explicit_file', base + ['src/demo.py'], '', False),
            ('devnull_no_path', base, None, True),
            ('matching_pipe_no_path', base, token + '\n', False),
            ('absent_pattern_explicit_dot', [executable, '--no-ignore', '-n', '-F', '--',
                                           'NEURAL_SWE_GENUINELY_ABSENT_SCOPE_LITERAL', '.'], '', False),
        ]
        observations = []
        for name, command, incoming, devnull in specifications:
            options = dict(cwd=root, env=environment, capture_output=True, text=True, timeout=15)
            if devnull:
                options['stdin'] = subprocess.DEVNULL
            else:
                options['input'] = incoming
            actual = subprocess.run(command, **options)
            observations.append(dict(condition=name, exit_code=actual.returncode,
                stdout=actual.stdout, stderr=actual.stderr,
                input_mode='devnull' if devnull else 'explicit_pipe', input_bytes=0 if devnull else len(incoming.encode())))
        rows = {row['condition']: row for row in observations}
        for name in ('empty_pipe_no_path', 'absent_pattern_explicit_dot'):
            if rows[name]['exit_code'] != 1 or rows[name]['stdout']:
                raise ValueError('Empty-input/absent-literal control differs: ' + name)
        for name in ('empty_pipe_explicit_dot', 'empty_pipe_explicit_file', 'devnull_no_path'):
            if rows[name]['exit_code'] != 0 or token not in rows[name]['stdout']:
                raise ValueError('Source-search positive control differs: ' + name)
        if (rows['matching_pipe_no_path']['exit_code'] != 0
                or rows['matching_pipe_no_path']['stdout'].strip() != '1:' + token):
            raise ValueError('stdin-only matching control differs')
        after = hashlib.sha256(source.read_bytes()).hexdigest()
        if before != after:
            raise ValueError('Search control changed source')
    return dict(created_utc=datetime.now(timezone.utc).isoformat(), status='completed',
        scope='Fresh independent synthetic search-input controls; no Kaggle data, model, grader or repair',
        platform=platform.system(), ripgrep_version=version,
        executable_sha256=hashlib.sha256(Path(executable).read_bytes()).hexdigest(),
        explicit_empty_pipe_is_not_native_inherited_FD0_measurement=True,
        global_ignore_rules_disabled_in_all_conditions=True,
        RIPGREP_CONFIG_PATH_removed_in_all_conditions=configuration_override_removed,
        source_sha256=before, source_bytes_unchanged=True,
        assigned_controls=6, completed_controls=len(observations), observations=observations,
        model_repairs=None, model_accuracy_gain_established=False,
        hidden_scoring_equivalence_or_causality_established=False)


if __name__ == '__main__':
    print(json.dumps(replay(), indent=2))

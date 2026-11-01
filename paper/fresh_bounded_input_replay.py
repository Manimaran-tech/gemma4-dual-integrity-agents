"""Fresh synthetic retry controls; no repository, model, reference or repair."""
import hashlib
import json
import subprocess
import sys

CHILD = '''import json, sys
mode = sys.argv[1]
values = iter(['bad', '7'] if mode == 'finite' else ['bad'])
attempts = 0
while True:
    attempts += 1
    try:
        value = 'bad' if mode == 'constant' else next(values)
    except StopIteration:
        print(json.dumps(dict(stop='input_exhausted', assertion_verified=False)))
        raise SystemExit(3)
    try:
        result = int(value)
    except ValueError:
        continue
    assert result == 7
    print(json.dumps(dict(stop='assertion_completed', value=result, attempts=attempts,
                         assertion_verified=True)))
    break
'''


def replay():
    rows = []
    for mode in ('constant', 'finite', 'exhausted'):
        try:
            p = subprocess.run([sys.executable, '-B', '-c', CHILD, mode],
                capture_output=True, text=True, timeout=2)
            rows.append(dict(condition=mode, command_completed=True,
                timed_out=False, exit_code=p.returncode, observation=json.loads(p.stdout)))
        except subprocess.TimeoutExpired:
            rows.append(dict(condition=mode, command_completed=False,
                timed_out=True, exit_code=None, observation=None))
    expected = [
        dict(condition='constant', command_completed=False, timed_out=True,
             exit_code=None, observation=None),
        dict(condition='finite', command_completed=True, timed_out=False, exit_code=0,
             observation=dict(stop='assertion_completed', value=7, attempts=2, assertion_verified=True)),
        dict(condition='exhausted', command_completed=True, timed_out=False, exit_code=3,
             observation=dict(stop='input_exhausted', assertion_verified=False)),
    ]
    if rows != expected:
        raise ValueError('Fresh retry/termination invariants differ')
    return dict(scope='Fresh synthetic input/termination mechanism, not a library repair',
        controls=rows, child_sha256=hashlib.sha256(CHILD.encode()).hexdigest(),
        command_timeout_seconds=2, missing_observation_is_not_known_assertion_failure=True,
        model_inference_or_library_repair=False)


if __name__ == '__main__':
    print(json.dumps(replay(), indent=2))

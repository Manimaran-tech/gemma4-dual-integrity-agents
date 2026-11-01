# Native repository evaluation

The transport/grading code is implemented and checked locally. No native coding
episode, physical-phone result or comparative improvement is established yet.
Actual repository issues and already-running ordinary apps are required.

## Runtime and input boundary

Gemma 4 E2B uses native LiteRT-LM on CPU with two threads. The repository harness
lists, reads, searches, edits, writes and deletes bounded source files. It rejects
host-inference fallback and protects grading paths. It supplies no device Python
interpreter, shell tool or native test runner. A changed-file export becomes an
unchanged Git patch on the host and is graded separately by the organizer verifier.
This is native generation with host grading, not a fully native development stack.

The memory controller admits/releases a whole engine. It does not implement
weight-block paging, GPU-VRAM borrowing, NPU allocation or persistent KV restoration.
A closed handle supplies no unmeasured physical RAM credit.

The prepared Rich development input is
`benchmarks/competition/mobile_inputs/20261004_rich_3067_dev_v2/`: 524 genuine files,
19,416,123 source bytes at the declared GitHub commit, including the MIT license.
Preparation is not inference or success. The failed first preparation is retained.
Android receives only ID, repository, base commit, problem, hints and source.
New grader tests/reference fixes remain evaluator-only. The public pool is already
exposed to the research assistant; all current retests are development work.
Confirmatory evaluation needs independently withheld assignments and audited inputs.

## Prospective execution

Keep the chosen real app open with an actual workload, for example Luanti with its
world running. The runner never launches a replacement app. Record its activity;
installed-package presence does not prove a heavy workload. Native E2B must already
be installed. Build sources/APKs together and explicitly select an ADB serial.

```powershell
& 'C:\Program Files\Python311\python.exe' scripts/build_native_checks.py --with-unit-tests --gradle-heap-mib 1024 --single-worker
& 'C:\Program Files\Python311\python.exe' scripts/run_native_repository_episode.py --serial emulator-5554 --prepared benchmarks/competition/mobile_inputs/20261004_rich_3067_dev_v2 --foreground-package net.minetest.minetest --mode OBSERVE_ONLY --deadline-seconds 600
```

These commands are examples, not recorded device runs. Physical S24 FE measurements
use its observed serial and form a separate stratum. ADB currently has no device.
Every assigned episode is stored under `benchmarks/real_world/native_repository/`
with a fresh ID, inputs/build hashes, observed hardware/app versions, staging hashes,
instrumentation output, model/tool journals, sampled memory, foreground package,
stage-journal boundaries and actual exports. Failed preflights remain assigned;
they do not become model failures. Kills/exceptions preserve available journals and
partial changes. Missing evidence stays unknown.

If a killed process has no declared export, the runner stops only our inference
package before collecting its actual working tree as a tar archive. Recovery
requires the native receipt proving that the complete assigned source was imported;
an unfinished import cannot be interpreted as deleted source. The original tar,
receipt, inventory, reconstructed patch and recovery provenance are retained.
Links and changes to protected grading files are rejected. This path can preserve
edits for independent grading, but never establishes generation completion,
inference success or a met deadline. Its transport checks pass on synthetic files;
on-device interruption recovery has not yet been exercised.

The cold boot recorded in `hardware_conditions/20261004T071834176325` reached
Android 17 with the existing 8-GiB configuration and hardware graphics. Windows
available physical memory then fell to about 89 MiB at one observation, so the
owned emulator was stopped before any repository inference. The launcher was
observed before the user's world-open confirmation arrived. This is a host-capacity
setup observation, not an assigned repository task or predictor failure. The
physical phone remains unmeasured; emulator execution is currently limited by host
headroom. These example commands therefore remain prospective.

Sampling begins after foreground validation and includes source import/generation;
shutdown is excluded from memory sampling. The 250-ms delay follows observation
and journal writes, so actual gaps need analysis. Journal I/O is included in timing.
Foreground presence is not input latency or frame quality. The generation deadline
includes import and generation/export; episode duration also includes shutdown.
A full workflow deadline including transport, queueing and grading is unverified.

## Independent grading

Freeze a request from a recovered episode using
`scripts/prepare_mobile_grade_request.py --episode <actual-episode-directory>`.
The request binds assignment, episode and unchanged reconstructed patch; it cannot
create an empirical episode. Use `kaggle/09_mobile_patch_validation.ipynb`,
Accelerator None, Internet off, original organizer environment, official data and
wheelhouse, genuine supplemental dependencies and that actual episode input.
The notebook loads no model and establishes no 31B leaderboard score.

Clean-base, candidate and reference conditions use fresh official verification
workspaces and the same 300-second limit. Core versions and verifier source are
bound to the previously observed genuine CPU fixture run. Preserve setup failures
and all raw outcomes. A passing clean base cannot demonstrate repair. Reference
controls never count as generated fixes. Supplemental dependency compatibility
does not establish private-grader equivalence. Official snapshot/device input-tree
equivalence is also not assumed from a matching commit label alone.

## Predictor comparisons

Collect new `OBSERVE_ONLY` fitting episodes, then freeze complete real stage
journals with `scripts/freeze_native_repository_seed.py`. Failures and interrupted
stages stay in the seed. Its manifest binds device fingerprint, app version,
code/runtime settings and fitting issue IDs. Exclude fitting issues from evaluation.
Old 2,048-context/128-output pilot profiles do not calibrate this 4,096-maximum-
context/512-requested-output path. Actual request settings may be smaller and
are recorded by the native stage observer.

Both `BUDGET_REACTIVE` and `PREDICTIVE` require the same frozen seed/manifest through
`--profile-seed` and `--profile-manifest`. They share the pressure guard, reactive
idle policy, 800-MiB reserve, conservative deadline rule, bracketed resident
configuration and zero forecast soft-excess allowance. Their declared admission
difference is whether the forecast gates a request. Frozen history now also blocks
release-delay learning. No release-delay seed or statistical coverage is supplied.

Unknown budget getters remain unknown. Strict prediction defers if required
process/UID budget evidence is unavailable; it is not validated for every 8-GB
phone. Reactive native compatibility needs actual measurements too. A stage seed
is an empirical fitting artifact, not independent conformal calibration.

Before comparison, freeze assignments, session order/repetitions, shared limits,
initial residency/thermal conditions, app workload and real foreground QoS
measurement. Preserve every assignment. Request completion cannot establish
coding correctness or superiority. The old six-response comparison keeps its
different 128-MiB predictive allowance and remains inconclusive.

## Publication gaps

Real native coding episodes with independent grades; matched policy conditions;
actual foreground interaction/frame quality; physical S24 FE measurements;
temperature/energy and telemetry overhead; live multimodal task semantics;
exposure-audited confirmatory assignments; and executable, hash-bound analysis
remain required. The current paper also lacks a successful built-in PDF compilation.

Research draft, October 8, 2026. Final Paper Track submission remains pending.

## Abstract

A repair check can pass while importing an installed library instead of the
edited checkout. We investigate this failure in the Gemma 4 development harness,
separating environment qualification, agent validation and model repairs. Eight
pretest inventories on four assigned Requests cases import host source; none of
the four clean-base/reference pairs qualifies. Genuine offline editable
installation changes all eight imports to workspace source and restores four
qualifying pairs under unchanged assertions. An allowed sandbox skill conditionally
checks source provenance. Forty synthetic native-agent loops on ten cases verify
edited source in six cases without intervention, nine with conditional installation
and ten with an explicitly applied validation environment. Independent fresh
controls reproduce the mechanism without competition data. An eight-condition
experiment holds the assertion, interpreter and version fixed: foreign imports
produce both false acceptance of an unfixed checkout and false rejection of a
correct edit. The guard rejects all four foreign origins. Two additional native
controls show content searches reading inherited input instead of known source;
explicit paths restore matches without edits. These results support
reproducible validation controls, not improved Gemma repair accuracy or equivalence
to the private scorer.

## Introduction

A failing repair test is useful only when it exercises the intended implementation
and represents the reported behavior. Import failures, stale bytecode and foreign
installations break different parts of that contract. More inference time alone
cannot establish which source was exercised.

The [Gemma 4 Developer Agent competition](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview)
requires `gemma-4-31b-it-qat-w4a16-ct` for model-backed agents. Its global patch
generation budget is twelve hours including setup, with patch validation excluded.
The [official starter](https://www.kaggle.com/code/ryanholbrook/getting-started-gemma-4-developer-agent)
provides a development harness and public tasks. We use that development setting
to study validation provenance, while retaining separate model and grader outcomes.
Our diagnosis concerns the local subprocess backend, not a demonstrated defect in
the private scoring infrastructure.

Editable installation is established. We contribute source-bound empirical
diagnosis, budgeted agent-side integration and executable controls exposing both
directions of misleading feedback.

## Methods and experimental boundaries

We distinguish four outcomes: fixture qualification, source import provenance,
source-edit visibility and verified model repair. A qualified fixture has a
nonpassing clean base and a passing official reference under the same verifier.
Qualification does not count as an agent repair. An import-origin success does
not prove that an assertion tests the issue. A synthetic source marker is a
mechanism control, not a solved repair task.

Plans bind task identities, inputs, source hashes, packages, dependencies,
condition order and notebook cells before execution.
Agent inputs contain only instance ID, repository, base commit, problem statement
and hints. Reference patches and private validation remain inside independent
CPU verifier controls; they are excluded from the agent and public supplement.
The public pool has prior research-assistant reference exposure. These experiments
are development studies and are not described as untouched holdouts.

Organizer packages and verifier source remain fixed. Supplemental dependencies
are prospectively declared; assertions, protected tests and production fixes
remain unchanged. Verifier SHA256 is
`98600fd6066a4dbd472490cb194b839a3a633afea9b99256cc081ea77beac0d3`.
Native integration checks all one hundred organizer Python sources. Executed
cells, chronological transports, archive members and downloaded output reconcile.
Hashes establish byte identity, not independent authentication of claims.

### Repeated Requests controls

A metadata-ranked twelve-case panel originally assigns four cases each from
Requests, FastAPI and Rich. Six FastAPI/Rich cases qualify; none of the four
Requests cases does. We retain those classifications and select no replacement
Requests case after observing failure. The following repeated diagnosis uses all
four original Requests cases, in their original order.

Eight pretest inventories in the native subprocess verifier reveal host
Requests 2.32.4 with the same imported-module hash across cases and reference
conditions. The backend includes the workspace root in PYTHONPATH while these
checkouts use `src/requests`, and skips editable project installation. The
observed import therefore does not reach the edited module. In a separate
intervention, each isolated environment receives a genuine editable installation
of its workspace project with `--no-index --no-build-isolation --no-deps`.
The original verifier command is then forwarded unchanged. A second control
applies the same installation earlier, after the source-bound Git-exclude setup
and before baseline creation or reference/test-patch application.

These verifier interventions use a declared local setup observer. They are not
part of a submitted agent. We report them separately from the allowed agent-side
skill to avoid confusing evaluator setup with submission capability.

### Interpreting validation feedback

Before treating a test outcome as patch evidence, record the interpreter,
working directory, resolved target module, source hash and explicit environment.
Check that the same assertion fails on the intended unedited source and passes
after the proposed edit. Source identity and edit sensitivity establish different
properties; neither proves issue relevance or absence of regressions. The guard
checks the first property. We evaluate the second with fixed synthetic assertions
and separately qualify real fixtures with the native verifier.

### Conditional agent-side guard

The standalone helper accepts an existing flat/src Python import name, discovers
one Git workspace and checks its resolved module file in a fresh process using
the skill interpreter. Separate bytecode-cache prefixes prevent rapid edits from
being hidden by a repository cache. Correct imports skip installation. Otherwise,
only an isolated environment with the declared backend may install the workspace
project, with no network, dependency resolution or build isolation, bounded to 45
seconds. It rechecks origin, removes only newly generated untracked egg-info and
confirms the tracked diff is unchanged. Missing backends, import exceptions,
nonisolated interpreters and persistent shadowing remain failures. It accesses
no reference solution and changes no evaluator or manager.

V14/v15 retain the required 31B model, nine tools, sampling and limits
(three minutes, fifty tools, one hundred turns, 300-second command timeout).
Origin-check instructions and a graph-key correction are bundled, not causally
isolated. V15 adds an explicit source-only validation environment for missing
backends or nonisolated installation; default imports remain unchanged.

The native panel freezes three cases each from Requests, FastAPI and Rich,
plus the sole public HTTPX case. A fixed salted SHA256 ranks IDs, not outcomes;
HTTPX's prior exposure is recorded. V14 pairs fresh sandboxes and predetermined
transport, varying only `--ensure`. V15 preserves cases, order and budget while
applying its returned environment. No repository-level generalization estimate
is established.

The original runner, compiler and budgeted skill executor use predetermined
replies without model weights. Each loop checks an inert source marker in a fresh
process, restores identical bytes and submits an empty patch with two charged
tools. Infrastructure failures stop execution; negative observations remain
assigned. Synthetic loops never count as repairs.

### Independent fresh experiment

The supplement includes a standard-library driver requiring Python 3.11+, Git
and locally installed pip, setuptools and wheel. It creates disposable Git
repositories and an isolated environment. Flat and src packages contain the
same tiny implementation. An identical assertion fails before a same-length
source edit and passes afterward, using fresh processes and separate cache
prefixes. A third control prepends a foreign module through PYTHONPATH; the guard
must report unsuccessful provenance even after installation. This protocol uses
no Kaggle data, evaluator, model or reference patch.

A second, prospectively frozen fresh experiment crosses checkout state
(buggy/corrected), foreign-copy state (buggy/corrected) and selected import origin
(workspace/foreign). All eight conditions use one disposable src repository,
one isolated interpreter, one byte-identical assertion and version `0.0.1` in
both copies. Each test process records its actual module path and file hash
before asserting the same expected value. Separate fresh cache prefixes prevent
stale bytecode from concealing the controlled edits. Inspect-only guard calls
must agree with actual test-process origin and preserve the tracked diff.
No package is installed. These are eight factorial conditions, not eight tasks.

## Results

All twenty-four verifier executions complete across three setup
conditions on the same four Requests cases. The unchanged setup imports host
source in all eight checks. Three pairs fail to verify their reference; the
remaining pair already passes at baseline. All sixteen installation-condition
checks import workspace source. Both installation points yield four failing
clean bases and four passing references. These are repeated controls on four
cases, not twelve independent repair successes.

| Setup condition | Workspace imports / checks | Qualified pairs / cases |
| --- | ---: | ---: |
| Unchanged native subprocess setup | 0 / 8 | 0 / 4 |
| Editable installation immediately before native pytest | 8 / 8 | 4 / 4 |
| Editable installation before native baseline and patch application | 8 / 8 | 4 / 4 |

[Figure 1 and its source data](https://www.kaggle.com/datasets/manimaran2308/requests-source-provenance-replay-v1)

Figure 1 retains the native fixture-qualification denominators. Earlier synthetic
agent/Evaluator controls reproduce the Requests import contrast with empty
patches and nonpassing clean-base grades. Neither establishes a model's ability
to choose or benefit from the intervention.

The fresh independent replay completes all three controls on Windows Python
3.12.14. Flat imports already read source and skip installation; src imports
change from missing to workspace source after one offline install. The fixed
assertion changes from exit 1 to exit 0 after the controlled source edit in both
layouts. Repeat setup skips installation. The foreign-PYTHONPATH control remains
unsuccessful and is correctly rejected. Repeating the experiment from the
extracted supplement reproduces these outcomes. 

The twenty-control cross-repository native integration panel completes and
reconciles. Inspect-only setup reads edited source in six of ten cases: all
FastAPI/Rich cases. Conditional installation raises source-import verification
and marker visibility to nine of ten, with exactly three Requests installs.
The HTTPX case remains negative because `hatchling.build` is absent offline.
An initial execution stops before controls because its manifest omits a shared
verifier hash. The retained execution-only amendment adds that exact hash and
preserves cases, condition order, source bytes and limits.

An explicit source-path extension now repeats the same fixed panel. When the
backend is absent, it can verify a source-only PYTHONPATH for a validation command,
without installing a backend or changing default imports. The returned prefix
must be used for every subsequent check. A fresh independent missing-backend
control verifies this distinction: the fixed assertion changes from failing to
passing after a source edit with the explicit environment, and still fails
when that environment is omitted. The second twenty-loop native panel completes
and reconciles: inspect-only verification remains six of ten, while conditional
verification and source-edit visibility reach ten of ten. Three Requests cases
install, six FastAPI/Rich cases skip installation and the single HTTPX case uses
the explicit validation environment. All forty loops preserve empty patches,
five predetermined replies and two charged tools per loop. The installation
guard takes approximately five seconds on Requests; this timing excludes the
extension's additional import inventory and is not total task cost.

| Native condition | Source verified / cases | Source edits visible / cases |
| --- | ---: | ---: |
| Inspect only, in each repetition | 6 / 10 | 6 / 10 |
| Conditional editable installation | 9 / 10 | 9 / 10 |
| Conditional installation plus explicit validation environment | 10 / 10 | 10 / 10 |

Figure 2 in the supplement shows the same denominators by repository. These
are paired mechanism checks on ten distinct cases, not forty independent tasks
or a model repair rate.

The new factorial experiment completes all eight conditions on Windows Python
3.12.14. The identical frozen code and plan repeat on Kaggle Linux Python 3.13.15,
matching all eight invariant observations. The supplement preserves that Linux execution and its source reconciliation;
it uses no competition input or model. These are repeated conditions on the
same synthetic design; the installation experiments are not repeated on Linux.
When the intended checkout is imported, the same assertion fails before
the edit and passes afterward, regardless of the foreign copy. A foreign corrected
copy makes the buggy checkout appear to pass; a foreign buggy copy makes the
corrected checkout appear to fail. Both copies report the same version. The
guard accepts all four workspace origins and rejects all four foreign origins,
including conditions whose verdict happens to match the checkout. No tracked
source changes during the guard calls.

| Intended checkout | Foreign copy imported | Observed assertion | Interpretation |
| --- | --- | --- | --- |
| Buggy | Buggy | Fails | Coincidentally correct feedback |
| Buggy | Corrected | Passes | False acceptance |
| Corrected | Buggy | Fails | False rejection |
| Corrected | Corrected | Passes | Coincidentally correct feedback |

Figure 3 in the supplement provides the full eight-cell contrast and source data.
This deterministic construction demonstrates a mechanism, not its prevalence in
real repositories. Version matching and a passing test are insufficient evidence
of checkout validation. Provenance success alone remains insufficient evidence
of a successful repair.

## Terminal model studies and protocol uptake

Seven terminal studies retain all 84 slots: 73 executions complete and 11 are
unattempted. The first six repeat one exposed six-case panel; the seventh uses
a separate six-case panel. Source, packages, traces, patches, grades and transports
reconcile. These are repeated development studies, not independent samples or
untouched holdouts.

| Comparison, first / second arm | Executions / assigned | Complete execution pairs | Pairs with both verifiers known | Verified successes, first / second |
| --- | ---: | ---: | ---: | --- |
| Shell / tool-rich | 12/12 | 6 | 4 | 1/6 / 2/6 |
| Shell / evidence workflow | 7/12 | 3 | 3 | 0/3 / 0/4 |
| Three / five minutes | 7/12 | 3 | 0 | 0/3 / 0/4 |
| Source-validation / focused prompt | 12/12 | 6 | 2 | 2/6 / 2/6 |
| Source-validation / structured interface | 12/12 | 6 | 1 | 2/6 / 1/6 |
| Source-validation / flat single interface | 11/12 | 5 | 1 | 2/5 / 1/6 |
| Source-validation / hypothesis pipeline, additional panel | 12/12 | 6 | 1 | 1/6 / 2/6 |

Success denominators include completed executions with unknown verifiers, not
complete known-outcome accuracy estimates. Minus-one grades remain unknown;
unattempted slots have no observed outcome. The supplement recomputes every
assigned denominator; an unavailable verifier is not a known test failure.

Tool-rich/shell has one tool-rich-only and one shared success; two pairs have an
unavailable verifier. One discordant pair cannot establish superiority.
Evidence-workflow and budget studies stop on protected-test conflicts, each
retaining five unattempted slots. More time alone yields no verified repair here.
The focused prompt calls no get_status, run_skill_script or submit_patch. Its two
verified production fixes equal the parent's while adding disposable scripts.
Native timeout fallback captures patches; missing submit calls do not prove absence.

V19 bundles navigation, edits, source assertions and completion in a changed
prompt/tool/skill interface. Required model, sampling and three-minute budgets
match v15, but verified repairs fall from two to one. Nine verifiers remain
unknown; five candidate patches are empty. Six of 41 skill calls receive argument
rejection, with one unclassified response. V20's flat arguments also pass prior
synthetic integration, but its 84 skill calls spend 46 calls reading. Twelve reads
exceed the line limit; registration, command-shape, path and replacement errors
remain. Edits occur at 125 and 137 seconds, with no source assertion or submit call.
Five candidate patches are empty; a removed-tool error leaves the last parent
slot unattempted. Neither interface measures candidate-only repair gain.

Salted metadata ranking assigns eight additional exposed cases, excluding prior
IDs. All 16 clean/reference controls complete: four FastAPI and two Rich qualify.
One Rich reference remains unverified; the last clean base times out at exit 124
despite a passing reference. Neither is replaced. All six qualified cases enter
the seventh study. Its native hypothesis planner and writer share the parent's
three-minute budget. Both arms repair one Rich case with an identical 503-byte
production patch. The pipeline also produces a verified 512-byte FastAPI repair
against an empty parent timeout. Nine verifier outcomes remain unknown, and only
the shared-success pair has both outcomes known. This is a delivery advantage
on one exposed case, not established statistical or hidden-score superiority.
No protected-test conflict occurs.

### Search-input provenance

Empty pathless searches in the seventh study motivate a separate CPU diagnostic.
The original subprocess backend inherits descriptor zero. In two fixed native
cases it is an empty FIFO: ripgrep 13.0.0 returns exit 1 with no matches when no
path is supplied, although the unchanged source contains the literal. Explicit
directory/file searches recover matches. Empty-pipe, matching-pipe, null-input
and genuinely absent-literal controls distinguish input selection from source
absence. Twenty-four charged commands run under original compilation; synthetic
replies submit empty patches. No model weights, repair grader or source edit is used.

Six fresh standalone controls reproduce this contrast with synthetic source and
ripgrep 15.2.0. Ignore filtering is disabled uniformly in these fresh controls.
[Upstream ripgrep input selection](https://github.com/BurntSushi/ripgrep/blob/master/crates/core/flags/hiargs.rs)
documents the existing stdin heuristic; this is not a newly discovered ripgrep
defect. The native development reproduction does not capture the GPU study's
descriptor zero or prove the cause of its timeouts or official 0.08 score.
V22 changes only writer instructions to require explicit search paths. Its exact
package passes two repeated native checks; these are package validation, not new
independent mechanism cases or repairs. Its model comparison remains pending
and contributes no outcomes here.

## Related work

[SWE-agent](https://arxiv.org/abs/2405.15793) studies the agent–computer interface;
[Agentless](https://arxiv.org/abs/2407.01489) organizes repair around localization,
patch generation and validation. [EnvBench](https://arxiv.org/abs/2503.14443)
treats environment setup as a distinct evaluation problem, while
[SWT-Bench](https://arxiv.org/abs/2406.12952) studies issue reproduction and tests
as filters for repairs. These motivate explicit environment and feedback checks.
[pytest documentation](https://docs.pytest.org/en/stable/explanation/pythonpath.html)
also explains how import paths can select an installed or local package.
Their results do not predict Gemma 4 performance. We contribute source-bound
provenance diagnosis, unchanged-assertion controls and reproducible feedback checks.

## Reproducibility and limitations

The version10 supplement ships 51 files, including a byte manifest, native/model
and protocol scalars, qualification outcomes, four fresh drivers and PNG/SVG figures.
Run `python verify_provenance_resource.py --fresh` to verify files, recompute recorded
analyses, compare Linux invariants and execute fresh controls. All eleven checks
pass on the downloaded resource: seven recorded checks and four fresh drivers.
Scalar replay does not rerun or independently authenticate native grading or
inference. Fresh experiments require Python 3.11+, Git, local build tools and ripgrep.
Missing prerequisites stop execution; no dependencies are downloaded. Invariant
observations are compared exactly across runtime versions and temporary paths.
Authored code is MIT licensed; data and figures use CC BY 4.0.

The Requests sample is small and exposed. Cross-repository native integration
uses synthetic replies; the factorial experiment tests a constructed mechanism,
not its real-world prevalence. Flat/src Python files are supported; namespace
packages, compiled extensions and multiple target files need additional coverage.
A passing origin check proves neither issue relevance nor repair correctness.
Subsequent tests must use the verified interpreter/environment. Pytest import
modes, plugins and workers can change resolution after preflight; the guard does
not instrument every module inside actual tests.

Private-scoring equivalence, the full twelve-hour schedule and improved Gemma
repair accuracy remain unverified. The current official main score is 0.08.
The standalone fresh protocols test the provenance mechanism beyond competition data.

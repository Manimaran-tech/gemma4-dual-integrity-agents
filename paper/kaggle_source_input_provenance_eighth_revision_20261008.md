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
explicit paths restore matches without edits. Eight terminal model studies have
not established improved repair accuracy. These results support reproducible
validation controls, without establishing private-scoring equivalence.

## Introduction

A failing repair test is useful only when it exercises the intended implementation
and represents the reported behavior. Import failures, stale bytecode and foreign
installations break different parts of that contract. More inference time alone
cannot establish which source was exercised.

The [Gemma 4 Developer Agent competition](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview)
requires `gemma-4-31b-it-qat-w4a16-ct`. Patch generation has twelve hours including
setup, excluding validation. The [official starter](https://www.kaggle.com/code/ryanholbrook/getting-started-gemma-4-developer-agent)
provides the public development harness. We diagnose its local subprocess backend;
private-scoring equivalence remains unverified.

Editable installation is established. We contribute source-bound diagnosis,
budgeted integration and executable controls exposing both directions of
misleading feedback.

## Methods and experimental boundaries

Fixture qualification, import provenance, source-edit visibility and model repair
are separate outcomes. Qualification requires a nonpassing clean base and passing
official reference under one verifier; it is not an agent repair. Correct origin
does not establish assertion relevance. Synthetic markers are mechanism controls,
not solved tasks.

Plans bind tasks, inputs, source/package hashes, dependencies, order and notebook
cells before execution. Agents receive instance ID, repository, base commit,
problem and hints. Reference patches and private validation stay in independent
CPU controls, excluded from agents and the public supplement. Prior research
reference exposure prevents describing this public pool as untouched holdouts.

Organizer source, assertions and protected tests remain fixed. Supplemental
dependencies are prospectively declared. Native integration checks all one
hundred organizer Python sources; executed cells, transports, archive members
and downloaded output reconcile. Hashes establish byte identity, not independent
authentication of claims.

### Repeated Requests controls

A metadata-ranked twelve-case panel originally assigns four cases each from
Requests, FastAPI and Rich. Six FastAPI/Rich cases qualify; none of the four
Requests cases does. We retain those classifications and select no replacement
Requests case after observing failure. The following repeated diagnosis uses all
four original Requests cases, in their original order.

Eight pretest inventories reveal host Requests 2.32.4 with identical imported-module
hashes across cases and reference conditions. The backend adds the workspace root
to PYTHONPATH, although these checkouts use `src/requests`, and skips editable
installation. Each isolated intervention installs its workspace with
`--no-index --no-build-isolation --no-deps`, then forwards the unchanged verifier.
The second intervention installs after the source-bound Git-exclude setup,
before baseline creation and reference/test-patch application.

These verifier interventions use a declared local setup observer. They are not
part of a submitted agent. We report them separately from the allowed agent-side
skill to avoid confusing evaluator setup with submission capability.

### Interpreting validation feedback

Before interpreting tests, record interpreter, working directory, resolved module,
source hash and explicit environment. Check that one assertion fails on the
intended unedited source and passes after editing. The guard checks source
identity; fixed synthetic assertions test edit sensitivity, while native clean/reference
controls qualify real fixtures. Neither establishes issue relevance or regression safety.

### Conditional agent-side guard

The helper discovers one Git workspace and checks an existing flat/src import in
a fresh skill-interpreter process with a separate bytecode cache. Correct origins
skip installation. Otherwise, an isolated environment with the declared backend
may install offline, without dependencies or build isolation, within 45 seconds.
It rechecks origin, removes only newly generated untracked egg-info and verifies
an unchanged tracked diff. Missing backends, import exceptions, nonisolated
interpreters and persistent shadowing remain failures. It uses no reference and
changes no evaluator or manager.

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

A standard-library driver creates disposable Git repositories and an isolated
environment with local build tools. Flat/src packages share one implementation.
An identical assertion fails before a same-length edit and passes afterward,
using fresh processes and separate bytecode caches. A foreign PYTHONPATH control
must fail provenance even after installation. No Kaggle data, evaluator, model
or reference patch is used.

A second frozen experiment crosses checkout state (buggy/corrected), foreign-copy
state (buggy/corrected) and import origin (workspace/foreign). All eight conditions
share one disposable src repository, interpreter, byte-identical assertion and
version 0.0.1. Each process records actual module path/hash before asserting.
Separate caches prevent stale-bytecode effects. Inspect-only guards must match
test-process origins and preserve tracked diffs. No installation occurs; these
are factorial conditions, not eight tasks.

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

The twenty-control native integration panel reconciles: inspect-only setup sees
edited source in six of ten cases; conditional installation reaches nine with
three Requests installs. HTTPX remains negative because `hatchling.build` is absent
offline. An initial manifest failure stops execution before controls. The retained
execution-only amendment adds the omitted verifier hash, preserving cases,
order, source bytes and limits.

A source-path extension repeats the panel, applying a verified source-only
PYTHONPATH when installation is unavailable. A fresh missing-backend control sees
the assertion fail before editing and pass afterward with that environment;
default imports remain failing. The second twenty-loop panel reaches ten of ten:
three Requests installs, six FastAPI/Rich skips and one HTTPX explicit environment.
All forty loops retain empty patches, five predetermined replies and two charged
tools. Approximately five-second Requests install timing excludes inventories
and total task cost.

| Native condition | Source verified / cases | Source edits visible / cases |
| --- | ---: | ---: |
| Inspect only, in each repetition | 6 / 10 | 6 / 10 |
| Conditional editable installation | 9 / 10 | 9 / 10 |
| Conditional installation plus explicit validation environment | 10 / 10 | 10 / 10 |

Figure 2 in the supplement shows the same denominators by repository. These
are paired mechanism checks on ten distinct cases, not forty independent tasks
or a model repair rate.

All eight factorial conditions complete on Windows Python 3.12.14. The identical
frozen code and plan repeat on Kaggle Linux Python 3.13.15, matching every invariant.
The supplement retains Linux execution and source reconciliation. Installation
experiments are not repeated on Linux. Intended-checkout imports make the assertion
fail before editing and pass afterward, regardless of the foreign copy. A foreign
corrected copy falsely passes the buggy checkout; a foreign buggy copy falsely
fails the corrected checkout. Both report the same version. The guard accepts all
four workspace origins and rejects all four foreign origins, including coincidentally
correct verdicts, without tracked source changes. These are repeated synthetic
conditions, not eight independent tasks.

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

Eight terminal studies retain all 96 slots: 85 executions complete and 11 are
unattempted. The first six reuse one exposed six-case panel; the last two reuse
a separate panel. Source, packages, traces, patches, grades and transports reconcile.
These are repeated development studies, not independent samples or untouched holdouts.

| Comparison, first / second arm | Executions / assigned | Complete execution pairs | Pairs with both verifiers known | Verified successes, first / second |
| --- | ---: | ---: | ---: | --- |
| Shell / tool-rich | 12/12 | 6 | 4 | 1/6 / 2/6 |
| Shell / evidence workflow | 7/12 | 3 | 3 | 0/3 / 0/4 |
| Three / five minutes | 7/12 | 3 | 0 | 0/3 / 0/4 |
| Source-validation / focused prompt | 12/12 | 6 | 2 | 2/6 / 2/6 |
| Source-validation / structured interface | 12/12 | 6 | 1 | 2/6 / 1/6 |
| Source-validation / flat single interface | 11/12 | 5 | 1 | 2/5 / 1/6 |
| Source-validation / hypothesis pipeline, additional panel | 12/12 | 6 | 1 | 1/6 / 2/6 |
| Hypothesis pipeline / explicit search, same additional panel | 12/12 | 6 | 1 | 2/6 / 1/6 |

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

V19 changes the prompt/tool/skill interface while preserving model, sampling and
three-minute budgets. Repairs fall from two to one; nine grades remain unknown
and five candidate patches are empty. Six of 41 skill calls reject arguments,
with one unclassified response. V20 passes synthetic integration but spends 46
of 84 skill calls reading; twelve exceed line limits. Registration, command-shape,
path and replacement errors remain. Edits occur at 125 and 137 seconds, without
source assertions or submit calls. Five candidate patches are empty; a removed-tool
error leaves the last parent slot unattempted. Neither interface establishes gain.

Salted metadata ranking assigns eight additional exposed cases, excluding prior
IDs. All 16 clean/reference controls complete: four FastAPI and two Rich qualify.
One Rich reference remains unverified; another clean base times out at exit 124
despite a passing reference. Neither is replaced. All six qualified cases enter
the seventh study under the parent's shared three-minute budget. Both arms deliver
an identical verified 503-byte Rich patch; the pipeline adds a verified 512-byte
FastAPI repair against an empty parent timeout. Nine verifiers remain unknown;
only the shared-success pair has both known. This single delivery advantage does
not establish statistical or hidden-score superiority. No protected-test conflict occurs.

### Search-input provenance

Empty pathless searches in the seventh study motivate a separate CPU diagnostic.
The original subprocess backend inherits descriptor zero. In two fixed native
cases it is an empty FIFO: ripgrep 13.0.0 returns exit 1 with no matches when no
path is supplied, although the unchanged source contains the literal. Explicit
directory/file searches recover matches. Empty-pipe, matching-pipe, null-input
and genuinely absent-literal controls distinguish input selection from source
absence. Twenty-four charged commands run under original compilation; synthetic
replies submit empty patches. No model weights, repair grader or source edit is used.

Six fresh controls reproduce the contrast with synthetic source and ripgrep 15.2.0,
with ignore filtering uniformly disabled. [Upstream input selection](https://github.com/BurntSushi/ripgrep/blob/master/crates/core/flags/hiargs.rs)
documents the existing stdin heuristic, not a newly discovered defect. Native
controls do not capture GPU descriptor zero or establish timeout/score causality.
V22 changes only writer search instructions and passes two native package checks.
Its completed eighth study yields one verified repair versus two for v21, with
nine unknown verifiers. Both share the Rich patch; only v21 delivers the FastAPI
repair against an empty candidate timeout. The candidate is held from main upload.
In the first three pairs, explicit paths appear in all 13 observed candidate
ripgrep calls versus one of 12 baseline calls. Two candidate cases invoke ripgrep;
all six patches are empty. This bounded uptake establishes no repair benefit.

Post-outcome analysis of 239 single tool intervals totals 0.097–4.364 seconds per
task. The largest response-to-next-call gap is 126.688 seconds; a successful
baseline edit starts at 167.641 seconds. Gaps include unseparated inference, queue
and framework time, not pure thinking time. Shell edits are not automatically
classified. These exploratory timings do not establish timeout causality.

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

The version11 supplement ships 55 files, including a byte manifest, native/model
and protocol scalars, qualification outcomes, four fresh drivers and PNG/SVG figures.
Run `python verify_provenance_resource.py --fresh` to verify files, recompute recorded
analyses, compare Linux invariants and execute fresh controls. All twelve checks
pass on the downloaded resource: eight recorded checks and four fresh drivers.
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

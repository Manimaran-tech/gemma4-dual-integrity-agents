Research draft, October 8, 2026. Final Paper Track submission remains pending.

## Abstract

Offline coding agents need trustworthy feedback as well as local inference.
A passing check may exercise an installed copy rather than the edited checkout;
a content search may read inherited input rather than source files. We present
an executable provenance resource and a workflow that separates generation,
execution, source identity and independently verified repairs. On four assigned
Requests cases, unchanged native setup yields zero qualifying clean/reference
pairs; offline editable installation restores all four under unchanged assertions.
Forty synthetic native-agent loops on ten cases see source edits in six cases
without intervention, nine with conditional installation and ten with an explicit
validation environment. An independent eight-cell experiment holds interpreter,
assertion and package version fixed: foreign imports produce false acceptance
of an unfixed checkout and false rejection of a correct edit. Its invariants
replicate on Windows and Linux. Native search controls and fresh bounded-input
controls distinguish missing evidence from known failure. Nine terminal Gemma
studies preserve 108 assignments, 97 executions and 11 unattempted slots without
establishing improved repair accuracy. A native Android coding workbench illustrates
the intended application; its repository repair performance remains unmeasured.

## Problem and contribution

Running an LLM offline does not make a coding workflow reliable. The agent needs
to know what source a check exercised, whether the check completed and whether
it represents the reported issue. Otherwise more inference can optimize against
irrelevant feedback. An interface that displays “passed” without this context
can mislead both the model and its user.

We contribute an empirical software-engineering resource: source-bound native
diagnoses, unchanged-assertion controls, independent fresh experiments and
replayable model-outcome denominators. The insight is that feedback identity and
completion must be checked separately from its verdict. We do not introduce
editable installation, import resolution, local inference or agent interfaces.
The contribution is the demonstrated failure, controlled intervention and
reproducible evidence boundary, rather than a new model architecture.

The [Gemma 4 Developer Agent competition](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview)
requires `gemma-4-31b-it-qat-w4a16-ct`. Its public development harness provides
our native integration setting; private-scoring equivalence is unverified.
The current official main score is 0.08. This resource paper is assessed separately
from whether a future leaderboard entry improves that score.

## Evidence-aware offline workflow

A coding workbench should expose four separate states: generated edit, completed
command, verified input/source origin and independently verified issue repair.
Generation-loop success must not automatically advance the last state.

Before interpreting a Python check, record the interpreter, working directory,
resolved module, source hash and explicit environment. Verify that the intended
checkout is imported. Use a relevant assertion that distinguishes the clean base
from a correct implementation; source identity alone does not establish relevance.
Run checks in fresh processes with isolated bytecode caches where necessary.
For content search, pass observed files or directories explicitly. For interactive
reproductions, use finite input and a local process timeout. Exit 124 or an
unreturned tool call means incomplete observation, not a successful assertion
or a known test failure.

The allowed agent-side helper discovers one Git workspace and probes flat/src
imports in a fresh skill-interpreter process. Correct origins skip installation.
Otherwise an isolated environment may install offline using declared build tools,
without dependencies or build isolation, within 45 seconds. It rechecks origin,
removes only newly generated untracked egg-info and verifies unchanged tracked
source. Missing backends, nonisolated interpreters and persistent shadowing remain
negative observations. An explicit source-only validation environment handles
an unavailable backend; subsequent checks must actually use that environment.
Default imports are not silently rewritten. The helper uses no reference patch
and changes no evaluator or manager.

Our Android repository harness implements the generation side of this contract:
it requires native on-device inference, exposes scoped file tools with observed
hashes, protects grading configuration and exports edits for independent host
grading. It explicitly records generation stop reason and leaves task correctness
null. It has no shell or Python verifier on the device. These are implemented
interfaces, not measured repository repair results. The retained readiness
report contains no completed repository-generation/grading episodes; physical
phone measurements remain deferred. The paper's measured contribution is the
provenance resource below, not claimed mobile speed or repair superiority.

## Methods

We distinguish fixture qualification, import provenance, source-edit visibility
and model repairs. Qualification requires a nonpassing clean base and passing
official reference under the same verifier; it is not an agent repair.
Synthetic markers measure edit visibility, not solved issues.

Plans bind cases, inputs, source/package hashes, dependencies, assignment order
and notebook cells before execution. Native integration checks all 100 organizer
Python sources. Executed source, transports, archive members and full downloaded
output are reconciled. Hashes establish byte identity, not independent
authentication of grading claims. Agents receive public issue inputs; references
and protected validation remain in separate qualification controls and are excluded
from the agent view and supplement. The exposed public cases are not holdouts.

### Requests qualification

A metadata-ranked panel assigns four cases each from Requests, FastAPI and Rich.
Six FastAPI/Rich cases qualify; none of the four Requests cases does. We retain
the failed classifications without replacing Requests cases after observing them.
All four original Requests cases enter the repeated diagnosis in their original
order.

Eight pretest inventories import host Requests 2.32.4 with identical module hashes
across cases and reference conditions. The native backend adds the workspace
root to PYTHONPATH, although these checkouts use `src/requests`, and skips editable
installation. Two isolated setup interventions install the actual workspace
with `--no-index --no-build-isolation --no-deps`: immediately before native pytest,
or before native baseline creation and reference/test-patch application. The
original verifier and assertions remain unchanged. These declared setup observers
are diagnostic controls, separate from the allowed agent-side skill.

### Native and independent controls

The native panel freezes three cases each from Requests, FastAPI and Rich plus
the sole public HTTPX case. Salted metadata ranking chooses IDs without observed
outcomes; HTTPX's earlier exposure is recorded. Original compiler, runner and
budgeted skill execution use five predetermined replies without model weights.
Each loop checks an inert source marker in a fresh process, restores its bytes
and submits an empty patch with two charged tools. Infrastructure failures stop
execution; their assigned slots are preserved.

Independent standard-library drivers create disposable repositories, isolated
environments and fresh processes. Flat/src packages share one implementation
and one assertion. A same-length source edit changes the assertion from failing
to passing; separate caches prevent stale-bytecode effects. A foreign-PYTHONPATH
control must fail provenance even after installation. A missing-backend control
tests an explicitly applied source environment. No competition data, evaluator,
model or reference is used.

The factorial experiment crosses checkout state (buggy/corrected), foreign-copy
state (buggy/corrected) and origin (workspace/foreign). Its eight conditions use
one disposable src repository, interpreter, byte-identical assertion and version
0.0.1. Every process records module path/hash. Inspect-only guards must match the
test-process origin and preserve tracked diffs; no installation occurs. Conditions
are not independent repository tasks.

## Results

All 24 Requests verifier executions complete. Unchanged setup imports host source
in all eight checks: three pairs fail to verify their reference and one already
passes at baseline. Both installation conditions import workspace source in all
eight checks and yield four failing clean bases and four passing references.
Repeated setup conditions on four cases are not twelve repair successes.

| Setup | Workspace imports / checks | Qualified pairs / cases |
| --- | ---: | ---: |
| Unchanged native subprocess setup | 0/8 | 0/4 |
| Install immediately before pytest | 8/8 | 4/4 |
| Install before baseline and patch application | 8/8 | 4/4 |

Across the first 20 synthetic native loops, inspect-only sees edited source in
six of ten cases; conditional installation reaches nine. Requests needs three
installs; HTTPX remains negative because its build backend is absent offline.
An initial manifest failure stops execution. The retained execution-only amendment
adds the omitted verifier hash without changing source, cases, order or limits.
The second 20 loops apply the explicit source environment: six FastAPI/Rich skips,
three Requests installs and one HTTPX environment reach ten of ten. All patches
remain empty. These controls establish integration and edit visibility, not model
selection of the intervention or repair accuracy.

The independent layout, missing-backend and shadowing controls reproduce their
declared outcomes. All eight factorial conditions complete on Windows Python
3.12.14. Identical frozen code/plan runs on Kaggle Linux Python 3.13.15 with matching
invariants; installation controls are not repeated on Linux. Intended-source
imports fail before the edit and pass after it regardless of the foreign copy.
Foreign imports instead give:

| Intended checkout | Imported foreign copy | Assertion | Meaning |
| --- | --- | --- | --- |
| Buggy | Buggy | Fails | Coincidentally correct feedback |
| Buggy | Corrected | Passes | False acceptance |
| Corrected | Buggy | Fails | False rejection |
| Corrected | Corrected | Passes | Coincidentally correct feedback |

Both copies report the same package version. The guard accepts four workspace
origins and rejects four foreign origins, including coincidentally correct verdicts.
This construction demonstrates a mechanism, not its population prevalence.
A passing command and matching version do not prove checkout validation.

### Input identity and incomplete commands

Two native CPU cases observe descriptor zero as an empty FIFO. Pathless ripgrep
13.0.0 returns no matches although unchanged source contains the literal; explicit
directory/file paths restore matches. Empty-pipe, matching-pipe, null-input and
absent-literal controls separate input selection from source absence. All 24 charged
commands use original compilation, synthetic replies and empty patches. Six fresh
controls reproduce the input contrast with synthetic source and ripgrep 15.2.0.
The [upstream input-selection implementation](https://github.com/BurntSushi/ripgrep/blob/master/crates/core/flags/hiargs.rs)
documents the established heuristic. GPU descriptor zero was not captured.

In the ninth model study, 219 tool calls have 218 completed observations. One
interactive reproduction has no returned result. A private replay on the same
public base shows constant invalid mocked input stalling until a two-second local
timeout, whereas finite invalid/valid input completes. This diagnoses one
reproduction mechanism; it neither fixes the library issue nor explains all
session timeouts. Fresh synthetic bounded-input controls reproduce that mechanism
without library source or model outputs. Missing intervals remain censored and
are excluded from completed-tool latency totals. Native synthetic wire controls
also show that a locally bounded command error returns control to the agent while
the organizer's 300-second command setting stays unchanged.

## Model studies: integration is insufficient

Nine terminal studies retain 108 assigned slots, 97 completed executions and
11 unattempted assignments. The first six repeat one exposed panel; the last
three repeat another. They cannot be pooled as independent trials.

| First / second arm | Executions / assigned | Pairs with both verifiers known | Verified successes, first / second |
| --- | ---: | ---: | --- |
| Shell / tool-rich | 12/12 | 4 | 1/6 / 2/6 |
| Shell / evidence workflow | 7/12 | 3 | 0/3 / 0/4 |
| Three / five minutes | 7/12 | 0 | 0/3 / 0/4 |
| Source-validation / focused prompt | 12/12 | 2 | 2/6 / 2/6 |
| Source-validation / structured interface | 12/12 | 1 | 2/6 / 1/6 |
| Source-validation / flat interface | 11/12 | 1 | 2/5 / 1/6 |
| Source-validation / hypothesis pipeline | 12/12 | 1 | 1/6 / 2/6 |
| Hypothesis pipeline / explicit search | 12/12 | 1 | 2/6 / 1/6 |
| Hypothesis pipeline / reduced writer reasoning budget | 12/12 | 0 | 0/6 / 0/6 |

Success denominators include completed executions with unknown verifiers; they
are not known-outcome accuracy estimates. Minus-one grades remain unknown and
unattempted slots have no observed outcome. Two studies stop on protected-test
conflicts; the flat-interface study stops after a removed-tool error. No assigned
negative or missing case is replaced.

The pipeline adds one verified delivery against an empty parent timeout, but
only one pair has both verifier outcomes known. Explicit search instructions
increase bounded observed path use (13/13 candidate calls versus 1/12 baseline
calls in the first three pairs) without improving repairs. Reducing the configured
writer reasoning budget from 4096 to 1024 yields zero repairs in both arms,
11 unknown verifiers and one known failed production patch. All 12 executions
omit explicit status, source-guard and submission calls. Native timeout fallback
can still capture a patch; absent submit calls alone do not prove no edit.

Post-outcome timing contains inference, queue, framework and cancellation gaps
that are not separately measured. Completed commands are often short, but the
unreturned command cannot be assigned zero duration. Synthetic compiler/wire
checks verify configured parameters and handoff, not deployed reasoning-budget
enforcement or model adherence. No hidden-score or prize-level gain is established.

## Related work and practical scope

[SWE-agent](https://arxiv.org/abs/2405.15793) studies repository interfaces;
[Agentless](https://arxiv.org/abs/2407.01489) separates localization, repair and
validation. [HarnessFix](https://arxiv.org/abs/2606.06324v2) diagnoses harness flaws
from traces, while [AI Harness Engineering](https://arxiv.org/abs/2605.13357)
examines runtime verification responsibilities. Our resource focuses on a specific
input/source identity failure with unchanged assertions and preserved missingness.
[pytest documentation](https://docs.pytest.org/en/stable/explanation/pythonpath.html)
already explains local-versus-installed import selection; we do not claim discovery
of that mechanism.

[Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) already supplies
offline mobile interfaces, agent skills and device use cases.
[AutoDroid-V2](https://arxiv.org/abs/2412.18116v3) uses on-device small-model code
generation for mobile automation. These rule out a broad first-mobile-harness
claim. Our intended application is an offline repository workbench that displays
generation evidence separately from independently graded correctness. Demonstrating
its mobile repair utility requires measured episodes that are not yet available.

## Reproducibility and limits

The [version12 resource](https://www.kaggle.com/datasets/manimaran2308/requests-source-provenance-replay-v1)
retains 60 files: hashes, qualification outcomes, model/protocol scalars, figures
and five fresh drivers. All 14 checks pass on the downloaded resource: nine recorded
checks and five fresh drivers. `python verify_provenance_resource.py --fresh` checks member
bytes, recomputes recorded analyses, compares Linux invariants and executes fresh
controls. Recorded replay checks consistency, not independent authentication or
a rerun of native grading/inference. Fresh controls require Python 3.11+, Git,
local build tools and ripgrep; missing prerequisites stop rather than download
dependencies. Authored code is MIT licensed; data/figures use CC BY 4.0.

The Requests sample is small and exposed. Native integration uses synthetic
replies. Constructed controls establish mechanisms, not real-world prevalence.
The guard covers flat/src Python files; namespace packages, compiled extensions,
multiple target modules, plugins and workers need further testing. A preflight
origin probe does not instrument every module inside subsequent tests. Correct
source alone proves neither issue relevance nor regression safety.

Private-scoring equivalence, the full twelve-hour main schedule, improved Gemma
repair accuracy and mobile repository performance remain unverified. Pending
main experiments are excluded from the terminal-study table. The resource makes
these evidence boundaries explicit so a local AI interface can report what its
workflow actually established.

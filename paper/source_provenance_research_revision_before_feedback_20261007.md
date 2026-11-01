# When repair checks import the wrong source: Gemma 4 provenance controls

Conditional offline setup and reproducible validation under finite tool budgets

Research draft, October 7, 2026. This manuscript is not a final Paper Track entry.

## Abstract

A repository repair check can execute successfully while importing an installed
library instead of the edited checkout. This makes the check insensitive to the
proposed patch and can invalidate a repair comparison. We investigate this failure
in the supplied Gemma 4 development harness, separating environment qualification,
agent-side validation and model repair outcomes. In four previously assigned
Requests cases, all eight native pretest inventories import the same host module;
none of the four clean-base/reference pairs qualifies. A separately declared,
genuine offline editable installation changes all eight imports to workspace
source and restores all four pairs: clean bases fail and reference patches pass
under the unchanged verifier and assertions. We implement a conditional source
guard through an allowed, budgeted sandbox skill, rather than an evaluator setup
hook. A fresh experiment independent of competition data verifies flat and src
layouts, source-edit sensitivity, skipped repeat installation and a retained
foreign-import negative control. Forty native integration loops on the same ten
cross-repository cases verify edited source in six cases without intervention,
nine with conditional installation, and ten with an explicitly applied source
validation environment. These results support a reproducible provenance
check for repair validation; they do not establish Gemma repair improvement or
equivalence to the private competition scorer.

## Introduction

Software repair agents depend on feedback from commands executed in a repository.
A failing test is useful only when it exercises the intended implementation and
its failure represents the reported behavior. Import failure, missing plugins,
stale bytecode and imports from another installation each break a different part
of that feedback contract. More inference time cannot by itself establish which
source a test has exercised.

The [Gemma 4 Developer Agent competition](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview)
requires `gemma-4-31b-it-qat-w4a16-ct` for model-backed agents. Its global patch
generation budget is twelve hours including setup, with patch validation excluded.
The [official starter](https://www.kaggle.com/code/ryanholbrook/getting-started-gemma-4-developer-agent)
provides a development harness and public tasks. We use that development setting
to study validation provenance, while retaining separate model and grader outcomes.
Our diagnosis concerns the local subprocess backend, not a demonstrated defect in
the private scoring infrastructure.

We ask three questions. Does an observed import mismatch explain the inability to
qualify the four assigned Requests fixtures? Can a submission detect and conditionally
correct its own imports using the original compiler and budgeted tools? Can a
reviewer reproduce the mechanism without competition snapshots, reference patches
or a large model? Our contribution is a source-bound diagnosis, a conservative
agent-side implementation and an executable independent control protocol. Editable
installation and persistent notes are established techniques; we do not claim to
invent them or claim a first-of-its-kind benchmark failure.

## Methods and experimental boundaries

We distinguish four outcomes: fixture qualification, source import provenance,
source-edit visibility and verified model repair. A qualified fixture has a
nonpassing clean base and a passing official reference under the same verifier.
Qualification does not count as an agent repair. An import-origin success does
not prove that an assertion tests the issue. A synthetic source marker is a
mechanism control, not a solved repair task.

Plans bind task identities, problem-only inputs, source hashes, package bytes,
dependency manifests, condition order and notebook cells before execution.
Agent inputs contain only instance ID, repository, base commit, problem statement
and hints. Reference patches and private validation remain inside independent
CPU verifier controls; they are excluded from the agent and public supplement.
The public pool has prior research-assistant reference exposure. These experiments
are development studies and are not described as untouched holdouts.

The organizer core packages and verifier source remain fixed. Genuine supplemental
HTTP/snapshot dependencies were declared before the relevant repeated controls;
no assertion, protected test or production fix was altered to manufacture a pass.
The verifier function SHA256 is
`98600fd6066a4dbd472490cb194b839a3a633afea9b99256cc081ea77beac0d3`.
Native integration additionally checks all one hundred organizer Python source
files against the retained inventory. Exact code cells, chronological transport
archives, member hashes and directly downloaded output are reconciled. Hashes
establish byte identity, not independent authentication of scientific claims.

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

### Conditional agent-side guard

The standalone helper accepts an existing import name supported by source in a
flat or src layout. It discovers one Git workspace and inspects the module in a
fresh process using the skill executor's interpreter. It verifies the resolved
imported file against the expected source file, rather than trusting a version
string or successful import alone. A fresh bytecode-cache prefix prevents a rapid
source edit from being concealed by an existing repository cache.

Correct imports skip installation. Otherwise, installation is permitted only
inside an isolated virtual environment with the declared backend available. It
installs only the workspace project, without network access, dependency resolution
or build isolation. Installation is bounded to forty-five seconds. The helper
rechecks provenance, removes only newly generated untracked egg-info and confirms
the tracked diff did not change. Missing build tools, import exceptions,
nonisolated interpreters and persistent shadowing remain environment failures.
It performs no evaluator or manager patch and accesses no reference solution.

The staged v14/v15 packages retain the required model, nine original native tools,
temperature 0.1, top_p 0.95, top_k 40, output limit 8192 and thinking budget 4096.
Their optional sidecars retain three task minutes, fifty charged tools, one hundred
turns and a 300-second command timeout. Their prompts require provenance checking
before trusting Python assertions. A separate exact graph-key instruction corrects
a previously observed API mismatch; it is not isolated as a factor here. These
packages are proposed integration candidates, not selected accuracy winners.
V15 adds an explicit source-path validation fallback when the build backend is
absent or installation would require a nonisolated interpreter. It verifies
the source import under the returned environment; default imports are unchanged.

The native integration panel freezes three previously unassigned cases each from
Requests, FastAPI and Rich, plus the sole public HTTPX case. IDs are ranked by
SHA256 of a fixed salt and case ID; issue text and outcomes do not rank them.
HTTPX's prior exposure is recorded and its single case cannot support a precise
repository-level generalization estimate. Each case gets two fresh native
sandboxes using the same v14 archive and identical predetermined HTTP transport.
The v14 condition change adds `--ensure` to the skill call. A separately frozen
v15 repetition preserves the same cases, order and tool budget, while allowing
the explicit source-path fallback and applying its returned environment to the
synthetic visibility command.

The original agent runner, compiler, ADK tool serialization, skill loader and
budgeted executor run without model weights. Predetermined replies load the skill,
execute the guard, run a synthetic source-visibility control and submit an empty
patch. The visibility control appends an inert marker to the existing imported
source, reads it in a fresh process and restores the identical original bytes
before submission. Each complete loop must retain an empty patch and two charged
tools. Infrastructure failures stop the panel; unsuccessful environment outcomes
stay assigned. No synthetic loop counts as a model repair.

### Independent fresh experiment

The supplement includes a standard-library driver requiring Python 3.11+, Git
and locally installed pip, setuptools and wheel. It creates disposable Git
repositories and an isolated environment. Flat and src packages contain the
same tiny implementation. An identical assertion fails before a same-length
source edit and passes afterward, using fresh processes and separate cache
prefixes. A third control prepends a foreign module through PYTHONPATH; the guard
must report unsuccessful provenance even after installation. This protocol uses
no Kaggle data, evaluator, model or reference patch.

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

Figure 1. The supplement retains the PNG/SVG and scalar denominators. Its
agent-import contrast uses separate synthetic native-agent loops, while
qualification uses the independent native verifier. Neither is Gemma accuracy.

Eight earlier native agent loops independently reproduce the import contrast:
unchanged setup imports host source in four of four cases; local installed setup
imports workspace source in four of four. All patches remain empty. A complete
native Evaluator integration executes both frozen v5/v10 packages on the four
cases with synthetic replies: sixteen agent/verifier sandbox installations read
workspace source, and all eight empty patches retain the expected nonpassing
clean-base grade. These controls establish the local environment intervention's
reach, not a model's ability to choose or benefit from it.

The fresh independent replay completes all three controls on Windows Python
3.12.14. Flat imports already read source and skip installation; src imports
change from missing to workspace source after one offline install. The fixed
assertion changes from exit 1 to exit 0 after the controlled source edit in both
layouts. Repeat setup skips installation. The foreign-PYTHONPATH control remains
unsuccessful and is correctly rejected. Repeating the experiment from the
extracted supplement reproduces these outcomes. Eight additional local tests
cover these behaviors, nonisolated setup, missing backend and invalid import names.

The twenty-control cross-repository native integration panel completes and
reconciles. Inspect-only setup reads edited source in six of ten cases: all
FastAPI/Rich cases. Conditional installation raises source-import verification
and marker visibility to nine of ten, with exactly three Requests installs.
The HTTPX case remains negative because `hatchling.build` is absent offline.
Its first execution failed before controls because the experiment manifest
omitted the shared environment verifier hash. The execution-only amendment
preserves the candidate, cases, order, conditions, limits and source bytes,
adding the exact parent verifier hash and an empty dormant schedule. The initial
failure remains retained and supplies no control observations.

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

## Relationship to model repair performance

Eleven completed historical model traces cover five distinct exposed cases.
Three verified artifacts repair the same Rich case; two are the identical patch.
They do not represent three independent task successes or candidate improvement.
The first prospective interface comparison completes five of eight assignments
with zero verified repairs and only two complete pairs. Three assignments remain
unattempted after a scheduler stopping-rule defect. A broader comparison fails
before inference at its archive-membership guard; that execution is retained.

The exact broader execution amendment now completes all twelve assignments on
six previously qualified FastAPI/Rich cases. The original tool-rich arm repairs
two of six; the shell arm repairs one of six. One Rich case succeeds only with
the original arm, another succeeds with both, and four cases fail with both.
One discordant pair on this exposed panel does not establish superiority. The
first FastAPI case consumes six minutes without a source edit in either arm:
thirty-nine search/read calls versus fifteen shell calls plus one budget query.
A separate shell attempt produces only two reproduction scripts. In a successful
Rich trace, the original agent makes the correct source edit at 92 seconds,
formats the whole repository, erases its edit with a whole-worktree checkout,
then repeats the edit before submitting at 286 seconds. This observed rollback
motivates preserving source changes; it does not prove a counterfactual
three-minute failure or imply that extra time alone fixes the agent.

The controlled evidence-workflow study completes seven of twelve assigned model
executions with zero verified repairs. Its three complete FastAPI pairs fail.
The seventh execution edits a protected Rich test file; the grader's test patch
cannot apply. The prospectively retained stopping rule halts at that returned
minus-one result. Five assignments remain unattempted, and the test-patch
conflict is not counted as a completed scored repair. Neither missing outcomes
nor this conflicting patch is reclassified to improve the candidate. Both
terminal studies reconcile every chronological archive, patch, grade, trace
and completed code cell with direct Kaggle output. The supplement retains
all assigned scalar outcomes and reproduces these denominators.

The Requests import diagnosis does not explain every failed FastAPI/Rich repair.
Both failed FastAPI documentation-task arms contain no tool-error responses,
while a successful Rich transfer contains several malformed path calls. Error
counts alone are insufficient to identify repair failure causes. A separate
graph control finds thirteen exact node keys returning results and thirteen
unique suffixes returning none in one public graph. This supports correcting a
tool instruction, without establishing localization or repair improvement.

The official v12 runtime-calibration submission completes with public score
0.08. This is a separate, unchanged earlier agent with no new guard, and supplies
no v14/v15 comparison or hidden-task traces. We make no repair-performance claim
for v14/v15. A future model study must
preserve paired cases, equal budgets, all missing assignments and environment
conditions, and report candidate-only repairs, baseline-only repairs and
regressions. Qualification outcomes cannot substitute for that comparison.

## Related work

[SWE-agent](https://arxiv.org/abs/2405.15793) studies the agent–computer interface;
[Agentless](https://arxiv.org/abs/2407.01489) organizes repair around localization,
patch generation and validation. [EnvBench](https://arxiv.org/abs/2503.14443)
treats environment setup as a distinct evaluation problem, while
[SWT-Bench](https://arxiv.org/abs/2406.12952) studies issue reproduction and tests
as filters for repairs. These motivate explicit environment and feedback checks.
Their model results do not predict Gemma 4 performance. Our narrower contribution
is the observed provenance failure, unchanged-assertion controls, conditional
budgeted integration and a fresh executable negative-control protocol.

## Reproducibility and limitations

The attached supplement provides recorded qualification/import scalars,
classifier, byte manifest, figure and `replay.py`, which recomputes the recorded
numbers. `fresh_source_provenance_replay.py` executes the independent experiment
and includes its standalone guard and a recorded expected result.
`fresh_source_path_replay.py` adds the missing-backend control and demonstrates
why the returned environment must be applied explicitly.
`terminal_model_scalar_replay.py` recomputes the completed model-study counts,
paired discordances and unavailable validation without imputing missing outcomes.
These scripts have different roles; scalar replay is not fresh grader execution. Runtime
versions and timestamps may differ on another machine, while assertions and
source-bound observations should remain comparable. Missing prerequisites must
be reported rather than repaired by downloading dependencies during the experiment.

The Requests sample is small and already exposed. Cross-repository integration
uses public development tasks and synthetic transport, not model decisions.
The guard supports flat/src Python layouts, requires importable dependencies and
refuses nonisolated installs. It does not correct every environment failure or
prove test relevance. A later pytest invocation must use the same interpreter
and source paths for the recorded provenance to apply.

The private scoring environment, full twelve-hour generation schedule and
improved Gemma repair rate remain unverified. The current official main score
is 0.08; neither staged guard candidate has a leaderboard score. These limits
constrain the claims, while fresh repository-independent controls make the
proposed provenance mechanism
directly testable beyond the competition dataset.

Research draft, October 7, 2026. Final Paper Track submission remains pending.

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
correct edit. The guard rejects all four foreign origins. These results support
reproducible validation controls, not improved Gemma repair accuracy or equivalence
to the private scorer.

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
agent-side implementation and an executable protocol exposing both directions of
misleading validation feedback. Editable
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

The staged v14/v15 packages retain the required 31B model, nine original tools
and unchanged sampling. Their sidecars retain three task minutes, fifty charged
tools, one hundred turns and a 300-second command timeout. Prompts require origin
checking before trusting Python assertions. An exact graph-key correction is
bundled and is not isolated here. V15 adds a source-only validation environment
when the backend is missing or installation is nonisolated. The returned prefix
must be explicitly applied; default imports remain unchanged. These packages
are integration candidates without established accuracy improvement.

The native panel freezes three cases each from Requests, FastAPI and Rich,
plus the sole public HTTPX case. A fixed salted SHA256 ranks IDs, not issue text
or outcomes; HTTPX's prior exposure is recorded. Each case gets two fresh native
sandboxes and identical predetermined transport. V14's only condition change
adds `--ensure`. A frozen v15 repetition preserves cases, order and tool budget,
while applying its returned environment to the visibility command. This panel
supports no precise repository-level generalization estimate.

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

Figure 1 separates native fixture qualification from synthetic agent imports.
The supplement retains its denominators and source data; neither contrast is
Gemma repair accuracy.

Earlier native synthetic agent and Evaluator controls reproduce the Requests
import contrast while preserving empty patches and the expected nonpassing
clean-base grade. They establish the local intervention's reach; synthetic
replies cannot establish a model's ability to choose or benefit from it.

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
matching all eight invariant observations. The [Linux replay notebook](https://www.kaggle.com/code/manimaran2308/fresh-import-feedback-portability-controls)
uses no competition input or model. These are repeated conditions on the
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

## Relationship to model repair performance

The source diagnosis does not explain every failed FastAPI/Rich repair. We keep
model results separate and retain failed, interrupted and unattempted assignments.
The broader execution amendment completes twelve assignments on six qualified,
exposed FastAPI/Rich cases. Tool-rich repairs two cases; shell repairs one. One
Rich case favors tool-rich, one succeeds with both, and four fail with both.
One discordant pair cannot establish general superiority.

The evidence-workflow study completes seven of twelve model executions with no
verified repair. Three complete FastAPI pairs fail. Its seventh execution edits a
protected Rich test file, preventing the grader's test patch from applying. The
original stopping rule halts at that unavailable validation result; five assignments
remain unattempted. The supplement reproduces every assigned denominator and
preserves missing outcomes as missing.

A successful tool-rich trace makes its correct source edit at 92 seconds, formats
the entire repository, erases that edit with a whole-worktree checkout, then
reapplies it and submits at 286 seconds. This observed rollback motivates preserving
production changes; the last edit time does not establish a counterfactual
three-minute failure. Other traces consume six minutes without production edits
or retain only reproduction scripts. Reliable imports alone do not resolve these
agent failures.

Both terminal studies reconcile chronological archives, exact executed code,
patches, grades and traces with directly downloaded output. Historical smaller
studies and setup failures remain documented in the supplement. The unchanged
earlier v12 submission completes at public 0.08; it supplies no new-guard comparison
or hidden-task traces. Improved repair accuracy requires a future paired model
study reporting candidate-only repairs, baseline-only repairs and regressions.

## Related work

[SWE-agent](https://arxiv.org/abs/2405.15793) studies the agent–computer interface;
[Agentless](https://arxiv.org/abs/2407.01489) organizes repair around localization,
patch generation and validation. [EnvBench](https://arxiv.org/abs/2503.14443)
treats environment setup as a distinct evaluation problem, while
[SWT-Bench](https://arxiv.org/abs/2406.12952) studies issue reproduction and tests
as filters for repairs. These motivate explicit environment and feedback checks.
[pytest documentation](https://docs.pytest.org/en/stable/explanation/pythonpath.html)
also explains how import paths can select an installed or local package.
Their model results do not predict Gemma 4 performance. Our narrower contribution
is the observed provenance failure, unchanged-assertion controls, conditional
budgeted integration and fresh executable controls for misleading test feedback.

## Reproducibility and limitations

The supplement ships a byte manifest, recorded native/model scalars, three fresh
experiment drivers, expected observations and PNG/SVG figures. Run
`python verify_provenance_resource.py --fresh` to verify files, recompute the
recorded analyses, compare recorded Linux invariants and execute the fresh controls.
Scalar replay does not rerun or independently authenticate native grading or
model inference. The fresh experiments require Python 3.11+ and Git; the installation
controls additionally require locally available pip/setuptools/wheel. Missing
prerequisites stop execution; dependencies are never downloaded. Runtime versions
and temporary paths may differ, while invariant observations are compared exactly.
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

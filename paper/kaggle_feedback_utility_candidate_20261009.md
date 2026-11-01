# When passing tests validate the wrong source

*Source and process evidence for offline coding workbenches*

Local working candidate, 9 October 2026. The four-episode matched phone pilot is
running; its independent grades are pending. This file has not been filed as a
final Kaggle paper, and no DOI has been issued.

## Abstract

An offline coding agent can receive a passing test result for a package it did
not edit. A successful source preflight can also describe a different process
from the one that later executes the test. We investigate these boundaries using
native organizer diagnoses, unchanged assertions and source-bound observations.
Four exposed Requests cases provide no qualifying clean/reference pairs under
unchanged setup; two declared offline installation interventions restore all four.
Controlled experiments reproduce false acceptance and rejection despite identical
package versions. In a three-library study, actual API-process evidence retains
144 supported decisions with zero wrong verdicts in each operating system's 288
constructed conditions, while exit/version/preflight policies make 72 wrong
checkout verdicts. Ten Gemma development studies preserve missing outcomes without
establishing repair gains. Native phone observations further separate successful
tool use and generation-loop completion from delivered source changes. We provide
an executable evidence resource for interfaces that distinguish proposed edits,
observed execution, source attribution and independently verified repairs.

## Problem and contribution

Useful local AI needs a workflow that tells the user what actually happened. A
coding workbench should distinguish an edited file from a tested fix, and a tested
fix from a result obtained against an unrelated installed copy. Package version
equality cannot distinguish these copies. A preflight source probe does not bind
a later interpreter or worker to the same source.

Our contribution is a reproducible empirical resource for these feedback
boundaries. It combines a native source-selection diagnosis, controlled setup
interventions, independent process experiments and a conservative model-outcome
audit. We do not introduce a new model architecture or claim the first offline
mobile interface. The measured question is which evidence supports a source
verdict while retaining useful decisions, rather than merely abstaining on every
check. A second question asks whether integration evidence translates into
improved Gemma repairs.

Plans freeze case IDs, problem-only inputs, source/package hashes, dependencies,
assignment order and notebook cells before execution. Native qualification checks
all 100 organizer Python sources. Executed source, unchanged exports, full output
and API transports are reconciled. Hashes establish artifact identity; scalar
replay alone does not authenticate a grader or repeat model inference. References
and protected validation remain evaluator-only. All competition cases used here
are exposed public development cases.

## Native source-selection diagnosis

A metadata-ranked panel assigns four cases each from Requests, FastAPI and Rich.
This diagnosis uses frozen swegemma 0.2.7, adk-submission 0.2.12 and
adk-eval-core 0.1.0. Later organizer updates and qualifications have separate
source identities; their results do not reinterpret the original observations.
The four Requests cases fail fixture qualification: the clean base must fail and
the official reference must pass under the same verifier. No failed case is
replaced. Inventories show host Requests 2.32.4 imported in all eight unchanged
clean/reference checks. The native backend adds the checkout root to PYTHONPATH,
although the package resides under `src/requests`, and skips editable installation.

Two diagnostic interventions install the checkout offline with `--no-index
--no-build-isolation --no-deps`: immediately before native pytest, or before
baseline creation and reference/test-patch application. The verifier and assertions
remain unchanged. Each check records its interpreter and selected source.

| Setup | Workspace imports / checks | Qualified pairs / cases |
| --- | ---: | ---: |
| Unchanged native setup | 0/8 | 0/4 |
| Install immediately before pytest | 8/8 | 4/4 |
| Install before baseline and patch application | 8/8 | 4/4 |

All 24 verifier checks complete. Unchanged setup yields three unverified-reference
pairs and one already-passing clean base. Both installation conditions restore
four discriminating fixtures. These are setup interventions on four exposed cases,
not generated repairs or evidence that every acceptable implementation is tested.

Synthetic predetermined replies separately exercise original compilation, tools
and budgets on ten public cases from Requests, FastAPI, Rich and HTTPX. Forty loops
compare inspect-only, conditional installation and explicit-source environments.
Edited source is observed in six, nine and ten cases respectively. HTTPX remains
negative under conditional installation because its build backend is unavailable
offline. Markers are restored and patches remain empty. The model did not discover
these interventions autonomously.

## Independent process experiments

The original eight-condition control crosses checkout state, foreign-copy state
and selected origin. Fixed assertions and identical version strings reproduce
false acceptance of an unfixed checkout and false rejection of a correct edit.
The mechanism replicates on Windows and Linux.

A sixteen-condition extension adds flat/src layouts and separates preflight from
the later test process. Preflight always imports the intended workspace; the
assertion process receives either intended or foreign source. Each actual check
records module origin, hash, version, interpreter and process identity. Two fresh
repetitions per operating system preserve identical policy outcomes:

| Feedback policy | Decisions /16 | Wrong checkout verdicts | Unsupported source claims | Unknown /16 |
| --- | ---: | ---: | ---: | ---: |
| Exit, version plus exit, or preflight plus exit | 16 | 4 | 8 | 0 |
| Actual test-process origin plus exit | 8 | 0 | 0 | 8 |
| Always unknown | 0 | 0 | 0 | 16 |

Four foreign-copy verdicts are coincidentally correct but still do not validate
the intended checkout. Actual-process evidence retains eight useful decisions;
always-unknown retains none. These are constructed conditions on one package,
not natural failure rates or independent software issues.

### Three real-library APIs

A separately frozen study captures source and original licenses from packaging
26.3, idna 3.20 and urllib3 2.8.0. Fixed assertions exercise name normalization,
label length and case-insensitive headers. One declared same-length fault per
library creates faulty/original workspace and foreign copies with equal versions.
The 48-condition grid per library crosses two layouts, both copies' source states,
selected origin and three boundaries: a fresh process in the same interpreter,
a second isolated interpreter, and a nested worker.

Two repetitions assign 288 conditions per operating system. Observer-off/on checks
use identical assertions; the observer records root and API-module origins after
execution. No dependencies are downloaded or installed. Final file hashes are
observations, not authentication of every executed byte or dependency import.

All 288 conditions and 576 API checks complete on each operating system. Every
library qualifies its original/injected-fault pair. No assertion exit changes
when the observer is enabled. Outcomes agree across both operating systems,
libraries and declared boundaries. Counts below are per operating system:

| Feedback policy | Decisions /288 | Wrong checkout verdicts | Unsupported source claims | Unknown /288 |
| --- | ---: | ---: | ---: | ---: |
| Exit, version plus exit, or preflight plus exit | 288 | 72 | 144 | 0 |
| Actual API-process root/module evidence | 144 | 0 | 0 | 144 |
| Always unknown | 0 | 0 | 0 | 288 |

Each library contributes 48 supported decisions and 24 wrong exit-only verdicts.
The endpoint is useful feedback classification under controlled source selection,
not full-project regression safety or model accuracy. Windows observer-off/on
median check times are 0.125/0.141 seconds; Linux medians are 0.199/0.206 seconds.
Fixed order and cache effects prevent a causal overhead claim. Kaggle's global
sitecustomize emits a nonfatal missing-wrapt warning in all 576 Linux checks;
assertions and source receipts complete, but clean startup is not established.

## Other feedback and model boundaries

Native search controls observe descriptor zero as an empty FIFO. Pathless ripgrep
returns no matches despite an unchanged source literal; explicit paths restore
matches. Empty/matching pipes, null input and absent-literal controls distinguish
input selection from source absence. Twenty-four charged native commands use
synthetic replies and empty patches; six fresh controls reproduce the mechanism.
[ripgrep's implementation](https://github.com/BurntSushi/ripgrep/blob/master/crates/core/flags/hiargs.rs)
documents the existing input heuristic. GPU descriptor identity was not captured.

One model-study reproduction has no returned tool result. A private replay shows
constant invalid mocked input stalling until timeout, while finite input completes.
Independent controls reproduce that pattern. Missing intervals remain censored;
this does not explain every timeout or establish a library repair.

Ten terminal Gemma development studies retain 120 assigned slots, 109 completed
executions and 11 unattempted slots. They reuse two exposed six-case panels. The
21 verified repair observations are repeated observations, not 21 unique issues.
The historical nonnegative-exit convention retains 40 known verdicts. Treating
five exit-2 collection/interrupt results as unknown leaves 35 known and 85 unknown
or unattempted slots. Original native grades remain retained. Worst-case paired
outcome bounds include zero in every study; these are sensitivity bounds, not
confidence intervals or imputed grades. The latest bounded-writer study verifies
one production repair per arm on the same issue, without established overall gain.

## Native mobile workbench

The prototype uses Gemma 4 E2B through LiteRT-LM on an S24 FE, CPU threads 2,
4,096-token context and scoped repository tools. It provides hash-checked edits
and unchanged exports for separate host grading, rather than a phone Python/shell
verifier. Isolated test APKs request no permissions or application components.
Stock-state, ownership and thermal checks precede installation; temporary apps and
private model/workspace data are removed after terminal or failed sessions.

The original twelve-slot study retains zero verified repairs, one verified failure
and eleven unknown outcomes: three pre-inference failures, one actual episode and
eight unattempted assignments. The actual episode ends after 222.868 seconds with
six responses, one successful root listing and four failed repository actions.
It reads no production source and exports no change. Independent grading fails
the clean base and unchanged export while passing the reference.

A separate adaptive interface revision adds directory search and actionable
errors. Its one exposed episode finishes in 96.894 seconds with two successful
tools, but searches docs, reads no production file and exports no edit despite a
successful generation-loop flag. Fresh independent grading again establishes
failure. This sequential single-case observation is outside the original study.

The episodes retain 528 and 247 memory samples, all reporting Calculator in the
foreground. Sampled maximum whole-app PSS is 2,923.55 and 3,107.25 MiB respectively;
battery temperatures span 39.8–40.9°C and 39.2–39.9°C. Both owned installations
were removed and absence verified. Foreground presence is not UI responsiveness;
sampled PSS is not exact peak or model-only memory; temperature is not energy.

A new four-episode pilot freezes two exposed tasks and counterbalanced baseline/
progress-policy arms in the same APK. The intervention adds production candidates,
read/hash prerequisites, bounded progress and a no-change postcondition. Thirty-seven
host controls and fifteen physical model-free controls pass. These controls are
integration evidence. Current native outcomes and fresh independent grades are
pending; no improvement claim follows from preparation. One trial per arm/task
cannot establish repeatability, population accuracy or component effects.

## Positioning and reproducibility

[SWE-agent](https://arxiv.org/abs/2405.15793) studies agent–repository interfaces;
[Agentless](https://arxiv.org/abs/2407.01489) separates localization, repair and
validation. [HarnessFix](https://arxiv.org/html/2606.06324v2) diagnoses harness flaws;
[HarnessTester](https://arxiv.org/html/2610.04921v1) evaluates test adequacy.
[STING](https://arxiv.org/html/2604.01518v1) strengthens weak assertions. Here the
source-selection failures occur under unchanged assertions.
[Harness or Model?](https://arxiv.org/html/2609.11987v1) motivates separating
completion from correctness. Our exposed adaptive panels do not establish
contamination-controlled superiority.

[pytest documentation](https://docs.pytest.org/en/stable/explanation/pythonpath.html)
already explains local/installed import selection.
[Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) and
[AutoDroid-V2](https://arxiv.org/abs/2412.18116v3) establish prior mobile interfaces
and on-device workflows. Our contribution is the specific empirical source/process
diagnosis and executable evidence resource, rather than discovery of these ideas.

The unified local v14 resource contains 208 byte-verified members. A fresh replay
from extracted files completes all 288 API conditions. It retains original notices,
Windows/Linux observations, missing model assignments and negative phone evidence.
The [server resource](https://www.kaggle.com/datasets/manimaran2308/requests-source-provenance-replay-v1)
remains v12; the new local artifact and manuscript have not replaced it. Authored
code uses MIT licensing; research text, data and figures use CC BY 4.0. Resource
replay does not rerun native model inference or independently grade new repairs.

Namespace packages, extensions, plugins, concurrent source changes and unobserved
workers remain outside the measured scope. Source attribution establishes neither
issue relevance nor test adequacy. Small exposed samples, constructed faults,
unknown grades and unrepeated phone trials limit generalization. Private-scoring
equivalence, improved leaderboard performance and prize quality remain unresolved.
The workbench's practical purpose is to present those evidence limits to its user.

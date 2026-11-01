# Prospective study: Android budgets and verified Gemma coding tasks

Status: protocol and tools implemented; official tasks imported on October 3, and no
SWE outcome or award established. This is the primary Paper Track direction.

October 4 boundary update: a documentation search exposed reference fields from
the public task manifest to the research assistant. The original partition files
remain frozen but cannot establish an unexposed assistant-level holdout for later
candidate tuning. Public retests are development work; confirmatory assignments
need independent withholding and an audited agent-input boundary. See the explicit
exposure record in `reports/competition_focus/reference_exposure_20261004.json`.

## Contribution to test

Release a reproducible resource that pairs real repository issue validation with
native local-inference resource traces and ordinary-app interaction measurements.
Test whether stage-aware prediction under Android process/UID limits improves
verified issues resolved within a deadline at an acceptable foreground cost.
The current memory manager remains central. A benchmark/library is the initial
award target; a new algorithm and comparative improvement require separate proof.

## Source and splits

Use organizer public `tasks.jsonl`, repository snapshots, graphs and offline
dependencies after rules acceptance. Record the exact HARNESS_README, source
hash, model identity and runner revision. Do not substitute the Android DeepSeek
adaptation for the organizer harness. Import no hidden evaluation information.

`competition.study.prepare_study` produces outer leave-one-repository-out folds.
Each fold has a different repository for calibration and the remaining repositories
for fitting/development. Agent inputs allow only issue ID, repo, base commit,
problem statement and supplied hints. Reference fixes/tests are evaluator-only.
Mount evaluator files outside the agent sandbox; writing separate folders alone
does not enforce that boundary. Lock the method before inspecting any outer-fold
results. Adapters and resource fits are fresh per fold; no learned cross-fold state
or manual prompt changes may transfer held-out answers. Full-data retraining for
the hidden competition evaluation happens only after study selection.

The downloaded source has 129 tasks: FastAPI 67, Rich 48, Requests 13 and HTTPX 1.
One FastAPI reference (`fastapi_15661`) was automatically displayed by the Kaggle
preview during file acquisition. Declare it pre-exposed and exclude it before
study assignment, retaining its ID/reason in the manifest (128 eligible tasks).
The one-task HTTPX fold cannot support a population reliability claim. Repository
shift also breaks an automatic exchangeability assumption for conformal bounds;
report it as an out-of-distribution stress test, not guaranteed 95% coverage.

Freeze the complete assignment table, seed, source, prompt/tool configuration,
runtime, model digest, budgets and app workload before execution. A failed,
deferred, killed, unattempted or setup-failed assignment stays in the denominator.
Report task-level and session-level outcomes; serial requests from one session
are not independent repetitions. Reference tests first fail at the clean base;
then grader tests validate the generated patch at the same base. Preserve actual
commands, exit codes, patches and raw logs. Never count model prose as success.

## Runtime and foreground workloads

E2B runs on Android CPU using the pinned LiteRT-LM runtime, independently of
emulator GPU graphics. Begin with the actual installed Firefox/VLC/Luanti apps;
document the observed workload and app versions. Do not add artificial RAM filler
or replace real app outcomes with a controlled toy app. Physical S24 FE runs form
a separate stratum. Verify OS feature availability; API 37.2 budgets cannot be
assumed on the phone. Host-side patch grading must be reported separately from
device inference and device tool execution. Do not call a host-graded direct
patch generation experiment a fully native autonomous coding agent.

Collect task latency from assignment, queue wait, first token if observed,
generation/tool/validation time, sampled process/UID charges, budget changes,
global headroom, telemetry overhead and gaps, observed release/restore costs,
foreground input/frame outcomes, continuity on return, temperature and energy.
Missing data remain null. Screenshot content is transient; publish no account
content. Vision/audio interface checks are separate from correctness experiments.

## Baselines and forecast calibration

Compare no-AI foreground workload, tuned equally informed reactive admission,
measured-release barrier, current stage predictor, prediction without release-time
accounting, and the full candidate only after its components are implemented.
Keep model, limits, authority, apps, backend and device condition matched. Randomize
paired session order after warmup and thermal recovery. Freeze repetitions based
on pilot variance and a predeclared practically useful effect; do not stop on a
favorable six-response count. Include mzCache/Sereno where reproducible under
compatible hardware and backend, or document the unsupported comparison.

`memory.joint_resource_calibration` implements a standard one-sided split-conformal
wrapper using the maximum normalized residual across process peak, UID peak,
global depletion and duration. Predictor/scales must be fixed from independent
fit data. Calibration is frozen. Reused IDs reject; interrupted/missing cases
receive infinite scores rather than disappearing. Insufficient finite rank causes
abstention. A nominal 95% bound requires at least 19 untouched calibration cases
per applicable population even before censoring, dependency and shift issues.
Exchangeability of Android serial requests is unproved: call the output a
development bound unless the design supports the assumptions. Sampled bounds
never prove continuous safety. This wrapper is existing statistical methodology,
not a claim of a novel algorithm; it is currently offline, not deployed admission.

Primary outcome: independently validated issues resolved within the full deadline
per assigned issue. Co-primary foreground outcome: measured interaction quality
against the no-AI and reactive conditions. Report simultaneous sampled forecast
coverage, not three separate successes presented as one joint guarantee.
Analyze paired independent sessions and keep repositories/devices distinct.

## Competition roles

The paper targets the separate Google/Kaggle Paper Track, principally a reusable
resource, and is judged on novelty, quality, relevance, verifiability and clarity.
The 31B competition uses the exact required model and official sandbox/tool
interface; mobile E2B numbers cannot establish its leaderboard performance.
Run the official baseline before deciding whether adapters or graph policies help.
Publish a <=3,000-word final writeup only after evidence and claims are reconciled.

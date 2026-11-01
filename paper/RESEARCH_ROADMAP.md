# Research direction: cooperative local agents under application pressure

**Latest research decision:** mobile reclaim waiting and unload-failure accounting
already exist in Off Grid AI. The narrower proposed contribution is task-stage
peak/reclaim-delay prediction for deadline-aware admission under changing Android
process/UID budgets. A sampled-peak/deadline prototype is implemented; calibrated
reclaim-time forecasting and comparative benefit remain unverified. See
[the revised decision](../reports/mobile_novelty_decision_20261001.md) for the
direct counterexample, evidence boundaries and rejection tests.

Status: development prototype and research hypothesis, updated October 1, 2026. No novelty, benchmark victory or publication
is established. Native LiteRT-LM Gemma E2B now passes tool and actual Settings
vision checks on the Android 17 emulator. An experimental idle-residency controller
is connected to its lifecycle; real-app mechanism pilots have started, including
a retained foreground-setup failure. This is not a completed comparative benchmark.
The S24 FE has not supplied native inference measurements.

The newly proposed intent/workflow orchestration direction was assessed in
[`workflow_orchestration_novelty_assessment.md`](../reports/workflow_orchestration_novelty_assessment.md).
The recommendation is a focused cooperative prototype with originality still
open. The assessment screens 18 works; it is not an exhaustive systematic review.
Workflow graphs, predictive prefetch, prediction-error handling and system/app
coordination all have prior art. The additional hypothesis is whether forecasting
upcoming stages improves this project's resource/progress decisions under measured
foreground-app constraints. Do not claim a new whole-OS scheduler from the diagram.

## Claim worth testing

Can a local multimodal agent complete more verified tasks within a fixed time
budget while keeping foreground apps responsive, by jointly deciding when to
infer, how much memory to reserve, and how to preserve and revalidate task progress?

The proposed contribution is a measured joint policy for an ordinary Android
application: pressure-aware resource admission, bounded multimodal perception,
and recovery from observed tool effects when the surrounding apps cannot be
rolled back. It should operate without modifying the kernel or force-stopping
other apps. Those properties alone do not establish novelty. The contribution
must be the policy, its demonstrated incremental benefit, and its reproducible
evaluation against close alternatives.

## Closest prior art and the boundary of our claim

| Work | Relevant overlap | Required distinction or comparison |
|---|---|---|
| [FlexServe](https://arxiv.org/html/2603.09046v3), 2026 preprint | Agent-workflow model/KV prefetch; cooperative memory | Workflow-aware prefetch alone is not novel. |
| [KVFlow](https://arxiv.org/abs/2507.07400), 2025, and [PBKV](https://arxiv.org/abs/2605.06472), 2026 | Graph-guided and dynamic predicted workflow KV policies | Forecasts and uncertainty handling already exist; compare compatible policy adaptations. |
| [Pythia](https://arxiv.org/abs/2604.25899), 2026 | Workflow-semantic agent serving | A workflow-informed serving interface alone is not a new contribution. |
| [NestDNN](https://arxiv.org/abs/1810.10090), MobiCom 2018, and [NeuOS](https://www.usenix.org/conference/atc20/presentation/bateni), USENIX ATC 2020 | Mobile multi-tenant inference and cross-layer multi-DNN coordination | Avoid claiming that resource coordination began with LLMs. |
| [mzCache](https://arxiv.org/html/2609.01338v1), MobiCom 2026 | Android weight/KV eviction and restoration; application pressure callbacks; no kernel modification | Its `evict(size)` interface receives the release amount externally. Test a task-aware policy above a capable backend; root-free operation is not a distinction. |
| [AgentRM](https://arxiv.org/html/2603.13110v1), 2026 preprint | Scheduling, context compaction and hibernation | Generic scheduling plus checkpoints is already covered. Its evaluation describes simulated workloads; our intended evidence is native multimodal inference and real foreground apps. This does not by itself prove a novel algorithm. |
| [Crab](https://arxiv.org/html/2604.28138v1), 2026 preprint | Aligning agent turns with OS-side recovery state | Distinguish observing/reconciling unmodified phone apps from restoring agent sandboxes. Do not claim semantic checkpointing is new. |
| [AgentRewind](https://arxiv.org/html/2608.14380v1), 2026 preprint | Aligned agent/environment checkpoints | Its workspace recovery boundary excludes external service/runtime rollback. Specify our limited evidence boundary and test uncertain outcomes, rather than promise arbitrary app rollback. |
| [MemGUI-Bench](https://arxiv.org/abs/2602.06075), 2026 | Mobile GUI memory evaluation | Use compatible published tasks where possible; add actual resource pressure and foreground measurements. A new benchmark must add those measurements, not rename GUI memory tasks. |
| [Context-Folding](https://arxiv.org/abs/2510.11967), 2025 | Compact agent trajectories for long tasks | Compare task-evidence preservation with simple truncation/summary. A prompt-only approximation is not a reproduction of its trained method. |
| [TierKV](https://arxiv.org/abs/2609.21172), September 2026 preprint | Predictive multi-tier KV placement, mobile text/vision/audio | Neither predicting before allocation nor multimodal mobile memory management alone is novel. Compare the specific decision algorithm and agent/app outcomes. |
| [NeuroPrefetcher](https://arxiv.org/abs/2608.22643), August 2026 preprint | Predictive sparse weight fetching from storage | Predicting and prefetching cold weights already has prior art. A cost envelope is engineering groundwork rather than a new weight predictor. |
| [AppFlow](https://arxiv.org/abs/2603.17259), MobiCom 2026 | System-wide app launch/memory scheduling | Our intended deployment avoids framework/kernel changes. Ordinary app launch optimization is not an original claim. |
| [PowerInfer-2](https://arxiv.org/abs/2406.06282) and [LLM in a flash](https://arxiv.org/abs/2312.11514) | Smartphone/flash-aware inference | Keep backend optimizations separate from agent policy. Different devices, models and published speedups cannot be compared directly with ours. |

This is a focused literature assessment, not proof that no other system implements
the combination. Recheck related work before freezing claims or submitting.

The owner's task-analyzer/predictor/prefetch-reserve-evict/verify/update diagram
uses established concepts. `reports/resource_prediction_novelty_assessment.md`
records that finding. A standalone predictor draft and eight unit tests exist,
but it is not connected to the runtime and has no real calibration profiles.
The resource/progress policy remains a hypothesis. Do not claim uniqueness from
the diagram, root-free deployment, screenshot deletion, or use of Gemma alone.

## Three engineering contributions to develop

1. **Predict request cost and use foreground feedback.** Sample actual peak
   allocations for cold/warm text, vision and audio requests, conditioned on model
   digest, backend, context/output limits and input size. Learn conservative cost
   estimates and test their coverage on held-out sessions. Include weights only
   when not resident. Check predicted incremental cost plus reserve before
   admission; use measured frame/startup deadlines and memory pressure to decide
   whether to defer or release owned runtime resources. A reserve rule cannot
   guarantee safety against arbitrary concurrent allocations. Report prediction
   errors, reserve violations, and cancellation/release latency.
2. **Persist and reconcile verified progress.** At tool boundaries, retain the
   goal, constraints, completed/uncertain operations, observations with timestamps,
   and the next action. For coding, include base revision, actual diff, file hashes
   and test exit status. Separate `prepared`, `dispatched`, `observed` and
   `uncertain` states. After interruption, inspect the current app/repository
   before planning another action. Do not replay an uncertain non-idempotent
   action automatically. An intent acknowledgment is not observed completion;
   no general exactly-once guarantee is possible without app support.
3. **Bound perception using evidence validity.** Keep screenshots/audio ephemeral,
   persist compact factual observations with provenance, and invalidate them when
   the relevant page/state changes. Request a fresh image when accessibility lacks
   the evidence needed for the next action. Measure vision-call count, memory
   peaks, stale-evidence errors and task correctness. Pixel-hash deduplication and
   deleting screenshots alone are implementation hygiene, not a paper contribution.

Yield at a completed tool boundary when feasible. If pressure forces interruption
mid-request, cancel using a verified backend mechanism and retain uncertain
operations for reconciliation. Releasing an HTTP connection or setting a timeout
does not prove the backend stopped. The current provider and mapping primitive
do not implement this entire lifecycle.

## Benchmark that can justify a stronger paper

Use one pinned E2B model, quantization, native runtime and input/task set across
conditions. E2B text/image/audio inputs must run on the device; Android TTS is a
separate output component. Verify backend-format compatibility instead of assuming
a GGUF can be loaded by a runtime requiring another model format. Start with the
official [LiteRT-LM Android interface](https://developers.google.com/edge/litert-lm/android)
as a backend candidate, then verify model support, actual allocation/release and
cancellation. Do not label a host bridge as local phone inference.

The principal outcome is independently verified task completion within a fixed
budget, reported alongside foreground p95/tail latency, missed frame deadlines,
app reloads and background continuity. Show the quality/responsiveness tradeoff
curve, not only tokens/s or available RAM. Choose acceptable latency overhead and
task-quality margins after a variance pilot, freeze them before held-out testing,
and include deferred, failed and timed-out tasks in the assigned-task denominator.
Separate queue wait, inference, tool execution and recovery time.

Run these conditions:

- No-AI foreground workload to establish the device/app reference.
- Unchanged native inference with ordinary mmap and fixed context.
- Context cap only, admission/release only, and the existing combined threshold policy.
- Progress persistence without resource feedback.
- Resource feedback without progress persistence/reconciliation.
- Full proposed policy, then remove cost prediction and evidence invalidation separately.
- Compatible prior backend/policies when actually reproducible. Label policy
  adaptations and hardware limitations; they are not full reproductions.

Use actual browser/editor/media applications, disposable test data and recorded
action sequences. Keep an editor draft and media playback active during agent
tasks, then verify continuity by observed state. Vary actual tabs and workload
levels gradually. Add repository-repair/documentation tasks with independent
validation so the study is relevant to agentic software engineering. Reading a
build error screenshot, inspecting source, applying a patch and running tests is
one useful workflow; shopping/typing remains a functional prerequisite.

Real-app sessions are the main experiment. Selected interruption points in the
same apps provide a separate mechanism test: before dispatch, after an action
but before acknowledgment, and after observed completion. They test recovery
correctness without manufacturing task outcomes. Include asynchronous page
changes and background work during the pause. Preserve uncertainty when an
operation has no reliable validator.

Randomize condition order in paired sessions and hold model/app versions,
context/output settings, workload inputs and charging/thermal state comparable.
Select repetitions from pilot variance, then freeze the plan. Correlated telemetry
samples are not independent trials. Report paired effects and uncertainty at the
session/task level, monitor overhead, and retain all failures. One S24 FE supports
a device-specific finding; recruit another device before claiming broad hardware
generalization. Emulator results do not substitute for phone energy or UFS tests.

Do not compare our E2B/S24 FE numbers against mzCache's published Qwen/EXAONE on
different 12 GB phones and claim a speedup. A direct superiority claim needs a
common supported model/device/runtime and matched workloads. A complementary
policy with useful gains over strong baselines can still be a valuable result.

## Implementation order and stop conditions

If proceeding with the workflow extension, first record development traces of
actual stage transitions and request peaks. Predict only from intent, current
state and past observations available at decision time. Establish a history-based
workflow policy and a runtime-state-only policy with equal backend capabilities;
then test whether the new forecast adds value. Keep a future-trace oracle separate
as an offline bound. Measure wasted prefetch and its foreground cost, including
branch mistakes and cancellations. Add this extension only after native inference
and reliable completion validation work; the existing uncalibrated draft remains
inactive during this assessment.

1. Integrate and prove the native multimodal backend. Verify text, screenshot and
   audio generation/transcription on the S24 FE, and map actual allocations.
2. Resolve the existing final-response failure; observe task state separately from
   the harness stop reason. Establish a usable fixed-policy baseline first.
3. Add durable progress, uncertainty states and independent validators. Test
   interruption/resume before coupling them to pressure signals.
4. Collect real-app request peaks and foreground traces. Fit the admission
   predictor only on development sessions; test the full policy on held-out ones.
5. Run ablations and compatible prior comparisons. Publish code, version/hash
   manifests, nonprivate raw records and replay notebooks.
6. Write the final claim from observed results. If gains are small, unstable or
   quality regresses beyond the frozen margin, report that outcome and refine the
   policy instead of selecting favorable scenarios.

The 31B main competition is a separate environment: use its exact required model
and actual organizer harness, measure resolved patches within its budget, and
transfer only the checkpoint/tool-policy parts its APIs support. Android memory
hooks are not assumed available. No adapter training or official baseline has
been completed. The paper does not need to claim main-event superiority.

## What would make the result influential

A reproducible demonstration that an ordinary 8 GB phone can sustain useful local
multimodal developer tasks while preserving other applications, with a clearly
explained policy and meaningful gains over simple alternatives, would address a
practical deployment problem. Evidence of correct recovery and the failure cases
would strengthen it. Publication impact and competition awards cannot be promised;
they depend on the actual result, novelty assessment, evaluation and review.
# Selected controller experiment (October 1, 2026)

Proceed with the scoped hypothesis in
[the mobile residency research decision](../reports/mobile_residency_research_gap.md):
idle resource retention/admission under changing process/UID budgets, with measured
reload cost and independent post-release accounting. The narrower
[October 1 decision](../reports/mobile_novelty_decision_20261001.md) distinguishes
observed public-budget integration and implemented empirical peak admission from
unverified statistical calibration, reclaim-time forecasting and production benefits.
The Python reference, opt-in host adapter and
Kotlin/native lifecycle controller are executable. Real-app effectiveness and
deployable foreground sensing still require verification. Do not describe rental caching, app-aware eviction or
foreground protection individually as novel. The linked primary-source matrix
includes Sereno, MobiLoRA, mzCache, FlexServe, serverless retention, Linear Elastic
Caching, ThunderAgent, RAGCache, LLMS and approval-timescale KV retention. Keep older roadmap stages as context;
they do not certify a finished contribution or take priority over native E2B
measurement.

## Frozen-history development result (October 2 local date)

The [comparison decision](../reports/memory_predictor_comparison_decision.md)
supersedes any expectation of benefit from the current maximum-increment
predictor. In the completed real-game ABBA comparison, the reactive baseline
accepted 5/6 requests and experimental majority-fit deadline admission 0/6.
The experimental variant remains inactive by default. Changing budgets and
starting charges complicate peak transfer; conditional forecasting is a research
hypothesis requiring held-out calibration, not a completed novel algorithm.

Separate builds establish native cancellation acknowledgement and cooperative
model-verification interruption while the game runs. They reduce an observed
failure mode but establish no paper-level performance gain. Preserve them as
mechanism evidence, then validate the current asynchronous text/vision/audio
path and useful tasks on the S24 FE before making physical-device claims.

<!-- state-resident-status:start -->
## State-conditioned resident candidate (October 2 development)

The [predeclared protocol](../benchmarks/real_world/STATE_RESIDENT_PROTOCOL.md)
records the new resident-envelope rule, provisional neighborhood/margins and
bounded soft-threshold forecast risk. All compatible completed resident peaks
stay in the memory ceiling; state support gates elapsed-time transfer. Current
exhaustion and the global reserve still defer. Sampled pressure requests native
cancellation and rejects output. No OS budget is raised and no future quota is
credited. Sampling, initialization and cleanup do not provide hard guarantees.

The candidate is implemented, not an established novel or superior algorithm.
The [bracketed support protocol](../benchmarks/real_world/BRACKETED_RESIDENT_PROTOCOL.md)
addresses the real 1279/1281 MiB process-charge gap in the hardware local-only
comparison. Fallback needs at least three complete observations on each strict
side and nearby UID charges, transfers all completed peaks and the maximum
supporting duration, and cannot use a majority to override its deadline bound.
It synthesizes no intermediate measurements and rejects unsupported states.
Training episodes use 300-second deadlines; matched development evaluation uses
180 seconds and frozen history. They must not be pooled as one success score.
The earlier increment-envelope result remains reactive **5/6**, predictive **0/6**.

The confirmed-pressure iteration uses a provisional 8 MiB band and 1000 ms
confirmation, with at most 500 ms gaps; 128 MiB excess or global headroom below
800 MiB cancels immediately. Failed probes reset confirmation. Every measured
threshold crossing remains visible. These parameters are not calibrated optima.
The [hardware condition](../benchmarks/real_world/HARDWARE_GRAPHICS_PROTOCOL.md)
uses verified NVIDIA emulator graphics, while Gemma remains on CPU with two
threads. Desktop VRAM is not model memory. A measured-environment hash separates
profiles, and all earlier failed/unfinished histories remain retained.

Current-build completed/failed records:

| Run | Mode | Accepted / assigned | Foreground samples | Host abort |
|---|---|---:|---:|---|
| `20261002T080930808451` | NO_AI | 0/0 | 79/79 | False |
| `20261002T081108994616` | PREDICTIVE | 0/3 | 66/66 | False |
| `20261002T081229692685` | PREDICTIVE | 3/3 | 115/115 | False |
| `20261002T081452913350` | BUDGET_REACTIVE | 3/3 | 119/119 | False |
| `20261002T081725233409` | BUDGET_REACTIVE | 3/3 | 115/115 | False |
| `20261002T081950152738` | PREDICTIVE | 3/3 | 123/123 | False |

Comparison `20261002T054534933949` retains 5/6 planned episode records.
- BUDGET_REACTIVE: **3/6** planned responses; 1/2 usable matched episodes.
  Actual bracketed admissions: 0.
  process: 0/0 eligible completed sampled forecasts covered; 0/3079 enabled-threshold samples above the observed limit.
  uid: 0/0 eligible completed sampled forecasts covered; 0/3079 enabled-threshold samples above the observed limit.
- PREDICTIVE: **0/6** planned responses; 1/2 usable matched episodes.
  Actual bracketed admissions: 0.
  process: 0/0 eligible completed sampled forecasts covered; 0/2264 enabled-threshold samples above the observed limit.
  uid: 0/0 eligible completed sampled forecasts covered; 3/2264 enabled-threshold samples above the observed limit.

Comparison `20261002T074650471392` retains 6/6 planned episode records.
- BUDGET_REACTIVE: **6/6** planned responses; 2/2 usable matched episodes.
  Actual bracketed admissions: 0.
  process: 0/0 eligible completed sampled forecasts covered; 0/1573 enabled-threshold samples above the observed limit.
  uid: 0/0 eligible completed sampled forecasts covered; 0/1573 enabled-threshold samples above the observed limit.
- PREDICTIVE: **4/6** planned responses; 2/2 usable matched episodes.
  Actual bracketed admissions: 0.
  process: 4/4 eligible completed sampled forecasts covered; 0/1137 enabled-threshold samples above the observed limit.
  uid: 4/4 eligible completed sampled forecasts covered; 5/1137 enabled-threshold samples above the observed limit.

Comparison `20261002T080929346071` retains 6/6 planned episode records.
- BUDGET_REACTIVE: **6/6** planned responses; 2/2 usable matched episodes.
  Actual bracketed admissions: 0.
  process: 0/0 eligible completed sampled forecasts covered; 0/1246 enabled-threshold samples above the observed limit.
  uid: 0/0 eligible completed sampled forecasts covered; 0/1246 enabled-threshold samples above the observed limit.
- PREDICTIVE: **6/6** planned responses; 2/2 usable matched episodes.
  Actual bracketed admissions: 4.
  process: 6/6 eligible completed sampled forecasts covered; 0/1265 enabled-threshold samples above the observed limit.
  uid: 6/6 eligible completed sampled forecasts covered; 0/1265 enabled-threshold samples above the observed limit.

Predeclared training series (300 seconds per request, not the scored comparison):

- `20261002T064423069748`: **7/9** planned accepted; 8 attempted.
- `20261002T072932792155`: **0/9** planned accepted; 1 attempted.
- `20261002T073651969317`: **9/9** planned accepted; 9 attempted.

The host-recovery calibration seed includes every new event from its predeclared series, including any interruptions. Earlier series are not pooled into its result.

Answer semantics, touch responsiveness, asynchronous vision/audio and S24 FE behavior remain unverified. No all-criteria win, statistical superiority or 10/10 claim follows.

<!-- state-resident-status:end -->

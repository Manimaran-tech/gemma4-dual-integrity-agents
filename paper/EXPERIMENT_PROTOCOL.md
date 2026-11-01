# Real-device and coding-agent experiment protocol

This protocol describes work to perform, not completed experiments. The manuscript
is an implementation/protocol draft until the required observations exist. See
SWE_MEMORY_STUDY_PROTOCOL.md for the competition-focused prospective study.

## Primary hypotheses

H1: Coupling memory admission with bounded context reduces foreground latency
under a fixed local-model workload, without an unacceptable patch-success loss.
H2: Factual persistent task checkpoints reduce re-navigation cost after yielding
model memory, compared with context reduction or unloading alone.
Neither hypothesis is established by the current unit tests or host microbenchmark.

## Record before each session

Record physical model, serial, Android fingerprint, kernel, page size, RAM,
storage free space, runtime revision, model SHA256, quantization, GPU/CPU backend,
context/output limits, battery/charging state, temperature, network, permissions,
installed app versions, workload revision, and randomization seed. Record how
foreground/background services behave and keep the measurement overhead visible.
The S24 FE specifications currently come from the owner, not a recorded device run.

The Pixel AVD is a functional capacity test. Report its x86 host, Android image,
actual `/proc/meminfo` and `/data` sizes. Do not merge emulator, WSL, host-Ollama,
and phone trials in a single "S24 FE" aggregate.

## Runtime prerequisite

Native inference must actually run on the phone. LiteRT-LM 0.17.1 now executes
the pinned Gemma 4 E2B model on CPU inside the Android 17 emulator; retained runs
include native allocation and process/UID/global telemetry. The older placeholder
JNI mapping and host Ollama episodes are separate, inactive comparison histories.
The S24 FE native prerequisite is still pending: prove generation with that same
pinned model/quantization on the physical device, then verify where weights,
KV state, compute buffers and GPU copies reside. Connect eviction to those actual
allocations. Discarding a separate unused mapping is not an inference optimization.

## Baselines and ablations

`RESEARCH_ROADMAP.md` narrows the proposed contribution after checking AgentRM,
Crab, AgentRewind and mzCache. Generic context hibernation and semantic checkpointing
already have prior art. Add separate progress/reconciliation-only and resource-
feedback-only conditions before interpreting the full joint policy. Account for
queue wait, inference, tool execution and recovery. Show task success and app
responsiveness together rather than optimizing a single RAM or throughput figure.

Use the same model and workload for: no-AI app baseline; stock inference runtime;
context limit only; admission/unloading only; combined policy; combined policy with
and without factual checkpoints. Include plain runtime mmap as a strong baseline
where supported. Add zRAM/PSI policy signals only as a separately measured ablation.
Compare mzCache when reproducible on the selected platform, or clearly document
why that comparison cannot run. It manages weights as well as KV state.

Do not use global app trimming, force-stops, kernel knob changes or hidden cache
flushes to advantage one condition. Apply the same app resets and warmup state to
every condition. A later app-trim study would require its own explicit condition.

## Workloads

The next emulator uses `Pixel_10_Pro_Android17_S24FE_8GB`, Android 17/API 37 with
patched Google Play system-image revision 5, configured 8192 MiB RAM and 128 GB
userdata. Setup facts are in `reports/android17_setup_verification.json`. Account
login belongs to the owner; app evaluation starts after they confirm login.
Retain the earlier Android 15 episodes as a separate dataset.

Use actual browser, editor and media applications for the next functional/stress
pilot. Record installed versions and observed page state. Start a local media
playback and a disposable editor draft, then run real search/navigation/typing
tasks with the agent and switch back to check continuity. Escalate actual tab and
workload counts gradually, measuring both guest and inference-host memory. If
host admission defers a request, record the deferral as an outcome. Do not use
account messages, private documents or purchases as test targets. Capture fresh
screenshots in memory only when the page changes, then release their references
after the provider request. Store outcome/metric records without account content.

These real-app emulator checks establish functionality and failure modes. The
native S24 FE randomized study starts only after a verified on-device backend
exists; host-backed app survival is not evidence that the model fits phone RAM.

Start with a short reproducible sequence of browser/editor/media/background tasks.
Document actual actions and tab/data state; a package launch does not establish
"10 tabs", "4K streaming" or "8K camera recording". Expand to camera/game/video
editing only after verifying those app modes and collecting comparable trials.
Measure background-task continuity and reload behavior when switching back.

Pilot each condition to determine variance and feasible duration. Randomize
condition order in paired device/workload blocks; use separate sessions after
thermal recovery. Set repetition count using pilot variance and a practical effect
threshold. Freeze it before final held-out experiments. Preserve failed trials.

## Metrics and attribution

| Metric | Evidence required | What does not establish it |
|---|---|---|
| Resolved coding issue | Patch applied to a clean base and successful validation | Model says "done" |
| TTFT | Request-start and first visible streamed-token timestamps | Total generation time or a placeholder response |
| LMKD kill | Relevant system event with process identity and timestamp | PID disappearance alone |
| Foreground responsiveness | Perfetto/frame-deadline/startup traces | Available RAM alone |
| Memory cost | Time series of relevant process RSS/PSS, GPU/buffer and system values | Mapping virtual size |
| Physical zRAM use | `mm_stat` allocator-use field | `SwapTotal` or logical disksize |
| Energy | Validated meter/sensor, voltage-current integration, sampling and idle baseline | A constant assigned in code |
| Logical storage writes | Defined block counter and device-layer interpretation | Process `write_bytes` alone |
| NAND wear | Appropriate physical storage/controller evidence | Clean model mapping or logical sectors |

Missing or permission-denied metrics remain null with a reason. Avoid summing
device-mapper and underlying device counters: that double-counts the same I/O.
No measured zero is emitted when a measurement was unavailable. Restore/prefill
cost and unload/reload frequency belong in the policy's latency/energy accounting.

## Analysis

Publish raw trials, source/hash manifests, settings and exclusions. Report per-device
paired effects, median and tail latency, confidence intervals, task success and
timeouts. Do not hide failed or unattempted coding issues from the denominator.
Repeated identical synthetic values cannot establish variance or significance.
Bootstrap paired blocks (not individual correlated samples) when appropriate;
justify analysis and avoid multiple-ablation cherry-picking.

## Main competition study

Use the exact required 31B model and official harness. Freeze repository-disjoint
development and held-out issue sets before any SFT/RL. Compare the no-adapter
baseline, retrieval/checkpoints and then trained variants one at a time. Save
tool trajectories, model/template versions, adapters, patches, validation output,
wall time, central budget status, invalid calls and environment errors. Any
training data must have traceable origin, license and split membership.

The 8 GB RTX 3050 workstation has not been shown adequate for 31B post-training.
Use appropriately provisioned Kaggle/other compute after availability and rules
are confirmed. Do not label an E2B fine-tune as the competition-required model.

## Paper readiness gate

The official paper-track overview specifies a Kaggle writeup of at most 3,000
words, original/unpublished work, and equal weighting of novelty, quality,
relevance, verifiability and clarity. Recheck the full rules and organizer updates
before submission. Require real native phone inference,
real multitasking and held-out coding trials, honest ablations and prior-art
comparison. Claims must point to a raw record and analysis command. Mark remaining
designs as proposed. A compiled PDF and unit-test success do not establish novelty
or empirical effectiveness.

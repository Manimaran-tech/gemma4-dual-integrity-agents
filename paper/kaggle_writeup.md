# NeuralOS: Auditing Native Gemma Agents Under Android Memory Contention

*A development pilot and a protocol linking resource traces to independently graded coding work*

## Abstract

Mobile agents share memory with ordinary applications. Completing inference does not establish a correct software repair, a calibrated resource forecast or a responsive foreground app. We implement native Gemma 4 E2B inference, empirical stage admission, whole-engine residency control and durable evidence records. In an Android 17 emulator pilot alongside Luanti/Mineclonia, the declared predictive and reactive comparison arms each complete six resource probes. Joint process/UID/global forecast coverage is only three of six predictive trajectories, and predictive median provider latency is 160 ms higher. The predictive arm permits 128 MiB of forecast excess; a separate zero-allowance diagnostic completes zero of three. These observations support a failure-preserving audit, not policy superiority. We prepare native repository tools, exact patch export and independent host grading, then specify the evidence needed to evaluate coding success and foreground cost together. No mobile coding result or physical-phone measurement is established.

**Working draft, October 5, 2026.** The evaluated mobile evidence is a development resource pilot. Mobile coding evaluation and statistical calibration remain prospective. This document is not a final competition entry.

## Introduction

An offline coding agent must fit model weights, runtime buffers, conversational state and repository evidence into memory shared with the user's apps. Global free RAM, process charges, UID charges and deadlines describe different constraints. Android exposes app-memory budget measurements from API 37.2; unavailable measurements must remain unknown. Budget excess triggers reclamation and swap rather than an automatic process crash. [Android app-memory budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets).

Our research question is whether stage-aware admission improves independently validated issues resolved within a full workflow deadline while preserving foreground interaction quality. The candidate contribution has three evidence levels: an implemented audit/export stack, an observed separation between resource completion and joint forecast coverage, and a prospective coding-resource protocol. We have not established a new memory algorithm or evaluated a complete coding benchmark.

The mobile research model is E2B. The main competition uses `gemma-4-31b-it-qat-w4a16-ct` and scores repository patches. E2B emulator results cannot imply a 31B leaderboard score. [Main competition](https://www.kaggle.com/competitions/gemma-4-developer-agent).

## Methods

![NeuralOS architecture and evidence chain](<D:/AI OS (ANDRIOD)/paper/figures/neuralos_evidence_chain.png>)

*Figure 1. Implemented native tools/controller and export code are separated from the prepared grading path, retained resource-probe outcomes and prospective actual repairs. This is a local preview; the figure still needs a public Kaggle asset upload before publication.*

### Native execution and controller

Gemma 4 E2B runs on Android CPU through pinned LiteRT-LM 0.17.1 with two inference threads. Emulator graphics acceleration is separate from model execution. Desktop VRAM is not additional phone memory.

The controller serializes requests, pins active inference and retains or closes a whole idle engine. Failed close retains a pending state; fresh headroom is measured before admitting another request. Closing a handle does not prove physical-page reclamation. Weight-block paging, fine-grained KV eviction and KV persistence across release are not implemented.

The empirical predictor separates modality, context/output limits, cold/warm state and starting-charge neighborhoods. Its experimental bracketed variant requires measured support on both sides of an unsupported starting process charge. Compatible observed peaks remain in the envelope; it does not synthesize intermediate measurements. Retention prices and prediction margins are provisional heuristics, not learned optimal constants or coverage guarantees.

For observed process/UID budget $B_j$, current charge $U_j$ and forecast increase $\widehat\Delta_j$, strict admission requires $U_j+\widehat\Delta_j\le B_j$. Global headroom $A$, predicted depletion $\widehat G$ and reserve $R$ require $A-\widehat G\ge R$. Predicted duration plus wait must fit the remaining deadline. Scope budgets are checked separately, never summed. Missing required evidence causes deferment. Development soft-excess and majority-duration options relax this rule and are declared explicitly.

### Repository generation and independent grading

An API-26+ prototype offers bounded source listing, reads, searches and hash-checked edits in a dedicated repository copy. Grading paths are read-only. A native-provider guard rejects host-inference fallback. Byte-preserving exports bind changes and deletions to the base inventory and permit unchanged patch reconstruction on the host. The device supplies no Python interpreter or test runner. This is native generation with host grading, not a fully native development stack.

The source/APK-bound episode runner and independent CPU grading notebook are prepared. Reactive and predictive evaluation configurations now share an 800-MiB reserve and zero forecast soft-excess allowance. Frozen evaluation blocks predictor and release-delay learning. These changes have produced no new device comparison or independently graded mobile repair.

An independent Kaggle CPU audit now matches all 524 files in the prepared Rich development input to the official grader's starting source, with no differing bytes or missing files. Eight transported checkpoints are hash-verified and the comparison is recomputed during reconciliation. The Python 3.12.13 worker uses no accelerator and runs no inference or tests. Both inventories exclude `.git`; file-permission equivalence, private-scoring equivalence and task correctness remain unestablished. Earlier wheel-installation and namespace failures remain retained. Complete-import receipts and interruption recovery can preserve actual edits for grading; they cannot prove generation completion or a met deadline. On-device recovery remains untested.

### Evidence chain

Each assignment retains identity, source/model/runtime hashes, configuration, measured state, tool/model journals, exports and grading provenance. Starts persist before native execution; completions persist before learning. Interrupted or capped records remain explicit. Process/UID charges are not relabeled as PSS or model-attributed weight allocations. Measurements are sampled and getters are non-atomic, so retained peaks do not establish continuous safety.

The repository field `whole_app_pss_mib` measures current-process PSS, not summed UID usage. The phone's budget capability remains unknown. Strict prediction defers when own-budget getters are unavailable; observe-only compatibility runs cannot establish process/UID compliance. Observed disabled limits are a separate stratum from unsupported getters and positive limits.

## Experiments and observed results

### Real-app emulator pilot

The retained comparison is `20261002T080929346071`, using source APK build `20261002T080650069096`, an 8-GB Android 17 emulator, 2,048 context tokens, 128 requested output tokens and 180-second request deadlines. Luanti/Mineclonia supplies an actual game workload. The prompts are resource probes, not repository issues with correctness tests.

The declared comparison consists of two sessions per arm, each assigning three probes, in A-B-B-A order. Stage history is seeded from nine earlier cold-text observations and frozen during comparison. This is development evaluation after prior tuning. Sessions were not independently randomized; game position, cache, mutable budgets and host load were not reset.

| Observed quantity | Predictive comparison arm | Reactive comparison arm |
| --- | ---: | ---: |
| Completed resource probes | 6/6 | 6/6 |
| Independent sessions | 2 | 2 |
| Median provider latency (ms) | 20,894.5 | 20,734.5 |
| Expected foreground-package samples | 238/238 | 234/234 |
| Process forecast coverage | 6/6 | Unavailable |
| UID forecast coverage | 6/6 | Unavailable |
| Global forecast coverage | 3/6 | Unavailable |
| Joint process/UID/global coverage | 3/6 | Unavailable |
| Forecast soft-excess allowance (MiB) | 128 | 0 |

Forecast coverage concerns completed sampled trajectories. The reactive arm emits no forecast, so its coverage is unavailable. Foreground-package presence does not establish input latency, frame quality or user responsiveness. Serial requests and memory samples are not independent repetitions.

The full six-session plan also retains a no-AI reference and a zero-allowance predictive diagnostic. The diagnostic completes **0/3**: all three probes defer for predicted process-peak headroom. Its assignments remain recorded separately because it uses a different policy allowance. The table's 6/6 denominators describe the declared comparison arms, not every predictive assignment.

Four predictive requests use bracketed support. Global depletion is underestimated by up to 105 MiB, while minimum sampled predictive available memory remains 4,237 MiB. Neither comparison arm exceeds its enabled soft threshold in retained samples. Successful resource completion can therefore coexist with forecast error. Predictive median latency is 160 ms higher; two sessions per arm and unmatched allowances support no causal or statistically reliable gain.

The nine seed observations are all cold text; three have changing budgets. They are not independent fit/calibration data and do not calibrate the newer 4,096-maximum-context/512-requested-output repository path. Native multimodal interface checks elsewhere in the history remain separate from this denominator. Live multimodal semantics, energy and physical S24 FE results remain unmeasured. USB testing is deferred.

### Separate 31B development evidence

The organizer pipeline executed with the required 31B model on four Kaggle L4 GPUs, swegemma 0.2.7 and vLLM 0.19.1. A pre-exposed smoke issue produced a retained patch but resolved 0/1. A public two-issue comparison printed 0/2 for both baseline and contract-cleanup candidate; full patches/traces were missing on worker recovery. These counts establish no correctness improvement or mobile-policy result.

Independent Rich fixture controls show clean-base failure and reference success. Requests' unchanged base and reference both pass in the repaired supplemental environment, so that fixture cannot demonstrate repair there. Reference passes are environment controls, never generated fixes. Supplemental compatibility does not establish private-grader equivalence. Interrupted/canceled attempts with no grades remain unresolved.

The later saved version-7 Rich retry completed one assignment per arm: baseline 0/1 verified repairs with a 1,255-byte patch, and `source_only_v3` 0/1 with an empty patch. Both report test exit code -1. All 22 listed artifacts reconcile, including two full model/tool traces; retained log and test-output files are empty, so full diagnostic text is unavailable. The candidate trace records at least 16,385 input tokens plus a 16,384-token output reserve exceeding its 32,768-token context window. No assertion failure is inferred from exit -1 without grader text. This public one-case development comparison establishes no gain or leaderboard score; the earlier 0/2 and missing-trace results remain separate.

A subsequent frozen 31B diagnostic reduced the output cap to 8,192 and retained two Rich issues with completed clean-base failure/reference-pass controls. Source-only and tool-path instruction variants each resolved **1/2**, producing the same 609-byte source patch on Rich2725; both failed Rich4079 with official exit 1. All four assignments, full traces, official receipts and 15 chronological checkpoint transfers reconcile. Selection followed public fixture controls and prior reference exposure; these issues are development material. The tie establishes no instruction benefit, general repair rate or mobile transfer. No protected test edits appear in the successful patch. [Retained private Kaggle run](https://www.kaggle.com/code/manimaran2308/neuralswe-31b-fixture-qualified-cap8192?scriptVersionId=355185909).

A separate budgeted source-only transfer with compaction interval five also resolved **1/2** on those exposed cases. Both reached the 50-tool limit. Rich2725 produced a 1,099-byte production patch; Rich4079 added reproduction scripts without repairing production code and failed validation. Both full traces and official receipts reconcile. Budget and compaction settings changed together, so this establishes neither a causal compaction benefit nor a candidate improvement. A separately frozen four-case Requests/FastAPI CPU panel completed all eight clean/reference controls: one base already passed, and three references remained unverified. No case qualified, and no replacements were selected. Reference controls are environment checks, not generated repairs. [Private transfer run](https://www.kaggle.com/code/manimaran2308/neuralswe-31b-source-budget-compaction5?scriptVersionId=355257901).

## Prospective coding-resource evaluation

### Correctness, leakage and denominators

The proposed resource joins native generation traces, independently graded repository patches and ordinary-app interaction measurements. Frozen repository-disjoint partition tooling exists, but the organizer public pool was exposed to the research assistant. Public retests are development work. Confirmatory assignments require independent withholding and audited input boundaries; creating separate agent/evaluator folders alone is insufficient.

Agent inputs contain only ID, repository, base commit, problem, supplied hints and the genuine source. Reference fixes and grading tests stay outside agent mounts. Freeze assignments, configurations, splits, workload, session order and repetitions before execution. Preserve failed imports, deferrals, kills and unattempted assignments. Source-byte equality is established for the prepared Rich input; each new task requires its own audit and fresh clean-base/reference controls before interpreting candidate grades.

The primary endpoint is independently validated repairs within the full workflow deadline per assigned issue. A full clock includes queueing, import, generation, tools, export, transport and grading. The current native runner times import through generation/export, so it does not establish that full endpoint.

For $N$ assignments, $k$ reconciled successful repairs and $u$ unresolved correctness/timing outcomes, report $k/N$ and the identification interval $[k/N,(k+u)/N]$. This describes missing information, not statistical confidence. Known deferrals or deadline overruns are non-successes; absent grades after worker interruption are unresolved, not observed incorrect patches. Report failure reasons independently of the binary endpoint.

Pair independent sessions, randomize order after warmup/thermal recovery, and keep repositories and devices in separate strata. Predeclare a useful repair-rate improvement and foreground noninferiority margins. Choose repetitions using a separate variance pilot and report uncertainty for repair differences and measured input/frame costs. Individual serial requests cannot supply independent sample size. Compare no-AI, equally informed reactive admission, measured-release barriers and implemented prediction variants with identical model, authority, risk limits and starting residency.

### Calibration and foreground cost

An offline standard one-sided split-conformal wrapper uses the maximum normalized residual across process peak, UID peak, global depletion and duration. Predictor/scales must be fixed using independent fit data; calibration is frozen. Reused identifiers reject evaluation. Missing/interrupted cases receive infinite scores and insufficient finite rank causes abstention. [Conformal prediction](https://arxiv.org/abs/2107.07511).

Nine calibration cases cannot provide a finite nominal 95% correction: the required rank is ten. Nineteen fresh cases are only the minimum rank condition. Serial dependence, budget drift and repository/device shift require separate assessment. The wrapper is not integrated into Android admission and yields no per-request safety guarantee. [Adaptive conformal inference](https://proceedings.neurips.cc/paper/2021/hash/0d441de75945e5acbc865406fc9a2559-Abstract.html).

Actual Firefox, VLC and Luanti workloads need measured interaction/frame outcomes, continuity, telemetry overhead, temperature and energy. Physical S24 FE data form a separate stratum; API 37.2 availability must be observed on that device. Vision/voice tasks need semantic oracles and screenshot-disposal evidence. These experiments remain prospective.

## Related work and relevance

[mzCache](https://arxiv.org/abs/2609.01338) already handles Android weight/KV eviction and restoration during multitasking; its fine-grained mechanism exceeds our backend. [Sereno](https://www.usenix.org/conference/osdi26/presentation/xin) protects foreground QoS through bandwidth yielding. [MemSpec](https://arxiv.org/abs/2608.10362) combines prediction and resident draft management on edge devices. [AgentRM](https://arxiv.org/abs/2603.13110), [Crab](https://arxiv.org/abs/2604.28138) and [AgentRewind](https://arxiv.org/abs/2608.14380) address resource scheduling and recoverable agent state. Moving established ideas to an 8-GB phone is insufficient novelty.

[Android Bench](https://github.com/android-bench/android-bench/blob/main/docs/tech_report.md) and [SWE-Bench Mobile](https://arxiv.org/abs/2602.09540) evaluate mobile-app development; public [Gemma E2B Android benchmarks](https://github.com/blyzai/lexa-edge-benchmarks) also exist. Our narrower hypothesis is that joining native execution, memory forecasting, independent patch correctness and ordinary-app cost yields a useful reusable resource. The required direct coding evidence is absent, and inspected literature cannot prove firstness. Published gains on other devices are not comparisons with this emulator.

The Paper Track equally scores novelty, quality, relevance, verifiability and clarity; Best New Resource is an explicit category. This framing is relevant but establishes neither award competitiveness nor novelty. [Official Paper Track](https://www.kaggle.com/competitions/gemma-4-developer-agent-paper/overview).

## Reproducibility and limitations

Run `python paper/replay_pilot_evidence.py --output paper/pilot_evidence_replay.json` from the repository. The replay checks frozen pins and 128 retained inventory files across all six sessions. It reconstructs completion/latency from raw results and replays forecast coverage from pinned existing analysis; it does not independently reimplement native telemetry analysis. The original comparison, failed diagnostic and null mobile-coding/phone outcomes are preserved. Replay source pins were created during this continuation, not original preregistration.

Frozen notebook 15 retains its locally verified ZIP-input replay. Kaggle automatically extracts Dataset ZIP uploads, so separate notebook `16_paper_extracted_resource_guarded_replay.ipynb` verifies all **138** extracted selected files before staging or executing the same replay code. A same-size code mutation was rejected before execution. Its private CPU Kaggle version 2 completed in **27.3 seconds**, reproducing all six sessions and retained pilot values. Downloaded JSON is semantically identical with only Windows CRLF versus Linux LF differences; CSV is byte-identical. Five output members and their hashes reconcile. The scoped resource and notebook are private pending release review; verifiability for outside readers still requires public assets and usage instructions. [Actual Kaggle replay](https://www.kaggle.com/code/manimaran2308/neuralos-paper-resource-guarded-replay?scriptVersionId=355251050). The separate starting-source proof remains in `reports/kaggle_runs/20261004_mobile_source_audit_retry2/reconciled/audit_reconciliation.json`.

The existing `paper/main.tex` source remains the detailed manuscript. Three built-in compilation attempts failed with `Unable to find standard directories for platform`; the later source-audit update has not been compiled and no verified PDF exists. Before final delivery we need native coding episodes, compatible independent grades, matched locked evaluation, genuine foreground/energy evidence, a usable licensed release and public resource links. Current measurements support an auditable development finding; the proposed coding benchmark and controller benefit remain unestablished.

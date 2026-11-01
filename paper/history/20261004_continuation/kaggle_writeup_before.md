# NeuralOS: Auditing Memory-Predicted Local Gemma Agents Under Android Multitasking

Mobile agents share memory with ordinary applications. A completed inference request does not establish either a correct task result or a calibrated memory forecast. We implement native Gemma 4 E2B inference, empirical stage admission, whole-engine residency control and durable measurement records. A retained Android 17 emulator pilot runs inference alongside a real Luanti game workload. Both predictive and reactive policies complete six of six assigned text requests. The predictor covers sampled process and UID peaks in all six, but covers all three memory scopes jointly in only three. Provider latency is slightly higher than the reactive baseline, and a declared soft-headroom allowance prevents interpreting completion as strict forecast admission. These development results motivate an auditable resource joining memory traces, ordinary-app outcomes and independently verified software patches. We implement repository-disjoint study preparation and a standard joint calibration wrapper with explicit abstention. The prospective mobile software-engineering study has no measured outcomes yet.

**Draft status:** Evidence-backed development pilot and prospective resource design. Physical-phone evaluation, verified coding outcomes, held-out policy benefit and a scored competition submission remain pending. A single excluded 31B development smoke and a supplementary public development comparison have run. No comparative superiority or new statistical theorem is claimed.


## Problem and research question

An on-device coding agent needs model weights, runtime buffers, conversational state and repository evidence while users browse, play media or run a game. Free RAM alone does not characterize this competition. Own-process charges, UID charges, global headroom and task deadlines have distinct meanings. Android app memory budgets provide public process/UID measurements in API 37.2; unsupported APIs must not silently become zero usage [budget](https://developer.android.com/topic/performance/memory/app-memory-budgets).

Our question is whether stage-aware admission can increase independently validated issues resolved within a deadline while preserving ordinary-app interaction quality. A resource request finishing is only an intermediate event. It must not be counted as a correct software patch, a responsive foreground app, or a safe continuous memory trajectory.

We keep two settings separate. Native E2B is the mobile research model. The main competition requires `gemma-4-31b-it-qat-w4a16-ct` and evaluates repository patches [competition](https://www.kaggle.com/competitions/gemma-4-developer-agent). E2B emulator results cannot imply a 31B leaderboard score. Desktop VRAM is not additional model RAM on the target phone.


## Implemented system


### Native execution and measurement

Gemma 4 E2B runs on Android CPU through pinned LiteRT-LM 0.17.1. Emulator graphics use hardware acceleration separately. Earlier host-Ollama episodes remain a separate history and are not native mobile measurements. The older disconnected mapping primitive is not presented as an inference optimization.

Each request has a durable attempt identifier and start/completion records. Records identify model/runtime, configuration, modality, residency state, sampled charges, headroom and timing. Missing completions, capped traces and incomplete telemetry remain explicit. Immutable inventories bind retained files to SHA256 hashes; replay verifies them before computing results. Unit-test fixtures are synthetic schema or mathematical checks, never empirical measurements.

Process/UID budget charges are not relabeled as PSS or model-attributed weight allocation. Global available memory is independently observed. Budget changes are recorded rather than treated as a fixed capacity. A closed engine handle does not prove physical pages have been reclaimed; admission re-samples headroom.


### Residency and empirical stage admission

An API-26+ repository prototype supplies bounded file observation and hash-checked editing in a dedicated source copy. Grading paths are read-only; exports bind changed bytes and deletions to the base inventory. A native-provider guard rejects host-inference fallback. The episode runner records actual model/tool responses and sampled memory alongside an already-running real app, then exports a candidate for independent host grading. It has no device Python interpreter. The app and instrumentation build, but no repository episode has executed yet. Its larger maximum context and file-tool authority do not inherit the earlier text pilot's calibration or outcomes.

An independent CPU grading notebook is prepared with clean-base and reference controls. New diagnostic settings match reactive and predictive reserves and allow zero forecast excess. Frozen evaluation also blocks release-delay learning. These implementation changes have not produced a new device comparison or verified coding result.

The controller serializes requests and pins active inference. Idle policies can retain or close a whole engine. Release has a pending state: failed close cannot permit optimistic handle reuse or memory credit. The backend does not implement fine-grained weight/KV eviction or KV persistence across engine release.

Idle rental policies compare accumulated measured retention cost, including an allowance for observed close delay, with an initialization-cost envelope. This is a heuristic adaptation of existing cost-based retention ideas. Its prices are configuration parameters, not learned optimal constants or a transferred competitive guarantee. Active-pressure guards are separate from idle retention.

The native stage predictor uses empirical sampled peaks and duration envelopes. Configuration and modality separate profiles; cold and warm requests do not borrow observations automatically. A starting-charge neighborhood limits local transfer. The experimental bracketed variant requires observed support on both sides when direct neighbors are insufficient. Memory envelopes retain compatible observed resident peaks rather than selecting only the lowest local peaks. Starting charges are measured state, not allocations attributed to weights.

For process/UID scope $j$, let $B_j$ denote its observed budget, $U_j$ its current charge and $\widehat\Delta_j$ the predicted increase. Strict admission requires $$
\begin{aligned}
 U_j+\widehat\Delta_j &\le B_j,\\
 A-\widehat G &\ge R,\\
 \widehat T+\widehat L &\le D.
\end{aligned}
$$ Here $A$ is global available memory, $\widehat G$ predicted depletion, $R$ a configured reserve, $\widehat T$ stage duration, $\widehat L$ additional wait and
$D$ remaining deadline. Enabled scope constraints are checked separately; budgets are not summed. Missing required observations cause deferment.

Development variants expose explicit risk settings: historical-majority duration admission and a bounded forecast excess over soft headroom. They are not strict forms of the equations above. Current-violation checks and active guards remain necessary, but do not guarantee that all unsampled peaks obey a limit.


## Retained real-app development pilot

The audited comparison is `20261002T080929346071`, source APK build `20261002T080650069096`. It uses the configured 8 GB Android 17 emulator, CPU inference with two threads, 2,048 context tokens, 128 output tokens and 180-second request deadlines. Luanti/Mineclonia is the actual foreground workload; this is not a toy application or artificial RAM filler. Text requests in this comparison are resource probes, not verified repository issues.

Two episodes per policy assign three requests each. Policy order is Aâ€“Bâ€“Bâ€“A; this small development comparison is not an independently randomized confirmatory study. The predictor's stage-peak history is seeded from an earlier collection and frozen within the comparison. Earlier failed variants, including a zero-of-six predictor outcome, remain in the evidence history rather than being removed.


| Observed quantity | Predictive | Reactive |
| --- | --- | --- |
| Completed resource requests | 6/6 | 6/6 |
| Median provider latency (ms) | 20,894.5 | 20,734.5 |
| Expected foreground samples | 238/238 | 234/234 |
| Process forecast coverage | 6/6 | â€“ |
| UID forecast coverage | 6/6 | â€“ |
| Global forecast coverage | 3/6 | â€“ |
| Joint three-scope coverage | 3/6 | â€“ |

Replay of retained development evidence. Coverage concerns sampled completed trajectories. A reactive policy emits no forecast, so its coverage is unavailable, not zero. Foreground presence is not interaction responsiveness.


The predictor permits up to 128 MiB of forecast excess over observed soft process/UID headroom; reactive admission has no forecast allowance. Both retain current guards. Four predictive requests use bracketed support. These differing admission rules prevent claiming a strict-headroom policy improvement from the six-response target. Neither policy has observed enabled-scope threshold excess in its retained samples. This is sampled evidence, not continuous safety.

Predictive global depletion is underestimated by up to 105 MiB, although the minimum sampled available memory remains 4,237 MiB. Thus all requests can finish while the global forecast still fails. Predictive median provider latency is 160 ms higher than reactive. The pilot establishes implementation behavior and an audit failure mode, not faster inference or superiority over published systems.

The seed collection has nine starts and nine finishes. All nine eligible cases are cold text requests; three have changing budgets. It supplies neither warm nor multimodal calibration and is not an independent fit/calibration split. Serial requests and sampled time points are not independent experimental units.

Native vision/audio interface checks and actual Settings typing episodes exist elsewhere in the retained history, including failures. They are not added to this text comparison's denominator. Generated speech inputs establish interface functionality, not spontaneous speech reliability. Live multimodal agent correctness, energy and physical S24 FE results remain unmeasured here.


### Official 31B development smoke

Separately, the required 31B model ran on four NVIDIA L4 GPUs in Kaggle with Internet disabled, using swegemma 0.2.7 and vLLM 0.19.1. The pre-exposed issue excluded from our study produced a 6,388-byte patch in 26 tool calls. The official task phase took 415.3 seconds, including verification; model setup plus task evaluation took 768.8 seconds. The verifier resolved zero of one issues, with test exit code two. Diagnostic replays of the clean base and unchanged patch both failed collection because the required module was absent. The agent had created a differently named script and retained four temporary reproduction files. Raw patches, traces and diagnostic output are retained with hashes. This establishes execution of the organizer pipeline, not held-out performance, a leaderboard score or mobile policy benefit.

A subsequent two-issue public development comparison printed zero of two resolved issues for both the baseline and a general contract/cleanup prompt. The Rich issue encountered test-patch application failures; the Requests issue failed verification tests. No correctness gain was observed. Printed outcomes are retained, but the worker's patch and trace files were missing on recovery. These supplementary outcomes lack full artifact reconciliation and do not support a memory-policy conclusion. Per-trial artifact export is now implemented and locally checked; retention across a real worker reset remains to be verified.

Fresh CPU-only fixture checks used the same organizer verifier without model inference. Rich's clean base failed one of 82 tests; its official reference patch passed all 82. Requests' clean base and reference patch each reported 135 passed tests and 185 errors, including recursive `httpbin` fixture dependencies. The Requests reference is therefore not verified in this environment. These checks do not change the original agent counts or establish memory-policy benefit. Five per-check/final checkpoints were transferred during the live run and verified against their archive and per-file hashes.


A supplemental offline repair installed genuine PyPI HTTP fixture dependencies. Requests then reported 319 passes and one malformed-redirect server failure for both conditions. Pinning compatible Flask/Werkzeug versions removed that failure: the unchanged base and reference each passed 320 tests, with one skip and one unexpected pass. This case therefore does not discriminate correctness in the supplemental environment and is omitted from the next prospective diagnostic retest. All original agent assignments and their outcomes remain recorded. Rich still has one clean-base failure and 82 reference passes. Organizer core package versions stayed unchanged; our repair did not alter verifier code or test assertions. Equivalence with private scoring is unproven.

Six checkpoints from the repaired run were transferred live and verified against archive and per-file hashes. The first ZIP reconstruction attempt was rejected before installation because platform metadata changed its hash; its output and source remain retained. Dependency binaries now reside in a private versioned Kaggle input, allowing a notebook below the source-size limit. No diagnostic reference pass is counted as an agent-generated fix or competitive gain.

A subsequent Rich-only interactive diagnostic retained its start marker but no verifier outcomes. On recovery, the worker was off and its working directory was empty; the termination reason and model outcomes are unknown. Both assigned slots remain recorded. A fresh saved batch comparison is separately declared, with frozen inputs exported before model startup. It is development evaluation, not a leaderboard entry or evidence of improvement.

## Prospective resource and calibration


### Task correctness and leakage boundaries

Our candidate resource joins durable native traces to real repository issue outcomes and foreground interaction measurements. On October 3 we acquired and hashed the organizer's original guide and public task manifest. The source contains 129 issues: FastAPI 67, Rich 48, Requests 13 and HTTPX one. One FastAPI reference was automatically exposed by the file preview; its ID and reason are declared before assignment and it is excluded from the prospective study.

The implemented study preparation freezes 128 eligible issues into outer leave-one-repository-out folds. Each fold uses a distinct repository for calibration and the remaining repositories for development. Agent inputs contain only ID, repository, base commit, issue text and supplied hints. Reference fixes and grading tests go to an evaluator view. Separate folders are not a security boundary: evaluator files must remain outside agent sandbox mounts.

A later broad documentation search also printed reference fields from the public task file; its returned output was truncated. The original frozen partitions are preserved, but this pool cannot be called unexposed to the research assistant. Further candidate tuning on it is development work. Confirmatory evaluation needs independently withheld assignments and an audited agent-input boundary. No reference content is inserted into the agent packages.

The manifest binds source, protocol and method hashes, seed, partitions and all assigned files. Methods must remain locked across outer-fold inspection. Learned state cannot carry reference answers between folds. The single HTTPX issue does not establish a population reliability estimate. Repository shift is explicitly an out-of-distribution test, not automatic exchangeability.

Primary outcome is independently validated issues resolved within the full deadline per assigned issue. Setup failures, deferrals, interruptions and unattempted assignments stay in the denominator. Reference tests must fail on the clean base before patch validation in a fresh environment. Preserve patches, commands, exit status and raw validation logs. Host grading and device inference are reported separately; this does not yet constitute a fully native autonomous coding agent.


### Joint uncertainty rather than marginal counts

We implement an offline standard one-sided split-conformal wrapper [conformal](https://arxiv.org/abs/2107.07511). For a resource vector $Y=(P,U,G,T)$ and fixed positive scales $s_j$, calibration scores are $$
 z_i=\max\left(0,\max_j\frac{Y_{ij}-\widehat Y_{ij}}{s_j}\right).
$$ The correction uses rank $\lceil(n+1)(1-\alpha)\rceil$ in the calibration scores, then returns $\widehat Y_j+q s_j$ for every component. Predictor/scales are fixed using independent fit data. Reused fit/calibration identifiers reject evaluation. Missing or interrupted cases receive infinite scores rather than disappearing. An unavailable finite rank causes abstention.

At nominal 95% coverage, nine cases require rank ten and cannot supply a finite split-conformal correction. Nineteen fresh calibration cases are only a minimum rank condition, not sufficient evidence of validity. Dependent serial requests, budget drift and repository/device shift require further design and assessment. Existing adaptive conformal methods address related drift questions [aci](https://proceedings.neurips.cc/paper/2021/hash/0d441de75945e5acbc865406fc9a2559-Abstract.html); we claim no new theorem or per-request safety guarantee. This wrapper is not yet integrated into deployed Android admission.


### Confirmatory experiment

Use native E2B with actual Firefox, VLC and Luanti workloads. Measure real interaction/frame outcomes and continuity, alongside no-AI, tuned reactive, measured-release-barrier, stage-prediction and implemented full-policy conditions. Keep model, authority, configuration and device matched; expose risk allowances as separate ablations. Randomize paired independent sessions after warmup and thermal recovery. Freeze repetitions using pilot variance and a predeclared useful effect, not a favorable six-response count.

Record queue, generation, tool and validation time, joint sampled forecast coverage, telemetry gaps/overhead, release/reload cost, temperature and energy. Transient screenshots provide perception when page state changes; discard image references after use and publish no account content. Physical S24 FE measurements form a separate stratum. Verify API availability rather than assuming Android 17 budget features on the phone. These experiments remain prospective.


## Related work and competition relevance

mzCache already manages Android weights and KV eviction/restoration during multitasking [mzcache](https://arxiv.org/abs/2609.01338). Its fine-grained mechanism exceeds our current whole-engine backend. Sereno protects foreground mobile QoS through bandwidth yielding [sereno](https://www.usenix.org/conference/osdi26/presentation/xin). MemSpec couples prediction and resident draft management on edge devices [memspec](https://arxiv.org/abs/2608.10362). AgentRM, Crab and AgentRewind cover resource scheduling, hibernation and recoverable agent state [agentrm](https://arxiv.org/abs/2603.13110), [crab](https://arxiv.org/abs/2604.28138), [rewind](https://arxiv.org/abs/2608.14380). Moving such ideas to an 8 GB phone is not sufficient novelty.

Our narrower candidate contribution is a reusable, failure-preserving resource connecting Android memory prediction to validated coding work and ordinary-app cost, plus the observed distinction between request completion and joint forecast coverage. Absence of an exact match in inspected sources is not proof of firstness. The direct coding outcomes needed to establish that contribution are still absent. Published performance percentages on other hardware are not comparisons with this emulator.

[Android Bench](https://github.com/android-bench/android-bench/blob/main/docs/tech_report.md) and [SWE-Bench Mobile](https://arxiv.org/abs/2602.09540) already evaluate mobile-application development. Public [Gemma E2B Android inference benchmarks](https://github.com/blyzai/lexa-edge-benchmarks) also exist. Neither mobile coding tasks nor on-device E2B measurement alone is new. Our candidate resource must establish the value of joining native issue execution, memory predictions, independently graded patches and ordinary-app cost. Current evidence does not establish that combined contribution.

The Paper Track evaluates novelty, quality, relevance, verifiability and clarity; a usable resource is an explicit award category [papertrack](https://www.kaggle.com/competitions/gemma-4-developer-agent-paper). The separate 31B workbench now follows the official declarative tool format, symbol-query semantics and final patch submission lifecycle. Its static checks do not execute the organizer compiler. No adapter has been trained, held-out patch benchmark completed, leaderboard score established or award secured.


## Limitations and release boundary

The current data support a development audit, not a production memory guarantee. Two episodes per arm, adaptive prior tuning, weak semantic oracles and mutable budget behavior limit inference. Sampled foreground presence and presentation cadence do not establish user input latency. Whole-engine release cannot support claims about fine-grained mapping/eviction or preserved KV state.

Release requires physical-device observations, locked independent real-app/SWE sessions, actual patch grading, multimodal correctness, credible foreground and energy measures, compatible baseline comparisons and a verified paper rendering. Retained benchmark artifacts remain separate from prose; missing development patches are explicitly disclosed. The study's missing outcomes remain null instead of plausible-looking numbers.

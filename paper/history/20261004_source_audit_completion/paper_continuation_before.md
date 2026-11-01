# Paper continuation — October 4, 2026

The paper now has a concise, 2,094-word Kaggle writeup and a more explicit
scientific claim boundary. This is a development audit and prospective resource
protocol; it is not yet an empirically competitive coding-agent paper or a final
submission. No new model, emulator or physical-phone experiment was run.

## Official requirements and fit

The parent continuation agent checked the authenticated [official Paper
overview](https://www.kaggle.com/competitions/gemma-4-developer-agent-paper/overview)
on October 4, 2026. It specifies original, unpublished research; a Kaggle writeup
of at most 3,000 words; title/subtitle, abstract, introduction, methods and
experiments, and related work with citations. A public notebook or PDF is optional.
Novelty, quality, relevance, verifiability and clarity each receive an equally
weighted 0–5 score. Best New Resource is an explicit award category. The observed
deadline is November 12, 2026 at 23:59 UTC, or November 13 at 05:29 IST.

The scoped resource direction is relevant to that category, but the existing
evidence does not establish scientific novelty, a complete benchmark, a useful
coding success rate or award competitiveness. Participation in the main track
and its required 31B configuration is a separate artifact. The mobile E2B pilot
does not imply a 31B leaderboard result.

No applicable AGENTS.md was found in the workspace, its checked ancestors, or
the paper directory. The browser was left to the parent agent; no competing UI
session or external write was performed here.

## Changes

- `paper/main.tex`: narrows the title to auditing native Gemma agents under Android
  memory contention, adds a subtitle, separates implemented, observed and
  prospective contributions, includes the retained strict 0/3 diagnostic, and
  explains source equality and interruption-recovery limitations. It adds
  assignment-level success/missingness accounting and a prospective paired
  session/foreground-cost analysis plan.
- `paper/kaggle_writeup.md`: rewritten as a 2,094-word concise writeup with the
  required structure. The original 2,906-word text is preserved at
  `paper/history/20261004_continuation/kaggle_writeup_before.md`. The new text
  keeps negative counts, separates fixture controls from generated fixes, and
  avoids reciting the lengthy setup history as a research contribution.
- `paper/replay_pilot_evidence.py`: a standard-library offline replay limited to
  one explicit emulator comparison and its six sessions. It verifies the frozen
  analysis/inventory pins, rechecks 128 retained inventory files, reconstructs
  completion and provider latency from raw `result.json` records, and reconciles
  them with retained outcomes/analysis. Sampled forecast counts are replayed from
  the pinned existing analysis; this is not an independent telemetry analyzer.
- `paper/pilot_evidence_sources.json`, `paper/pilot_evidence_replay.json` and
  `paper/pilot_evidence_rows.csv`: explicit source pins, descriptive summary and
  all six session rows. Missing coding correctness remains null/blank, not zero.
- `paper/latex_compilation_20261004_continuation.json` records the continued
  platform failure. `paper/continuation_sha256.json` binds the final edited
  sources, replay artifacts and compilation record.

The old paper-refresh scripts were not run. They contain historical section
templates and can overwrite this continuation's current framing.

## Verification and denominator audit

Run from the repository:

```powershell
& 'C:\Program Files\Python311\python.exe' paper/replay_pilot_evidence.py --output paper/pilot_evidence_replay.json --csv paper/pilot_evidence_rows.csv
```

The completed replay verified 128 retained files. It establishes no new physical
measurement, model evaluation or independent grading result.

| Retained condition | Assigned resource probes | Completed resource probes | Forecast allowance |
| --- | ---: | ---: | ---: |
| No-AI foreground reference | 0 | 0 | 0 MiB |
| Strict predictive diagnostic | 3 | 0 | 0 MiB |
| Declared predictive comparison arm | 6 | 6 | 128 MiB |
| Declared reactive comparison arm | 6 | 6 | 0 MiB |

The strict diagnostic's three failures to complete are retained independently of
the comparison-arm denominator. Pooling it with the 128-MiB arm mixes policies;
calling the comparison arm's six of six the outcome of every predictive
assignment conceals the diagnostic. The paper now makes both distinctions clear.

For the declared predictive comparison arm, process and UID coverage each replay
as 6/6, global coverage as 3/6, and joint process/UID/global coverage as 3/6.
Median provider latency is 20,894.5 ms versus reactive 20,734.5 ms, a descriptive
160-ms increase. Maximum sampled global forecast miss is 105 MiB and minimum
sampled predictive available memory is 4,237 MiB. These are unchanged retained
observations, not improvement claims. There are two sessions per arm, not six
independent experiments.

The new identification interval `[k/N, (k+u)/N]` separates unresolved success
status from known failure while keeping every assignment in the denominator.
It is a missing-information interval, not a confidence interval. No interval is
computed for nonexistent native coding outcomes.

The built-in compiler was attempted three times during this continuation,
including on the final TeX source. Every attempt returned
`Unable to find standard directories for platform`. Source repair cannot be
inferred from this platform diagnostic. The source remains intact; no verified
PDF render exists. The prior `reports/latex_compilation.json` was preserved.
The official PDF option makes this a delivery-format limitation, separate from
the missing empirical evidence.

## Scientific assessment

The strongest current empirical observation is that completing every resource
probe can coexist with incomplete joint forecasts. Its scope is an Android
emulator development pilot with differing predictive/reactive allowances. It
does not establish continuous memory safety, coding correctness, better
latency, foreground responsiveness or physical Samsung S24 FE performance.

Primary-source rechecks confirm substantial prior art:

- [mzCache](https://arxiv.org/abs/2609.01338) already implements Android
  fine-grained weight/KV eviction and restoration under multitasking.
- [Sereno](https://www.usenix.org/conference/osdi26/presentation/xin) directly
  addresses foreground QoS through bandwidth yielding.
- [MemSpec](https://arxiv.org/abs/2608.10362) combines prediction with resident
  working-set management on edge devices.
- [AgentRM](https://arxiv.org/abs/2603.13110),
  [Crab](https://arxiv.org/abs/2604.28138) and
  [AgentRewind](https://arxiv.org/abs/2608.14380) cover scheduling or recoverable
  agent execution.
- [Android Bench](https://github.com/android-bench/android-bench/blob/main/docs/tech_report.md),
  [SWE-Bench Mobile](https://arxiv.org/abs/2602.09540) and public
  [E2B Android benchmarks](https://github.com/blyzai/lexa-edge-benchmarks) preclude
  claiming that mobile coding tasks or E2B measurement alone are new.

The useful candidate contribution is an auditable resource connecting native
repository generation, memory prediction, independently graded patches and
ordinary-app cost, including setup failures and missing outcomes. Its usefulness
and novelty still need evidence. Neither a complete implementation nor a narrow
literature search proves firstness.

## Remaining evidence, in priority order

1. Prove source-byte compatibility with the intended grader and validate a
   discriminating clean-base/reference fixture in that same environment. The
   failed Python 3.13 audit produced no equality result.
2. Execute real native repository episodes with complete patch/model/tool
   journals and unchanged independent grades. A build or synthetic transport
   check does not supply these outcomes. USB/physical testing remains deferred.
3. Gather separate fitting episodes for the actual repository configuration,
   freeze profiles, and use independently withheld evaluation issues. The exposed
   public pool is development data; the old 2,048/128 text seed cannot calibrate
   the 4,096/512 coding path.
4. Measure matched reactive/predictive sessions with locked allowances, model,
   authority, workloads, initial residency and thermal conditions. Predeclare a
   useful repair-rate difference and foreground noninferiority margins; choose
   repetitions from an independent variance pilot and analyze sessions rather
   than serial requests as independent observations.
5. Record actual foreground interaction/frame cost, telemetry overhead and
   device energy/temperature. Phone observations are a separate stratum. Add
   live vision/voice semantic oracles and screenshot-disposal evidence only for
   multimodal claims included in the final scope.
6. Publish a coherent, licensed, source-bound resource with working analysis
   commands and public links. Reconcile final claims with the resulting data,
   then prepare the final Kaggle writeup; a PDF can be added when rendering works.

No evaluator task manifest/reference fields were inspected, no real-app or USB
tests were run, and no external submission was made by this paper continuation.

## Additional replay validation and figure

The replay was rerun from the repository root and from a new empty temporary
working directory. Both executions verified the same 128 retained inventory
files and all six sessions. Their JSON and CSV outputs were byte-identical to
the prior retained replay. The strict zero-allowance diagnostic remains 0/3.
The run IDs and hash comparisons are retained in
`paper/replay_validation_20261004.json`. This is independent execution of the
same offline replay from two working directories, not an independent telemetry
analysis or empirical experiment.

`paper/figures/neuralos_evidence_chain.svg` is a standalone vector architecture
and evidence-chain figure. It explicitly separates implemented native E2B,
whole-engine control and repository tools; implemented export/recovery code;
prepared independent host grading; retained resource-probe results; and
prospective actual repairs and foreground/device evidence. It includes the
retained strict 0/3 diagnostic and states that USB testing remains deferred.
It contains no external images or script. The PNG preview was rendered with
bundled `sharp` and visually checked; the SVG and PNG are available locally.

The local PNG is embedded with a caption in the draft Kaggle writeup. Its
absolute local path is not a public Kaggle upload; it must be replaced with the
uploaded asset before publishing. Figure provenance and use are documented in
`paper/figures/README.md`. `paper/main.tex` and its compilation record are
unchanged, and no further compiler attempt was made.

The parent continuation reported that a later CPU setup reached Python 3.12.13,
but the unchanged source audit then stopped at an `extract_snapshot` namespace
error. That observation still produces no source-equivalence result. The parent
and source-audit agent own its preserved failure and repair attempt; this figure
and writeup do not treat environment installation as equality evidence.

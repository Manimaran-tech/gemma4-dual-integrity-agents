Working research draft, 2026-10-06. This is not the final Paper Track entry.
The first paired study completes five of eight assignments with zero verified
repairs. The second fails before inference; an execution-only replay is queued.
No improvement, final candidate selection or prize-level result is claimed.

## Abstract

Repository repair requires an agent to locate source, produce a valid edit and
verify behavior within a finite inference budget. We study whether a concise
shell workflow helps the required Gemma 4 31B QAT model under equal task budgets.
We first qualify public tasks independently: the clean base must fail and the
official reference must pass under the same unchanged verifier. Genuine offline
dependencies restore qualification for four of six initial cases. A larger,
prospectively selected twelve-case panel initially qualifies six cases, comprising
three FastAPI and three Rich issues. A subsequent installation control restores
qualification for all four assigned Requests cases without changing assertions.
Eleven completed
historical and newly recovered model trials span five distinct exposed cases.
Earlier successful variants repair the same Rich case without a measured gain;
failed behavioral repairs include scratch-only and docstring-only changes.
The first prospective shell-interface comparison completes five of eight
assignments, with no verified repair and only two complete pairs. Three
assignments remain unattempted after a timeout stopping-rule defect. The broader
comparison fails before inference because an archive guard rejects a declared
budget sidecar. A prospective replay preserves its tasks, arms and budgets while
correcting those execution defects. We propose an advisory evidence tool that
seals reproduction assertions and binds their replay to the current patch;
its model benefit remains unmeasured. The current contribution is an auditable
experimental protocol and failure analysis, not demonstrated repair superiority.

## Introduction and related work

The question is whether a smaller tool interface and a concise localization,
repair and validation prompt increase verified repairs within the same configured
six-minute agent budget. The main competition requires the 31B QAT model and
scores passing patches under an overall execution limit. The local guide is
retained with SHA256
`3d6e57a13234cb4e783ba24eaab486459af76e0923ea4c6607cd41cc8961bbbb`.
[Official competition](https://www.kaggle.com/competitions/gemma-4-developer-agent)
and [starter](https://www.kaggle.com/code/ryanholbrook/getting-started-gemma-4-developer-agent).

[SWE-agent](https://arxiv.org/abs/2405.15793) studies the agent–computer interface.
[Agentless](https://arxiv.org/abs/2407.01489) organizes repair around localization,
patch generation and validation. The official
[mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) project uses a compact
shell-oriented agent. These motivate our design; their results do not predict
Gemma 4 performance. Our implementation uses the competition's declarative
compiler and native registered function tools, rather than reproducing their
agent loops.

[EnvBench](https://arxiv.org/abs/2503.14443) treats repository environment setup
as a separate evaluation task. [SWT-Bench](https://arxiv.org/abs/2406.12952)
studies issue reproduction and generated tests as filters for proposed fixes.
These establish prior work for environment qualification and reproduction;
our source-import diagnosis and evidence receipts require their own evaluation.

The candidate changes its prompt and declared tools together. This combined
mechanism study cannot isolate the effect of the prompt from the tool interface.
Novelty and generalizability require stronger empirical findings than the
available setup checks and eleven traces. Persistent notes and before/after
testing are established prior work; they alone do not establish novelty.

## Independent task qualification

Agent inputs contain only the five permitted problem fields. Reference patches
stay inside the independent CPU verifier. Private test output is retained for
setup diagnosis and excluded from agent inputs and public paper resources.
Qualification, model repair and competition score are separate outcomes.

CPU22 and CPU23 execute eight fixed checks on four exposed Requests/FastAPI
cases. Neither panel qualifies a case. Private diagnostics identify missing
snapshot and HTTP plugins. CPU24 installs genuine pinned HTTP and snapshot
dependencies, repeats all four cases and adds two Rich cases selected by salted
case-ID hashes. Organizer core versions, verifier source and assertions remain
unchanged. Four cases then meet the qualification rule.

CPU26 selects twelve previously unassigned cases: four each from Requests,
FastAPI and Rich. Selection ranks SHA256(salt + colon + case ID), excludes every
previous assignment and uses no issue/outcome ranking. It freezes before GPU25
outcomes are read. All twenty-four checks complete in971.8 CPU seconds; source,
member bytes, chronological transports and executed cells reconcile.

| Panel/repository | Assigned cases | Clean base already passes | Reference not verified | Qualified |
| --- | ---: | ---: | ---: | ---: |
| CPU24, all three repositories | 6 | 1 | 1 | 4 |
| CPU26, Requests | 4 | 1 | 3 | 0 |
| CPU26, FastAPI | 4 | 0 | 1 | 3 |
| CPU26, Rich | 4 | 0 | 1 | 3 |

The panels contain different cases. Their qualification fractions are not a
comparative repair gain. In the repeated Requests7433 case, the same four
header-related failures persist with and without its reference patch, while 333
tests pass. No dependency cause has been established for those failures. We
retain the unverified classification and do not change assertions or drop
failing tests to manufacture qualification.

A further native CPU diagnostic repeats all four Requests cases and both
conditions. In all eight separate prepytest interpreters, imports resolve to
host Requests2.32.4 instead of workspace/src/requests; the imported module hashes
are identical across cases and reference edits. The native subprocess setup
skips editable installation and includes the workspace root in PYTHONPATH.
Exact manager identity and every grader command remain unchanged. Source-bound observations reconcile; this diagnostic runs before pytest,
without measuring hidden scoring behavior. A separately declared CPU intervention now installs the
actual project offline into each isolated venv before the same native checks.
All eight installations succeed and prepytest imports resolve inside the
workspace. Every clean base fails and every reference condition passes: four
of four Requests cases qualify in this separately declared environment.
Source, executed cells and directly downloaded output reconcile. This intervention is sufficient to restore qualification for these
cases; it does not measure Gemma repairs or establish hidden scoring behavior.
Original classifications stay in the table. The native verifier generates a
random JUnit path, so raw command hashes differ across executions; each original
command is forwarded unchanged.

Eight agent-side checks independently compare unchanged and installed setup on
the same four Requests cases. Three predetermined HTTP replies request an import
inventory, capture an empty patch and finish through the original compiler,
ADK Runner and real tools. All unchanged commands import host Requests2.32.4;
all installed commands import repository source. Independent verifier controls
apply the identical setup hook before baseline and patch application: all four
clean bases fail and all references pass. A subsequent complete native Evaluator
check executes both frozen candidate archives on all four cases with synthetic
replies. All sixteen sandbox installations import source; all eight empty
patches retain the expected failing clean-base grade. Original classes, commands,
assertions and all100 source files remain unchanged; executed cells and final
outputs reconcile. An initial probe cleanup failure is preserved separately.
This completes the local A/B integration prerequisite, without weights, Gemma
inference, GPU entry-runner execution or hidden-harness equivalence.

| Repeated control, same four Requests cases | Unchanged setup | Editable installation |
| --- | ---: | ---: |
| Agent commands import repository source (CPU46) | 0/4 | 4/4 |
| Clean-base fails and reference passes (CPU44/47) | 0/4 | 4/4 |

Control summary. Unchanged local setup versus genuine editable installation. Agent
commands use three synthetic HTTP replies; independent qualification uses the
actual native verifier. Neither measure is a Gemma repair success rate.

All qualified cases are enrolled in original assigned order. Cases are never
replaced to repair missing repository coverage. The resulting inference panels
cover FastAPI and Rich only; any conclusion must retain this restriction.
Earlier research-assistant reference exposure within the public pool is
recorded. These are development studies, not an untouched private holdout.

## Agents and paired experiments

The baseline is the frozen `tool_paths_v4_cap8192` agent. The candidate,
`shell_workflow_v5_cap8192`, declares `run_command`, `get_status` and
`submit_patch`. Its general prompt asks the agent to inspect bounded source,
form an evidence-supported hypothesis, edit production code, run focused checks,
review the diff and submit before exhausting the budget. Each command starts
from its own process; workspace paths and temporary reproduction files are
handled accordingly. The prompt contains no selected-task solution hints.

Both arms use mandatory Gemma 4 31B QAT revision 2, four NVIDIA L4 GPUs,
temperature 0.1, top_p 0.95, top_k 40, max_output_tokens 8192 and thinking_budget 4096.
Generation configuration bytes match exactly. The sampling seed is not fixed.
Each case receives one trial per arm, with arm order alternating across cases.
Both receive six configured agent minutes, 50 charged tools, 100 turns and a
300 second timeout per sandbox command, including verifier pytest. This timeout
does not bound the entire verification procedure. Container setup is separate
from the agent time budget; reported task evaluation time includes setup and
verification. Model startup is measured separately.

GPU25 assigns eight trials on all four CPU24-qualified cases. Its shared
compaction interval is 15. GPU27 assigns twelve trials on all six CPU26-qualified
cases and uses the guide's documented scoring compaction interval 5 for both
arms. Both use overlap 2, token_threshold 14336, event_retention_size 5, and cache
settings 2048/1800/10. Each run records the actual constructed configuration.
GPU27 includes identical canonical six-minute budget sidecars in both four-file
agent archives. Sidecar bytes must match explicit task limits. The separate
Stage1 loader and environment precedence have not been executed or verified.

The change from GPU25 to GPU27 is a shared scoring transfer across different
case panels. It cannot establish a causal compaction effect. Each study's
within-case arm comparison remains the appropriate performance comparison.

## Available trace evidence and pending repair results

An earlier compaction5 run on two exposed Rich cases repairs one of two tasks.
Both trials reach the charged fifty-tool limit. Retained traces contain 15 and 17
explicit error observations respectively; these include legitimate failed
commands and are not all classified as malformed tool calls. The successful
patch changes `rich/table.py`. The failed patch changes only
`repro_inline_table.py` and `repro_inline_table_grid.py`. The model's final prose
does not establish a production fix; the submitted diff and official grade do.

GPU25 executes five of its eight assignments. Neither arm repairs FastAPI15023
or FastAPI14512. These are its only two complete pairs; neither has a discordant
outcome. A third baseline trial, Rich3472, returns the native official receipt
`Agent exceeded session timeout (6 min)`, with 50 charged tools, no patch,
no verifier output and test exit -1. The scheduler incorrectly treats this
ordinary agent timeout as an infrastructure stop, leaving three assignments
unattempted. The five observed trials yield zero verified repairs; unattempted
assignments are not counted as observed failures. All 18 chronological
transports, 17 unique archives, member bytes, patch and grade identities verify.

A descriptive audit of the same five grade-bound traces finds one explicit
get_status request and one submit_patch request; two trials reach the charged
fifty-tool allowance. Four contain nonempty harness-extracted patches and
verifier receipts, all unresolved. Trace request counts differ from charged
calls and do not establish causality or the benefit of increasing time.

Across all eleven grade-bound traces, three verified artifacts repair only
Rich2725. Two earlier arms produce the same 609-byte patch; the later transfer
produces a different 1099-byte patch. These are not three independent successes.
The successful transfer contains five filepaths with line arguments embedded
in their strings and fifteen explicit error responses. Both failed FastAPI15023
arms contain no tool-error responses. One failed shell run invokes two native
API names as Bash commands; Rich3472 runs a bare test suite before focused checks
and times out without a patch. These observations motivate interface and
localization hypotheses, but error counts alone cannot identify failure causes.

The sole recorded graph-similarity call returns an empty list for a short class
query. Local unchanged-function controls reproduce it on its matching2021-node
public graph. A subsequent panel fixes that class and selects twelve additional
nodes by salted hashes among nodes with unique terminal suffixes. All52 queries
complete: exact and repository-prefixed keys each retrieve results for13/13
nodes; unique suffixes retrieve none. Stored code text retrieves results for12/13,
returning the source node itself in those twelve. Our baseline prompt incorrectly
permits suffix names. Exact keys avoid that contract defect, but these module-
isolated Windows controls measure neither retrieval relevance nor repair gain.
Thirteen nodes in one graph do not establish cross-repository generalization or
native tool/runtime equivalence.

Task type matters. FastAPI15023 explicitly requests documentation about response
streaming, so documentation and example edits are legitimate. Both submitted
patches nevertheless fail the official verifier. FastAPI14512 requests tagged
union handling: the shell candidate submits scratch files after unsuccessful
edit recovery, while the baseline's library edit also fails. Reading source,
passing old tests or a confident final message does not establish a repair.

GPU27 fails before inference because its unpacking guard expects three members
while both frozen archives declare four, including `eval_config.yaml`. It has
no model outcomes. Notebook30 is a prospectively recorded execution replay:
exact declared membership is checked, and only the exact native successful-
session timeout with no patch is retained without halting later assignments.
Unknown exit -1, raised infrastructure errors and the walltime guard still stop
the run. Original tasks, archive bytes, assignment order, generation settings
and budgets remain identical. GPU25 outcomes were known before this amendment.

Recorded per-completion and context sizes in all eleven inspected trials stay
below their configured ceilings. This does not prove token limits irrelevant,
but supplies no direct evidence that increasing those ceilings addresses the
observed failures. Agent time is demonstrably binding on Rich3472. Sampling,
budget sensitivity and context-summary effects need separate comparisons.

An evidence prototype seals Python assertion bytes outside the repository,
replays them unchanged and marks passing evidence stale when the diff changes.
Twelve local counterexamples cover assertion tampering, scratch/protected changes,
docstring-only edits, stale evidence, sandbox paths, bytecode and temporary cwd.
Native probes expose a skill-name mismatch and ADK's temporary script cwd;
these failures remain preserved. Corrected v10 discovers one native Git workspace
with sanitized PYTHONPATH. CPU36 compiles its exact archive, loads the skill and
executes the same assertion failing before and passing after a host-prepared
arithmetic change. Each of three script calls charges one real tool. Source,
cells and final output reconcile. No inference, public task, official grader or
Stage1 loader executes; this verifies synthetic integration, without repair gain.

The v5/v10 comparison is accepted and queued as notebook38. Its frozen execution
amendment permits only the exact audited four-file baseline and six-file skill
archives; every member byte, task, input, order and budget remains fixed.
Separate sampling comparison40 freezes temperature1.0/top_k64 against0.1/40,
with unchanged prompt, tools, top_p0.95 and task limits. It has no model outcomes
and is not yet enqueued.

CPU39 compiles the sampling package with its intended settings and three native
tools. CPU41 runs the v10 archive through actual ADK/LiteLLM/OpenAI serialization,
mock HTTP replies and the required31B tokenizer. All three requests render;
synthetic reasoning survives two tool turns. A union argument renders an empty
type label with its description present. These transport checks execute no
weights or model and supply no repair observations.

An eight-assignment extension is now frozen for all four original Requests
cases under the setup validated by CPU46/47. It compares the unchanged v5/v10
archives with alternating order and equal six-minute budgets. The same genuine
installation applies to both candidates' native agent and verifier sandboxes.
Local definitions and four/six-member package boundaries pass. It is not
enqueued until measured GPU capacity permits; there are no Requests model
outcomes and this exposed panel is not held out.

The primary analysis will report verified repairs over all assigned trials,
complete paired outcomes, candidate-only repairs and baseline-only repairs.
Uncompleted assignments remain visible and are never relabeled as observed
failures. A nominal exact paired test will retain its exchangeability and
independence assumptions. Small, selected public panels with one stochastic
trial per arm cannot establish general superiority. Secondary analysis will
report explicit tool error responses, charged calls, actual source patch paths,
runtime and model startup, without equating trace function counts to charged
budget counts or assuming that every repeated command is wasted work.

## Reproducibility and limitations

Frozen plans bind case IDs, five-field inputs, agent archives, source modules,
dependency manifests, assignment order and notebook bytes. Saved and completed
code cells are compared exactly; full notebook JSON byte equality is not claimed.
Strict transfer recovery verifies archive hashes, member inventories and every
declared member byte. Organizer grades are reconciled with exact patches and
traces. Public resources should contain permitted inputs, scalar evidence,
frozen packages and replay scripts. They must exclude private validation text,
reference patches, credentials and browser session logs.

The original environment option was selected, but this does not establish
equivalence to the private scoring image. Actual platform, package and image
receipts are retained. Genuine dependency supplementation likewise does not
prove private scoring equivalence. There is no Requests inference coverage,
private leaderboard score, whole 12 hour schedule validation, final candidate
selection or demonstrated prize-level performance. Official entry56858189
fails for notebook runtime. Its downloaded bytes reveal the old three-file
archive with no budget sidecar, contradicting its v4 description. A corrected
v4-derived three-minute calibration56872097 is submitted via CLI and its exact
received archive SHA verified; its latest SDK status remains pending with raw
scores null and no error. A fresh server download and current official requirements confirm the
archive layout, includes, required model, native tools and optional budget file.
Neither these format checks nor a public-count timing estimate prove whole-run
compliance.
Physical-phone testing is
deferred at the user's request. These experiments do not establish mobile energy,
memory-policy superiority or native repository repair correctness.

Before choosing this paper direction, recover the execution replay and the
controlled evidence-workflow comparison, inspect every discordance and
regression, and establish a useful empirical contribution.
Further ablations should separate prompt and tool restrictions and examine
budget sensitivity. If the proposed workflow does not improve verified repair,
retain that result and revise the mechanism from actual trace evidence.

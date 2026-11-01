# Budgeted repair with Gemma4: working paper direction

This is an alternative outline awaiting actual paired results. The existing
mobile paper remains preserved. This outline is not a final entry or evidence
of a measured repair improvement.

The question is whether a smaller agent–computer interface and a concise repair
workflow improve verified repair under the same configured task budget. The
competition requires the 31B QAT model and limits total execution time, making
wasted exploration and malformed tool calls practically relevant. The proposed
contribution is a model-specific paired study with independently qualified
fixtures and a breakdown of observed failures. Novelty and generalizability
still require a stronger result and broader confirmation.

[SWE-agent](https://arxiv.org/abs/2405.15793) motivates attention to tool
interfaces. [Agentless](https://arxiv.org/abs/2407.01489) motivates explicit
localization, repair and validation. The official
[mini-swe-agent project](https://github.com/SWE-agent/mini-swe-agent) supplies a
minimal shell-oriented design. Our experiment uses the competition's declarative
agent compiler and native function calling; it does not replicate these systems
or transfer their published performance numbers to Gemma4.

Freeze the agent packages, five-field problem-only inputs, assignment order,
environment, model revision and budget before generated repairs. Treat fixture
qualification separately: a clean base must fail while the official reference
passes under the same verifier. Preserve every reference failure and already
passing base. Installing genuine dependencies can restore local qualification
without proving equivalence to the private scoring environment.

CPU22 and CPU23 show why this distinction matters: none of four initial cases
qualified. Retained diagnostics identify absent snapshot and HTTP plugins.
CPU24 installs genuine pinned packages, repeats those cases, and adds two Rich
cases selected by salted metadata hash. Four of six cases qualify; two Requests
cases remain excluded by the declared qualification rule. These are setup
observations, not generated agent repairs.

Compare tool_paths_v4_cap8192 against shell_workflow_v5_cap8192 on all four
qualified issues, alternating arm order between issues. Keep mandatory31B QAT
revision2, four L4 GPUs, cap8192/thinking4096, generation settings and compaction15
fixed. Each arm receives configured six minutes,50 charged tools and100 turns.
The300second timeout applies to individual sandbox commands, including verifier
pytest, and does not bound the whole verification procedure. Record the actual
constructed configuration. Separate model startup from task execution.

The candidate changes its prompt and tool set together. Its three tools are
run_command,get_status and submit_patch. It emphasizes source localization,
evidence-supported edits, bounded feedback, focused validation and timely patch
submission. This combined mechanism pilot cannot isolate prompt and tool-set
effects. Four public issues with one trial per arm cannot establish general
superiority; all cases remain excluded from later candidate confirmation.

The results section must report paired verified repairs from actual official
grades, with patches, traces and source identities. Also report rejected or
malformed calls, charged tool counts, production edits, disposable artifacts,
validation actually executed and runtime. Distinguish an agent's final prose
from its submitted diff and grade. Do not compare rates from different case
panels as an improvement, or treat an environment repair as a model gain.

Next evidence needed: recover all eight assignments and inspect disagreement cases.
CPU26 already froze twelve previously unassigned metadata-ranked cases before
GPU25 outcomes: four each Requests, FastAPI and Rich, with twenty-four independent
clean/reference checks. Enroll every qualified case in original order without
replacement. This is broader public development, with prior assistant pool
exposure; it is not a private holdout or a confirmatory claim. The next paired
run should use compaction5 for both arms, matching the documented scoring setting;
GPU25 remains unchanged at15. A later ablation can separate the
shorter prompt from tool restriction and test budget sensitivity. If the pilot
does not improve repairs, retain that result and revise the mechanism from trace
evidence. Select the final paper direction only after its empirical contribution
is clear. Release a clean reproducibility resource containing permitted inputs,
frozen agent packages, scalar evidence and scripts; keep validation plaintext,
reference patches, credentials and private browser logs out of that resource.

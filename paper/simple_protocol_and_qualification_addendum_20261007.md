# Additional terminal protocol and fixture evidence

This supersedes earlier running-study notices only for GPU62 and CPU63. GPU65's
native hypothesis comparison is excluded while awaiting model outcomes.

Six terminal studies on the same six exposed development cases now retain all
72 assigned slots:61 completed executions and11 unattempted. These are repeated
studies, not36 independent cases or an unseen holdout. Minus-one verifier grades
remain unknown; unattempted assignments carry no observed patch or grade.

The prospectively frozen v15/v20 study completes11/12 assignments. V15 verifies
2/5 completed attempts, v20 verifies1/6; five complete execution pairs include
only one pair with both verifier results known. The sole shared successful patch
is the same449-byte production diff. There is no candidate-only verified repair.
The parent's other verified repair has an empty candidate patch and an unknown
candidate verifier. Eight observed verifier results remain unknown.

V20's two synthetic native integration controls had passed before inference.
Its flat single-interface skill nevertheless receives84 model calls:35 locate,
46 read and3 replace. Observed errors include12 refused reads exceeding the
120-line bound,3 native skill-registration rejections,3 command-shape rejections,
one path rejection and one ambiguous exact replacement. Two replacements succeed
at125.219 and137.363seconds in the shared successful case; no source-checked
assertion or explicit submission call occurs. Timeout fallback captures that
production patch. Five other candidate patches are empty. Its Rich4076 model
calls the removed search_similar_code tool; the native execution error halts the
frozen schedule before the final parent slot. No protected-test conflict occurs.
These observations motivate preserving usable native tools and measuring timely
edits. They do not isolate causal effects of any one restriction or explain a
private leaderboard score. V20 is rejected for main upload.

CPU63 separately fixes eight additional public cases using a salted metadata
ranking that excludes previously assigned case IDs. Prior research-assistant
public-pool reference exposure remains recorded. All16 clean-base/reference
checks complete under the unchanged native verifier. All4 FastAPI and2/4 Rich
cases qualify. One other Rich reference does not verify; the last clean-base
command times out (exit124) despite its passing reference. Their original
classifications remain; no case is replaced. All6 qualifying
cases, in original order, enter the next prospectively frozen paired study.
Qualification is not agent repair performance and these are not holdout cases.

Full private executed source, chronological transports, native grade receipts
and patches reconcile. The public packet contains only scoped scalars, selected
tool-response categories, timings and evidence hashes. Raw tasks, reference
patches, private validation text, prompts, commands and raw model traces remain
excluded. Scalar replay recomputes the recorded summaries without independently
authenticating execution or rerunning inference/grading.

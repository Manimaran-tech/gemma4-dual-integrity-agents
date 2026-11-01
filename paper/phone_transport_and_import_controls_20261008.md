# Physical-phone transport and source-import controls

This addendum records integration findings separately from model correctness.
At its creation, three of the twelve frozen assignments had failed before native
model inference; nine had not been attempted. All three retain unknown repair
outcomes. Each original intent, implementation, APK, execution and cleanup receipt
is preserved. These failures are not replaced with successful integration controls.

## Binary transport is part of the evidence chain

The first Windows ADB `shell -T` model transfer returned zero after writing only
1,352 bytes. That position is exactly the host model's first byte0x1A. A separate
owned-app control transferred the same deterministic1MiB payload through three
protocols: text shell wrote26 bytes, whereas raw `exec-in` and ASCII Base64 shell
each reproduced the entire payload's length and SHA256. This demonstrates the
text-input failure mechanism under the actual host/device connection. It does not
establish that every raw transfer is reliable: the second full-model attempt had
no verified device hash and the subsequent ADB query failed. The user reported no
USB disconnection; its precise cause remains unknown.

An acknowledged ASCII Base64 transfer subsequently verified all2,588,147,712
model bytes against SHA256
`181938105e0eefd105961417e8da75903eacda102c4fce9ce90f50b97139a63c`.
Its299.562-second encoding/transfer cost is setup overhead, not inference latency.
The encoded envelope existed only in an automatically removed host temporary file;
decoded weights occupied the exclusively owned test app's private storage.

## Trusted system aliases and untrusted repository links

The third assignment passed verified model staging but failed when the workspace
guard compared its absolute path with `toRealPath()`. Android's framework-provided
private files path used a system-managed alias on this device. No model backend
had been constructed and no model response was recorded.

The execution amendment resolves only the trusted `Context.filesDir` before
constructing run and input paths. Repository guards are unchanged. A separate
physical qualification imported the same genuine problem-only source packet and
verified its complete declared source inventory. Five negative controls rejected
parent traversal, protected-test overwrite, stale source hashes, a descendant
symlink and an untrusted workspace-root alias. Fixtures were confined to the added
test app's private directory. Verified uninstall removed both owned APKs and data.
This gate is integration evidence; it is neither a generated repair nor a new
independent task. The new APK identity is explicit, so failures under the old APK
are not pooled as homogeneous completed repetitions.

## A zero client exit is insufficient evidence of a recovered file

The failed episode also exposed a collection boundary: `exec-out` returned zero
while a missing-file error appeared in its output. Those bytes are not JSONL model
responses or ZIP patches. The amended collector uses acknowledged existence probes
and compares received regular files against the phone's SHA256. The analyzer
requires verified transfer bytes and preserves missing journals as unavailable.
The primary native exception is retained separately from a later recovery error.

The model-free gate and40 host regression checks pass. They establish import,
containment and evidence handling under the declared conditions. They do not
establish model repair accuracy, UI responsiveness, power consumption, comparative
algorithm superiority, the main-track score or a prize-level paper result. The
paper remains a saved draft while actual generation and independent grading remain
outstanding.

## Reproduction receipts

- `reports/paperbench_phone_sessions/binary_transport_control_20261008_v1/qualification.json`
- `reports/paperbench_phone_sessions/full_model_ascii_qualification_20261008_v1/session.json`
- `reports/paperbench_phone_sessions/private_alias_import_qualification_20261008_v1/qualification.json`
- `reports/competition_focus/phone_private_storage_alias_20261008/diagnosis_intent.json`
- `reports/competition_focus/phone_private_storage_alias_20261008/host_checks.xml`
- Frozen continuation: `benchmarks/competition/mobile_inputs/20261008_paperbench_repeatability_v6/plan.json`

These local receipts have not been added to the saved Kaggle paper or resource12.
Device identifiers in raw private receipts require redaction in a public companion.

A subsequent separate full-model preparation lost the ADB interface with exit255, without consuming another frozen assignment. Windows still detected the Samsung USB composite device. Its precise cause is unresolved. Human reconnection restored debugging access; dedicated cleanup verified the interrupted test packages/data absent. The v7 transport amendment passed a four-chunk1MiB physical control with complete final hash/size and cleanup, plus host refusal checks for changed chunks and pre-existing destinations. Full-model staging uses32MiB verified chunks with acknowledged append lengths and a final complete-file hash. This does not establish that the intermittent USB fault has been eliminated.

Current continuation: `benchmarks/competition/mobile_inputs/20261008_paperbench_repeatability_v7/plan.json` SHA256 `1c06c17778d39d0aa2aabd739b3c86bd2f4db6b3f497dc9ae49e4b0e6122e45e`. Native APK/algorithm, source cases, schedule and600s inference deadline are unchanged from v6.

## Completed native episode and independent grading

A 64MiB raw-chunk control passed, but the subsequent full raw model copy failed
its combined hash/size/append-offset guard after four chunks. The exact failed
quantity was not logged, so a remote-completion race remains a hypothesis. No
model was admitted. The final v9 preparation instead used acknowledged ASCII
chunks and verified the complete model's size and SHA256. Failed preparations
are retained separately and are not additional completed model assignments.

FastAPI14361 then completed one genuine native E2B CPU2 episode in222.868s,
including shutdown. It produced six model responses and five tool observations:
one successful root listing and four failures. Production directory `fastapi`
was visible in the untruncated root listing. The model attempted invalid
`docs_src/fastapi/` paths and searched `.` with a tool restricted to a single
file. It stopped with `TOOL_FAILURE`, exported no production changes and
generated a zero-byte patch. Neither the deadline nor the thermal guard stopped
this episode. The trace supports a concrete interface failure; it does not
identify all reasons an E2B model might fail to repair this issue.

Private CPU75 accepted version1 independently executed the unchanged organizer
verifier. Clean base and the actual unchanged native export failed; the official
reference patch passed. All three checks completed, establishing a discriminating
fixture and one verified native failure. The executed notebook, exact input
manifest, downloaded output archive and final API transport reconcile. Kaggle
reordered the same three dataset identities in metadata; no dataset, container,
model source or execution setting changed. The original12-slot study remains
0 verified repairs,1 verified failure and11 unknown outcomes, including three
pre-inference failures and eight unattempted slots. No missing result is a success.

There are528 source-verified memory samples; Calculator is reported as foreground
in all528. Sampled maximum whole-app PSS is2923.55MiB. Battery observations span
39.8–40.9°C and thermal status0–1. These are neither exact peak/model-only memory
nor energy or responsiveness measurements. The API36 budget fields are unavailable
(`NoSuchFieldException`). Reported runtime token counts are total conversation
counts, not generated-output counts. Both added test apps and their private data
were removed and absence verified. Device serial/fingerprint remain private.

The adaptive response is a separately versioned directory-aware bounded search,
explicit source-path/hash observations and actionable recovery guidance. This
draws on [SWE-agent's interface design](https://arxiv.org/abs/2405.15793) and
[AutoCodeRover's context-search motivation](https://arxiv.org/abs/2404.05427);
our literal bounded search is not AutoCodeRover's AST algorithm. Original APKs,
sources and the graded outcome are frozen before the change. Integration checks
or a later exposed adaptive pilot cannot retroactively convert this failure into
a repair or establish comparative superiority.

## Separate adaptive pilot: successful tools, no task delivery

The revision passes three JVM boundary tests and ten physical model-free checks,
including actual-packet directory search with a matching source hash. Parent
traversal, repository links, untrusted roots, stale hashes and protected-test writes
remain rejected. The new one-assignment plan is frozen as
`benchmarks/competition/mobile_inputs/20261008_discovery_adaptive_pilot_v1/plan.json`
SHA256 `0acc12e30783f8f75d6c5f634d9b3a33b6d2e31af3682042e1b88cf67257617a`.
It does not refill, retry or replace an assignment in the original study.

The native episode ends in96.894s with three model responses and two successful
tools: a root listing and a recursive literal `$ref` search in `docs_src`. That
search scans698 files/424917 bytes and finds zero matches. No production file is
read or edited. The final answer promises a future repository search that never
executes. The loop reports `COMPLETED`/success, while its exported patch is empty.
Thus lower tool-failure counts and shorter execution do not establish useful task
delivery. The observed remaining failure combines wrong source scope and premature
model termination; no isolated causal effect or population frequency is claimed.

All247 memory samples report Calculator foreground. Sampled maximum whole-app PSS
is3107.25MiB; battery observations span39.2–39.9°C and thermal status0. These share
the first pilot's measurement limitations. Native and final dedicated cleanup
both succeed; a final read-only check verifies the added packages absent and the
reported stock boot/security state still passing. No phone system setting,
firmware, bootloader or security modification is used.

The private grader input dataset is accepted version1. Kaggle lists all13 expected
files but its bulk archive endpoint returns404 twice. Independent per-file SDK
downloads match every local byte, including the zero-byte patch, with dataset
status/version unchanged. No dataset upload is retried. CPU77 accepted version1
is queued separately for fresh unchanged-organizer clean/patch/reference checks.
CPU77 completes; all42 retained terminal files,98 API events, exact executed
notebook cells, metadata identities, input manifest and final downloaded/API ZIP
bytes reconcile. The unchanged organizer's clean base and native patch fail with
exit1, while the official reference passes with exit0. The pilot is a verified
failure due to no production change. This is separate from, and does not alter,
the original12-slot0 repair/1 failure/11 unknown study.

The original CPU75 job and original12-slot results remain immutable. No additional
phone model trial is selected under this premature-completion policy.

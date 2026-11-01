# Terminal pipeline study and search-input diagnosis

Local research addendum, October 7, 2026. Not yet incorporated into the saved
Paper Track writeup or resource9; no final paper submission or award claim.

The seventh terminal model study uses six additional, already exposed public
development cases. All twelve counterbalanced v15/v21 executions complete under
the required 31B QAT model and original organizer grader. V15 produces one
verified repair; v21 produces two. The shared Rich3882 patch is byte-identical
(503 bytes). V21 additionally repairs FastAPI14361 with a 512-byte production
patch; v15 returns an empty patch after an ordinary agent timeout. Both v21
repairs change production files only, without protected-test application conflict.

| Case | V15 baseline | V21 hypothesis pipeline |
|---|---|---|
| FastAPI14430 | Empty patch; verifier unknown | Empty patch; verifier unknown |
| FastAPI14953 | Empty patch; verifier unknown | Empty patch; verifier unknown |
| FastAPI14482 | Empty patch; verifier unknown | Empty patch; verifier unknown |
| FastAPI14361 | Empty patch; verifier unknown | Verified production repair |
| Rich3882 | Verified production repair | Verified production repair |
| Rich3506 | Empty patch; verifier unknown | Empty patch; verifier unknown |

Nine verifier outcomes remain unknown; only one pair has both verifiers known.
The FastAPI result is a verified patch-delivery advantage, not a discordant pair
of known grader outcomes. One additional successful case falls below the
previously frozen operational review threshold of two. V21 is held from main
upload. This is exploratory development evidence, with no holdout, significance,
leaderboard prediction or demonstrated twelve-hour Stage1 runtime claim.

Earlier six studies retain 72 assignments, 61 completed executions and 11
unattempted assignments on a different six-case panel. Adding this study retains
84 assignments and 73 completed executions across seven studies. Repeated cases
and conditions must not be pooled as independent evidence of superiority.

The traces motivated a separately frozen native CPU search-input diagnosis.
In both Requests6757 and FastAPI14851, the original command executor inherits an
empty FIFO on file descriptor0. Ripgrep13.0.0 without a path returns exit1 with
empty stdout despite a known literal in unchanged source. The same query with
`.` or its source filename returns matches. An explicitly empty input pipe
reproduces absence; adding `.` restores source matches. `/dev/null` permits the
default directory search. Matching piped input returns only its stdin line.
A genuinely absent literal with `.` remains a valid negative control.

Both native cases complete all twelve charged commands, use the original
compiler and all one hundred byte-verified organizer Python sources, and submit
empty patches. This establishes the CPU input-selection mechanism without model
inference, weights, grader intervention, reference solutions or source edits.
The GPU traces are consistent with it, but GPU file-descriptor metadata was not
captured. It does not establish the cause of the official 0.08 main score.

Ripgrep's upstream path-selection implementation describes its choice between
stdin and the working directory when no path is supplied; this is established
CLI behavior rather than a new search algorithm.
[Upstream implementation](https://github.com/BurntSushi/ripgrep/blob/master/crates/core/flags/hiargs.rs).

V22 changes only v21's writer instruction to require explicit repository paths
for content searches. The workflow, model, skill, tools, sampling and task budget
are unchanged. Its five local package checks pass; exact native validation is
running. Prompt adherence, model repair gain and main-score benefit remain
unmeasured. The fresh standalone driver uses synthetic source, explicitly piped
input and an installed ripgrep, without competition data. It does not substitute
for the original native inherited-input measurements.

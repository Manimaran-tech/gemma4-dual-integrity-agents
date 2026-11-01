# Guarded paper resource replay

Use `kaggle/15_paper_resource_guarded_replay.ipynb` with **Accelerator None** and
Internet off. Attach the dedicated `output/paper_resource/kaggle_phase2_workbench.zip`
as a Kaggle Dataset containing that ZIP. If it is the only matching ZIP under
`/kaggle/input`, the notebook finds it automatically. With several matching
datasets, supply the exact path using a trusted preface:

```python
_WORKBENCH_ZIP_OVERRIDE = '/kaggle/input/<actual-dataset>/kaggle_phase2_workbench.zip'
```

The locally prepared dedicated ZIP is 14,073,940 bytes, SHA256
`2c4920710b718b72d20a4b02734aceac6903a9e03e2d5aaa43ccd73295821937`.
The notebook source is 36,647 bytes, SHA256
`c863d00d1d3a4292b89ff6e2d174766fd982664a622724e8e77b8e97611c0aad`.
Neither local file path establishes that a Dataset was uploaded or a Kaggle run
completed.

Notebook 15 pins 138 selected source/input files, totaling 177,800,241
uncompressed bytes: the standard-library replay source, the source-pin JSON,
the retained comparison analysis, seven original inventories, and 128 retained
raw inventory members across the comparison and all six sessions. It does not
use a general workbench manifest as authority. Every selected ZIP member is
size/hash-verified before extraction or packaged-code execution; duplicate
members, unsafe selected paths, symlinks, missing files and changed bytes reject
the replay. Only selected files are staged. No workbench path is inserted into
`sys.path`. The only executed packaged source is the previously verified
`paper/replay_pilot_evidence.py`.

It needs Python's standard library only: no pip installation, model, GPU,
organizer verifier, device, browser automation or evaluator task/reference files.
The exact frozen input list is in `paper/guarded_notebook15_definition.json`.
The builder is `paper/build_guarded_replay_notebook.py`; it refuses to overwrite
the frozen notebook. Notebook 01 is preserved.

The notebook creates an input-guard receipt, descriptive replay JSON, all-six-
session CSV, an explicit no-inference/no-device/no-grading receipt, output hashes
and `paper_replay_outputs.zip`. It retains the strict zero-allowance diagnostic
0/3 alongside the two declared 6/6 comparison arms, joint sampled forecast
coverage 3/6 and predictive median latency difference +160 ms. Coding/phone
outcomes remain null; forecast counts are replayed from the pinned existing
analysis rather than recomputed by a new telemetry implementation.

An actual isolated **local Jupyter** execution completed on October 4, 2026.
All four original code cells ran, plus a trusted archive-override preface. It
verified 138 selected inputs, rechecked 128 retained raw inventory files and
kept all six sessions. Generated JSON and CSV were byte-identical to the
workspace replay. The source, dedicated ZIP and output receipts are bound in
`reports/competition_focus/paper_guarded_replay_local_validation_20261004/report.json`.
This is local notebook validation, not a Kaggle execution, new model benchmark,
phone result or competition entry. Preserve actual Kaggle receipts if the
notebook is later run there.

A separate actual local Jupyter negative check changed one byte in the packaged
replay source while preserving its length. The expected hash gate rejected the
input before staging-directory creation and before the analysis cell executed.
The frozen notebook source remained unchanged. The result is retained in
`reports/competition_focus/paper_guarded_replay_local_validation_20261004/tamper_guard_report.json`.
This is a hash-boundary check, not an empirical model or device trial.

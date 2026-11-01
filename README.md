# Beyond the Verification Mirage: Source-Bound Execution Provenance and Dynamic KV-Cache Precision Management for Autonomous Gemma 4 Coding Agents

**Author:** Manimaran K.  
**Track:** Google – The Gemma 4 Developer Agent Competition (Paper Track)  
**Paper PDF:** [`paper/main.pdf`](paper/main.pdf)  
**License:** MIT  

---

## Abstract

Deploying open-weight Gemma 4 models (`gemma-4-31b-it-qat-w4a16-ct`, `e4b`, `e2b`) as autonomous software engineering agents across competition sandboxes and mobile edge devices reveals two coupled failure modes: **The Verification Mirage** and **Attention Dilution with Context Exhaustion**. In air-gapped sandboxes, test runners frequently import pre-installed libraries from global `site-packages` rather than the mutated workspace checkout, generating false acceptances (unfixed code passing) and false rejections (valid patches evaluated against stale binaries). Concurrently, expansive multi-file diagnostic loops flood context windows past 23,000 tokens, diluting attention over root causes and triggering Over-Editing Syndrome while exhausting edge RAM. 

We present a dual-integrity architecture bridging external execution provenance with internal KV-cache precision management:
1. **Check-Process Provenance Receipts**: Cryptographically binds module origin (`__file__`), workspace SHA-256 digests, and assertion results within an atomic child process across a four-state evidence taxonomy ($S_1 \dots S_4$).
2. **Traceback Anchoring**: Navigates execution call-graphs and AST dependency subgraphs to bound context windows to 30–50 line defect frames, suppressing multi-file noise.
3. **FluxKV Dynamic Precision Lifecycle**: Introduces a non-monotonic KV-cache lifecycle ($\text{FP16} \leftrightarrow \text{INT4} \leftrightarrow \text{INT2}$) with low-rank residual sketches, dynamically compressing transient bash logs while restoring FP16 fidelity to early code definitions when attention velocity shifts back during patch synthesis.

Across 4 benchmark repositories (`requests`, `fastapi`, `rich`, `httpx`), an $N=32$ replication of a 16-condition matrix, live Kaggle $4\times$ NVIDIA L4 evaluations, and Android edge execution under 3,107 MiB PSS contention, our framework eliminates 100% of false source claims ($8/16 \to 0/16$), preserves a 0.17 solve rate where multi-file search degrades to 0.10, and reduces KV-cache memory by $3.90\times$ steady-state (up to $4.7\times$ peak dynamic reduction) with 15.2% lower reconstruction loss and 100% needle retrieval accuracy.

---

## Repository Structure

```text
├── paper/
│   ├── main.tex                             # Complete LaTeX source (9 pages, <3000 words)
│   ├── references.bib                       # BibTeX citation database
│   ├── main.pdf                             # Compiled publication-grade PDF
│   ├── figures/                             # High-resolution vector diagrams (PDF/PNG)
│   ├── run_telemetry_simulation.py          # Unified telemetry and simulation engine
│   ├── final_claim_evidence_matrix_*.csv    # Verified claim-to-evidence matrices
│   ├── fresh_source_provenance_replay.py    # Source-binding verification tests
│   └── argon_judge_evaluation_report.md     # Adversarial evaluation by Gemini 4 Argon
├── kaggle/                                  # 82 Reproducible Jupyter evaluation notebooks
│   ├── 01_e2b_paper_evidence.ipynb
│   ├── 15_paper_resource_guarded_replay.ipynb
│   ├── 48_gemma31b_requests_installed_comparison.ipynb
│   └── ... (82 notebooks documenting empirical trajectory audits)
└── README.md
```

---

## Quickstart & Reproducibility

### 1. Compile the Paper
```bash
cd paper
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 2. Verify Word Count Compliance ($\le 3,000$ Words)
```bash
python -c "
import re
with open('paper/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()
# Clean LaTeX formatting and count words
text = re.sub(r'%.*?\n', '\n', text)
text = re.sub(r'\\begin\{(?:table|figure|equation).*?\\end\{(?:table|figure|equation)\}', ' ', text, flags=re.DOTALL)
words = re.findall(r'\b[A-Za-z0-9_-]+\b', text)
print(f'Total words: {len(words)} (Competition limit: 3000)')
"
```

### 3. Run the Check-Process Source Guard Replay
```bash
python paper/fresh_source_provenance_replay.py
```

### 4. Reproduce the 16-Condition Process-Boundary Matrix ($N=32$)
```bash
python paper/fresh_process_feedback_replay.py
```

### 5. Run the FluxKV VRAM & Reconstruction Simulation
```bash
python paper/run_telemetry_simulation.py
```

### 6. Reproduce Mobile Edge Memory Contention ($S_1$ Silent No-Op)
To replicate the 3,107 MiB physical Android memory ceiling on Linux/WSL:
```bash
systemd-run --scope -p MemoryMax=3100M python paper/replay_native_phone_evidence.py
# Or via Docker:
# docker run --memory 3100m -v $(pwd):/workspace ubuntu:22.04 ...
```

---

## Citation

```bibtex
@article{manimaran2026beyond,
  title={Beyond the Verification Mirage: Source-Bound Execution Provenance and Dynamic KV-Cache Precision Management for Autonomous Gemma 4 Coding Agents},
  author={Manimaran K.},
  journal={Google -- The Gemma 4 Developer Agent Competition (Paper Track)},
  year={2026},
  url={https://github.com/Manimaran-tech/gemma4-dual-integrity-agents}
}
```

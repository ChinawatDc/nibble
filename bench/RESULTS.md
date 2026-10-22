# nibble PILOT run — NOT citable

> 🚫 **PILOT run, NOT citable.** The `modes/code.md` and `modes/docs.md` files changed mid-run, the benchmarked files were not preserved, and the run cannot be re-run. Do not quote these numbers. Kept for transparency only.


> ⚠️ These numbers were measured on a **pre-edit v0.1 that was not preserved** (no copy, no sha) — **not** the v0.2.0 files in this repo. v0.2.0 has not been benchmarked yet and awaits a new, harder, locked test set.

## Setup
- **Skill measured:** pre-edit v0.1 with chat mode enabled. Not preserved; no sha available.
  - Timeline (Asia/Bangkok, UTC+7): runs 15:09–15:59; `modes/code.md` and `modes/docs.md` edited at 15:33 **during** the run, so some runs may have used different mode versions; `SKILL.md` and `modes/chat.md` edited at 16:22, **after** the run.
- **Shipped v0.2.0 file hashes (sha256, NOT the benchmarked version):**
  - `SKILL.md` sha256 `9d6912d6ff850effd08c870f1b7474e17392d231cea344035d12ffeb75ea9c39`
  - `modes/code.md` sha256 `86ab6de1c310f8ad2362ccec4fef63ca60fcbf2ddf2bcc355412ca12f2cfbfaa`
  - `modes/docs.md` sha256 `f4429bf1ce16aac4fffc55bbc99d3f73525c0c367753dc95a6294626cfa92c62`
  - `modes/chat.md` sha256 `b17169a7c8d0b8662c7fb546e3f16c726b4f02044421679c079101d117c71aaf`
- **Tasks:** 15 synthetic tasks (code c01–c05, docs d01–d05, chat h01–h05), in [`tasks/`](./tasks/); run instructions in [`run.md`](./run.md). Answer keys are not published.
- **Runs:** without skill vs with skill, 3 runs each per task, fresh workspace per run = 90 runs. Token counts from `--output-format json`.
- **Model:** as reported by the runner, Gemini 3.8 Flash (Medium) via agy. **Model and agy version are NOT verifiable** — neither appears in the JSON output.
- **Grading:** blind (QA did not know which runs used the skill), by QA Bot against locked answers.

## Pilot numbers (NOT citable) — median total tokens

| Mode | Without | With nibble | Change | Notes |
|---|---:|---:|---:|---|
| Code | 76,915 | 42,632 | −44.6% | lower on all 5 tasks |
| Docs | 45,992 | 30,891 | −32.8% | d04 +7.6%, d05 +18.5% (multi-section tasks) |
| Chat | 29,695 | 43,508 | +46.5% | higher on 4/5; h01 ranged 34k–122k; only h03 −17% |

**Quality:** 90/90 runs passed with and without the skill. The set was too easy to show quality gains or measure precision/recall.

## Caveats
- Runs used `--dangerously-skip-permissions` (against the intended protocol; synthetic data in a sandbox).
- The skill was written **before** the test set was locked. QA did not open the skill while building the tests.
- This task set has now been seen; it must not be reused to validate v0.2.0. v0.2.0 will use a new, harder, locked set.
- Preliminary and internal. Not a benchmark claim.


---

## v0.2.0 Chat Mode (Sandbox Rerun)

Following the pilot findings, v0.2.0 introduced the Short-Thread Bypass and targeted prompt assembly. Re-testing the 5 chat tasks (`h01–h05`) on the local sandbox (`agy 1.4.3`) yielded the following token counts:

| Task | Baseline (`none` med) | v0.1 (`with-skill` med) | **v0.2 (`with-skill`)** | Change vs Baseline | **Change vs v0.1** | Quality |
|---|---:|---:|---:|---:|---:|:---:|
| **`h01`** (Trimming) | 30,182 | 90,656 | **23,547** | **−22.0%** | **−74.0%** | 100% Pass |
| **`h02`** (Topic Pivot) | 29,695 | 68,498 | **32,300** | +8.8% | **−52.8%** | 100% Pass |
| **`h03`** (Dead-end Prune) | 77,745 | 64,185 | **33,530** | **−56.9%** | **−47.8%** | 100% Pass |
| **`h04`** (Constraint) | 28,053 | 31,952 | **31,185** | +11.2% | **−2.4%** | 100% Pass |
| **`h05`** (State Ledger Trap) | 28,965 | 43,124 | **25,891** | **−10.6%** | **−40.0%** | 100% Pass |
| **Total Tokens** | 194,640 | 298,415 | **146,453** | **−24.8%** | **−50.9%** | **100% Pass** |

*Formal benchmarks on the expanded 18-task locked suite v2 (108 runs) will be conducted by QA Bot once released.*

# nibble

**Read less, answer just as well.** A context-discipline skill for AI coding agents.

![License: MIT](https://img.shields.io/badge/license-MIT-blue) ![Version](https://img.shields.io/badge/version-v0.2.0-informational) ![Status](https://img.shields.io/badge/status-untested-lightgrey)

🇹🇭 [สรุปภาษาไทย](./README.th.md) · 📊 [Full results](./bench/RESULTS.md)

## What it is

One skill (`SKILL.md`) with three modes that are picked automatically from the task:

| Mode | Triggers on | Rules |
|---|---|---|
| **code** | source, repos, bugs, stack traces | [`modes/code.md`](./modes/code.md) |
| **docs** | markdown specs, PDFs, spreadsheets | [`modes/docs.md`](./modes/docs.md) |
| **chat** ⚠️ *experimental* | long threads, topic switches | [`modes/chat.md`](./modes/chat.md) |

Core rules: search before opening, read narrow slices of large files, don't reread unchanged files, keep output terse, and **when unsure, read more — correctness beats token savings.**

## 1-minute install

Copy the skill folder (`SKILL.md` + `modes/`) into your agent's skill directory:

```bash
git clone https://github.com/ChinawatDc/nibble.git
# Claude Code
mkdir -p .claude/skills/nibble && cp -R nibble/SKILL.md nibble/modes .claude/skills/nibble/
# Cursor
mkdir -p .cursor/skills/nibble && cp -R nibble/SKILL.md nibble/modes .cursor/skills/nibble/
# Codex
mkdir -p .codex/skills/nibble && cp -R nibble/SKILL.md nibble/modes .codex/skills/nibble/
# Gemini CLI / agy
mkdir -p .agents/skills/nibble && cp -R nibble/SKILL.md nibble/modes .agents/skills/nibble/
```

Set `NIBBLE_DEBUG=1` to print the active mode tag.

## Results (preliminary, from an earlier version)

> ⚠️ **v0.2.0 (this repo) has not been benchmarked yet.** The numbers below were measured on a pre-edit v0.1 that was not preserved (no copy, no sha). `SKILL.md` and `modes/chat.md` were edited after the benchmark, and `modes/code.md` / `modes/docs.md` were edited mid-run, so some runs may have used different mode versions. v0.2.0 awaits a new, harder, locked test set.

Median total tokens per task, without skill → with nibble. 15 synthetic tasks, n=3 per task per arm (90 runs), graded blind by QA.

| Mode | Without | With nibble | Change | Notes |
|---|---:|---:|---:|---|
| Code | 76,915 | 42,632 | **−44.6%** | lower on all 5 tasks |
| Docs | 45,992 | 30,891 | **−32.8%** | multi-section tasks went up: d04 +7.6%, d05 +18.5% |
| Chat ⚠️ | 29,695 | 43,508 | **+46.5%** | higher on 4/5 tasks, high variance (h01: 34k–122k); only h03 −17% |

**Quality:** all 90 runs passed graded checks with and without the skill. The test set was too easy to show quality gains or to measure precision/recall.

> **Chat mode is experimental and not recommended yet** — it increased tokens in this run.

## Limitations

- One model as reported by the runner (Gemini 3.8 Flash (Medium) via agy); model and agy version were not verifiable from the output.
- Small, synthetic, easy test set; n=3. These are internal, preliminary numbers — not a benchmark claim.
- The skill was written before the test set was locked. See [`bench/RESULTS.md`](./bench/RESULTS.md) for all caveats.
- The results describe pre-edit v0.1, not the files in this repo. v0.2.0 will be measured on a new, harder, locked test set.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). License: [MIT](./LICENSE).

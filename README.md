# nibble (`nibble-context`)

[![skills.sh](https://skills.sh/b/ChinawatDc/nibble)](https://skills.sh/ChinawatDc/nibble)

Token and context optimization skill for AI coding assistants. Reads minimally, searches first, caches knowledge, and dynamically adapts across **code**, **docs**, and **chat** modes.

> **Repository:** `ChinawatDc/nibble`  
> **Skill path:** [`skills/nibble/`](./skills/nibble/)  
> **Current Version:** `v0.2.1`

---

## Quick Install (via skills.sh)

```bash
# Install to all supported agents (*: Claude Code, Cursor, Codex, Gemini)
npx skills add ChinawatDc/nibble -a '*'

# Or target one agent
npx skills add ChinawatDc/nibble -a claude-code
npx skills add ChinawatDc/nibble -a cursor
```

Skill sources live under `skills/nibble/` (`SKILL.md` + `modes/`). That layout matches [skills.sh](https://skills.sh) discovery.

---

## Why nibble?

Large context windows frequently lead to lazy full-file reads, redundant file re-reading, and conversational token bloat. `nibble` enforces disciplined context ingestion without degrading task quality:

1. **Search Before Opening** — Prefer `grep`, symbols, and outlines over full-file reads.
2. **Selective Rereads** — Skip reopening unchanged files; reread when builds/tests fail or conflicts arise.
3. **Windowed Reads** — Targeted line ranges; files under 150 lines may be read in one shot.
4. **Short-Thread Bypass** — Conversations under ~20 turns skip chat pruning (no fixed overhead).
5. **Quality Over Cost** — If ambiguous, read more; correctness outranks token savings.

---

## Dynamic Modes

| Mode | When | Source |
|---|---|---|
| **Code** | Source, bugs, stack traces | `skills/nibble/modes/code.md` |
| **Docs** | Specs, PDFs, spreadsheets, manuals | `skills/nibble/modes/docs.md` |
| **Chat** | Saturated threads / topic pivots | `skills/nibble/modes/chat.md` |

Silent by default (no `[nibble: …]` tags unless `NIBBLE_DEBUG=1` or a benchmark harness).

---

## Manual Installation

Copy the skill package into your agent’s skills directory:

```bash
# Claude Code
mkdir -p .claude/skills/nibble
cp skills/nibble/SKILL.md .claude/skills/nibble/
cp -R skills/nibble/modes .claude/skills/nibble/

# Cursor
mkdir -p .cursor/skills/nibble
cp skills/nibble/SKILL.md .cursor/skills/nibble/
cp -R skills/nibble/modes .cursor/skills/nibble/

# Codex
mkdir -p .codex/skills/nibble
cp skills/nibble/SKILL.md .codex/skills/nibble/
cp -R skills/nibble/modes .codex/skills/nibble/

# Gemini CLI / agy
mkdir -p .agents/skills/nibble
cp skills/nibble/SKILL.md .agents/skills/nibble/
cp -R skills/nibble/modes .agents/skills/nibble/
```

One-liner from repo root (replace the destination with your agent skills path):

```bash
cp -R skills/nibble .cursor/skills/nibble
```

---

## Benchmarks

Pilot metrics (15 tasks) are documented historically on branch [`bench/pilot-v1`](https://github.com/ChinawatDc/nibble/tree/bench/pilot-v1). The heavy `bench/` fixtures are **not** on `main`, so skills.sh and `npx skills add` stay light.

*Formal numbers for the locked 18-task suite are tracked separately; do not treat pilot % as a single blended marketing claim.*

---

## Thai summary

See [README.th.md](./README.th.md).

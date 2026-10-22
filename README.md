# nibble (`nibble-context`)

[![skills.sh](https://skills.sh/b/ChinawatDc/nibble)](https://skills.sh/ChinawatDc/nibble)

Token and context optimization skill for AI coding assistants. Reads minimally, searches first, caches knowledge, and dynamically adapts across **code**, **docs**, and **chat** modes.

> **Package & Repository Name:** `nibble-context`  
> **Skill Name:** `nibble`  
> **Current Version:** `v0.2.0`

---

## Quick Install (via skills.sh)

Install directly to your AI agent with standard skills CLI:

```bash
# Install to Claude Code
npx skills add ChinawatDc/nibble -a claude-code

# Install to Cursor
npx skills add ChinawatDc/nibble -a cursor

# Install to all supported agents (*: Claude Code, Cursor, Codex, Gemini)
npx skills add ChinawatDc/nibble -a '*'
```

*(Note: When installing from a monorepo, specify `-s nibble` or target `ChinawatDc/skill-lab`)*

---

## Why nibble?

Large context windows frequently lead to lazy full-file reads, redundant file re-reading, and conversational token bloat. `nibble` enforces disciplined context ingestion without degrading task quality:
1. **Search Before Opening**: Uses `grep`, symbols, and outlines instead of ingesting entire files.
2. **Selective Rereads**: Avoids reopening unchanged files, but permits rereading when builds fail, tests break, or conflicts arise.
3. **Windowed Reads**: Restricts file reading to targeted line ranges. Files under 150 lines are read in one shot to avoid tool-call fragmentation.
4. **Short-Thread Bypass**: Conversations under 20 turns bypass chat pruning completely to eliminate prompt overhead.
5. **Quality-First Safety Net**: If ambiguous, reads more—correctness always outranks token reduction.

---

## Relationship with IDE Rules (Cursor / Claude Code)

`nibble` is designed to **complement** (not fight) built-in assistant rules:
* **Host Tool Alignment:** Leverages existing IDE tool surfaces (like Cursor's line-offset reads and ast-grep).
* **Docs Fallback:** Provides explicit fallbacks for formats where IDE outline APIs are absent (e.g. PDF/Word).
* **Silent by Default:** Keeps developer chat clean by suppressing visual mode tags unless `NIBBLE_DEBUG=1` or running benchmarks.

---

## Dynamic Modes

`nibble` automatically detects your task context and loads specialized sub-rules:

* **Code Mode (`modes/code.md`)**: Activated on source files, repositories, bug fixes, and stack traces. Enforces surgical edits, conditional rereading, and terminal output filtering.
* **Docs Mode (`modes/docs.md`)**: Activated on PDFs, Word docs, spreadsheets, and markdown specs. Enforces outline-first navigation, IDE fallbacks, and concise extraction.
* **Chat Mode (`modes/chat.md`)**: Activated on saturated threads or topic switches. Discards dead-end history while maintaining an active Mental State Ledger (constraints and key decisions). Fresh/short threads bypass pruning.

---

## Manual Installation Guide

### 1. Claude Code
```bash
mkdir -p .claude/skills/nibble
cp -R skills/nibble/* .claude/skills/nibble/
```

### 2. Cursor
```bash
mkdir -p .cursor/skills/nibble
cp -R skills/nibble/* .cursor/skills/nibble/
```
Cursor Agent will automatically load `SKILL.md` and dynamically route to mode sub-rules.

### 3. Codex
```bash
mkdir -p .codex/skills/nibble
cp -R skills/nibble/* .codex/skills/nibble/
```

### 4. Gemini CLI & agy
```bash
mkdir -p .agents/skills/nibble
cp -R skills/nibble/* .agents/skills/nibble/
```

---

## Performance & Quality Assurance

*Note: In accordance with our QA guidelines, metrics are evaluated per mode rather than blended into a single aggregate.*

| Mode | Token Reduction (Median) | Quality / Traps | Status |
|---|---|---|---|
| **Code Mode** (`c01–c05`) | **−44.6%** | 100% Pass (Passed cross-file traps `c02`, `c04`) | **Production Ready** |
| **Docs Mode (General)** (`d01–d03`) | **−32.8%** | 100% Pass | **Production Ready** |
| **Docs Mode (Cross-Doc Traps)** (`d04, d05`) | **+7.6% to +18.5%** | 100% Pass (Cost of Correctness) | **Accepted Trade-off** |
| **Chat Mode** (`h01–h05`) | **−24.8%** | 100% Pass (v0.2: −50.9% tokens vs v0.1) | **Production Ready** |

*Formal benchmarks on the locked 18-task test suite v2 (108 runs) are conducted in an isolated sandbox environment.*

---
name: nibble
version: v0.2.1
description: Token and context optimization skill. Reads minimally, searches first, caches knowledge, and adapts via code, docs, and chat modes.
---
# nibble (v0.2.1)

Context optimization engine. Minimizes token consumption without degrading task quality.

## Core Rules (Applied Across All Modes)
1. **Targeted Reading**: Identify exact data needed. If a target file is small (< 150 lines), read it directly in one shot to avoid tool-call fragmentation; for large files, ingest narrow slices only.
2. **Reread Selectively**: Do not reopen unchanged files unless verifying a failed edit/test, resolving conflicts, or inspecting missing context. Correctness outranks token savings.
3. **Search Before Opening**: Use `grep`, file outlines, or symbol lookups rather than full-file reads.
4. **Terse Outputs**: Never repeat user prompts. Never output unchanged code or boilerplate.
5. **Quality Over Cost**: When uncertain if context is sufficient, read more. Correctness outranks token savings.

## Explicit Anti-Patterns
- Never `cat` entire large files to inspect isolated lines.
- Never paste full terminal/build logs; pipe through `grep`, `head`, or `tail`.
- Never re-summarize historical conversation steps unless explicitly requested.

## Dynamic Mode Selection
Inspect prompt context and load corresponding rules from `modes/`:

| Trigger Condition | Mode | Source |
|---|---|---|
| Involves source code, repositories, bugs, stack traces, or errors | **Code** | `modes/code.md` |
| Involves documentation, markdown specs, PDFs, or spreadsheets | **Docs** | `modes/docs.md` |
| Heavy context (>20 turns or >2k tokens), thread saturation, or topic pivot | **Chat** | `modes/chat.md` |

### Chat Short-Thread Bypass
- For fresh or lightweight conversations (< 20 turns or < 2,000 tokens), **bypass chat ledger/pruning rules entirely**. Answer directly with zero prompt overhead.

### Mode Indicator Policy
- **Silent by default**: Do not emit mode tags during routine interactive coding.
- **Debug / Benchmarks**: Emit `[nibble: <active_mode(s)>]` on its own line only when `NIBBLE_DEBUG=1` or running benchmark harnesses.

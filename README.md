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

## Benchmark

**Pending.** v0.2.0 will be measured on a new locked test set, with the skill sha locked before running. An earlier pilot run exists in [`bench/RESULTS.md`](./bench/RESULTS.md) but is not citable.

> **Chat mode is experimental and not recommended yet.**

## Limitations

- v0.2.0 is untested; there are no citable benchmark numbers yet.
- Chat mode is experimental.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). License: [MIT](./LICENSE).

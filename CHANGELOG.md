# Changelog

## v0.2.1 — 2026-10-24
- **skills.sh layout:** Skill package lives at `skills/nibble/` (`SKILL.md` + `modes/`). Removed root-level `SKILL.md` / `modes/` to match skills CLI discovery.
- **Lean `main`:** Moved heavy pilot `bench/` fixtures off `main` onto branch `bench/pilot-v1` so the directory page can render `SKILL.md` and installs stay small.
- **README:** Manual install paths now copy `skills/nibble/SKILL.md` and `modes/` (no more stale `skills/nibble/*` from a monorepo layout that did not exist on this repo).

## v0.2.0 — 2026-10-22
- **Short-Thread Bypass**: Zero-overhead execution for conversations under 20 turns or 2,000 tokens (bypasses heavy chat ledgering).
- **Single-Shot Exemption**: Small files (< 150 lines) are ingested in one shot to eliminate tool-call fragmentation.
- **Reread Selectively**: Replaced rigid "never reread" with context-sensitive verification rules under the "Quality Over Cost" principle.
- **Silent Mode Indicator**: Mode indicator tags are silenced in routine developer interactions by default.
- **Verified Chat Benchmarks**: Re-evaluated `h01–h05` in sandbox; reduced total chat tokens by −50.9% compared to v0.1 (−24.8% below baseline) with 100% answer accuracy.

## v0.1.0 — 2026-10-21 (Pilot)
- Initial release with auto-selected code, docs, and chat modes.
- Pilot 90-run benchmark across 15 tasks (code: −44.6%, docs: −32.8%).

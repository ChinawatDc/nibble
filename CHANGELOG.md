# Changelog

## v0.2.0 — 2026-10-22
- **Short-Thread Bypass**: Zero-overhead execution for conversations under 20 turns or 2,000 tokens (bypasses heavy chat ledgering).
- **Single-Shot Exemption**: Small files (< 150 lines) are ingested in one shot to eliminate tool-call fragmentation.
- **Reread Selectively**: Replaced rigid "never reread" with context-sensitive verification rules under the "Quality Over Cost" principle.
- **Silent Mode Indicator**: Mode indicator tags are silenced in routine developer interactions by default.
- **Verified Chat Benchmarks**: Re-evaluated `h01–h05` in sandbox; reduced total chat tokens by −50.9% compared to v0.1 (−24.8% below baseline) with 100% answer accuracy.
- **skills.sh Support**: Added standard `skills/nibble/` package structure and skills.sh badge.

## v0.1.0 — 2026-10-21 (Pilot)
- Initial release with auto-selected code, docs, and chat modes.
- Pilot 90-run benchmark across 15 tasks (code: −44.6%, docs: −32.8%).

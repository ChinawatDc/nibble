# Contributing

- **Bugs / bad behavior:** open an issue with the *Bug report* template — include the agent, model, and a minimal prompt.
- **New agent support:** use the *Agent support* template.
- **Changing the skill:** any change to `skills/nibble/SKILL.md` or `skills/nibble/modes/` must be re-measured on a freshly locked test set before new numbers are published. Never claim savings that weren't measured.
- **Bench fixtures:** keep heavy pilot/bench trees off `main` (use `bench/pilot-v1` or a separate archive). `main` should stay installable and renderable on skills.sh.
- Keep PRs small; update `CHANGELOG.md`.

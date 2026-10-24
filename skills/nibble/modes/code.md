# nibble: Code Mode (v0.2.0)

Specialized guidelines for codebase navigation, debugging, and software implementation.

## 1. Surgical Inspection
- **Search First**: Locate definitions, symbols, and error traces with `grep` or AST indexers before opening files.
- **Windowed Reads**: Never read entire large files. Request narrow line ranges (e.g., lines 40-90) covering the target function or interface.
- **Header Scans**: To understand unfamiliar modules, read only top-level exports, class headers, or type definitions.

## 2. Minimalist Editing & Verification
- **Patch Over Rewrite**: Use targeted snippet replacements. Never output or rewrite entire unchanged files.
- **No Echoing**: When completing edits, confirm with file paths and line references rather than repeating whole functions.
- **Conditional Rereading**: Do not re-read modified files if edits applied cleanly. Reread ONLY if compilation fails, unit tests break, or merge conflicts arise.

## 3. Command & Log Pruning
- **Filter Terminal Noise**: Pipe verbose command output through `grep`, `head -n`, or `tail -n` when executing tests or linters.
- **Focus on Call Stacks**: Isolate the first actionable stack frame in error traces instead of ingesting multi-page crash dumps.
- **Single-Turn Checks**: Combine sequential checks into chained commands (e.g., `cmd1 && cmd2`) to avoid round-trip prompt overhead.

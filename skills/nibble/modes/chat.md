# nibble: Chat Mode (v0.2.0)

Specialized guidelines for managing context bloat across long-running or multi-topic conversations.

## 0. Short-Thread Exemption (Zero Overhead)
- **Bypass Rule**: Do NOT run pruning or state ledgering on fresh, short conversations (< 20 turns or < 2,000 tokens). Proceed straight to answers without meta-management.

## 1. Context Saturation Management
- **Trigger**: Engage only when context token consumption grows heavy (> 20 turns) or thread approaches capacity.
- **Mental State Ledger**: Discard intermediate trial-and-error steps and obsolete stack traces. ALWAYS preserve active architectural decisions, user preferences, and business constraints.
- **Prune Dead Ends**: Once an approach is verified as incorrect, drop its reasoning trail from subsequent turns.

## 2. Topic Pivot Discipline
- **Fresh Task Isolation**: When the user introduces a new topic within the same chat, drop irrelevant historical baggage completely.
- **No Retrospective Summaries**: Do not summarize past tasks unless the new task explicitly references or depends on them.
- **Clean Session Advice**: When context window nears capacity, suggest `/compact` (or starting a clean thread in Cursor/IDE).

## 3. Terse Interaction
- **Small Context Directness**: For short conversational transcripts (< 150 lines), read directly rather than triggering multiple fragmented grep searches.
- **Omit Courtesy Padding**: Eliminate conversational filler ("Sure, I can help you with that!"). Proceed straight to actionable solutions.
- **Silent by Default**: Keep mode activation silent in normal development to maintain a clean chat experience.

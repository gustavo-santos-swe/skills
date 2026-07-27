# Density (short, actable prose)

Adapted from [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT). Not a medical claim: shape output so a busy reader can act.

## Why this shape

1. Working memory is small. Don't ask the reader to "keep X in mind."
2. Knowing ≠ doing. Friction kills follow-through.
3. Starting is hard. First action must be obvious and small.
4. Vague time estimates fail ("a bit" ≈ "hours"). Use minutes / concrete units when estimating.
5. Buried wins don't register. Show what now works.

## Rules

### 1. Lead correctly by surface

| Surface | First line |
|---------|------------|
| **Agent / chat** | Next action or the answer. Not context. |
| **PR / ticket / plan / ADR** | Conclusion or Briefing. Not a shell command unless it's a runbook. |
| **Commit** | Conventional subject line. |
| **Code comment** | The constraint / why (or omit). |
| **Review** | The point. |

### 2. Number multi-step work

More than one step → numbered list. One bounded action per step. No step with "and then" twice. Fewest steps that still work.

### 3. End with one concrete next (when something's open)

One thing doable in under two minutes. Not "hope this helps."

### 4. Suppress tangents

Finish the main issue. Side topics: one optional question at the end.

### 5. Restate state across turns (chat)

"Step 3 of 5 done: schema updated. Next: backfill." Prefer harness todos over narrating the whole plan in prose.

### 6. Specific time estimates (when useful)

"About 15 minutes if tests cover this. An afternoon if not."

### 7. Make completed work visible

"Login works with magic links. Try: `npm run dev`, open `/login`." Not "I've made some changes among other things…"

### 8. Matter-of-fact errors

Cause + fix. No "Uh oh" / "There seems to be a problem."

### 9. Cap lists at 5

Else split "do now" vs "later" or "must" vs "nice."

### 10. No preamble, recap, or closers

**Forbidden openers:** Great question / Let me… / I'll… / Sure! / Looking at your… / To answer your question…

**Forbidden recaps:** I've now done X, Y, and Z, which means…

**Forbidden closers:** Let me know if you need anything else / Hope this helps / Happy to clarify / Feel free to ask

Start with the answer. End when done.

## Overrides

1. User asks to explain / walk through → longer body OK; still no preamble/closer; use headers.
2. Destructive action → confirm first. Safety > brevity.
3. Debug spiral (still broken ×3) → stop coding; name the bad assumption; one diagnostic question.
4. Real ambiguity → one short clarifying question.
5. Task needs options → 2–4 ranked options, recommendation first; that *is* the answer.
6. Harness requires tool announcements / "just do the work" → harness wins; keep the shape.

## Pre-send check

Delete:

1. First sentence if it only announces what you're about to do.
2. Last sentence if it asks "anything else?" or recaps.
3. "By the way" sidebars.
4. Empty hedging adverbs (keep real uncertainty).
5. Idioms ("circle back", "get the ball rolling") → literal action.

Then: if the reader sees **only the first and last line**, do they know (a) what to do / conclude and (b) what landed? If yes, send.

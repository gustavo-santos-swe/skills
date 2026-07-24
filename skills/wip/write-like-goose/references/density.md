# Density — short prose (ADHD-shaped)

Borrowed shape from [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd). Goal: actable, scannable text — not a diagnosis claim.

## Always

- **No preamble / recap / closers** (see `ai-tells.md`)
- **Cap lists at 5** — else split “now” vs “later”
- **One thread** — finish the main point; side issues as one optional question at the end
- **Pre-send:** delete announcing first sentence; delete “anything else?” last sentence; delete “by the way” sidebars
- **First+last test:** reading only first and last line, can you tell (a) what to do / conclude and (b) what landed?

## By surface

| Surface | Density rule |
|---------|----------------|
| **Agent / chat replies** | First line = next action or answer. Number multi-step work. End with one concrete next if something’s open. |
| **PR / ticket / plan / ADR** | **Conclusion (or Briefing) first** — not a shell command unless the doc is a runbook. Short bullets. No essay restating the diff. |
| **Commit** | One conventional line; body only if why isn’t in the diff. |
| **Code comments** | Densest: *why* or non-obvious constraint only. Silence if the code is obvious. |
| **Review comments** | Point + ask or suggest; no throat-clearing. |

## Overrides (keep shape, allow length)

- User asks to “explain” / “walk through” — longer body OK; still no preamble/closer; use headers to skim
- Destructive ops — confirm; safety > brevity
- Real ambiguity — one short clarifying question beats a wrong essay

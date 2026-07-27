---
name: research
description: Cited decision brief from primary sources before design locks. Use for library/API/options research - not for building the feature.
metadata:
  area: goose
---

# Research

Goose handbook for **bounded, cited investigation** before design locks in.

Voice: **`write-like-goose`**.

## When to use

- “SMS vs email?”, “which library for X?”, “what does this API actually guarantee?”
- Need facts from docs/specs/source before **brainstorm** or **planning**
- Reading legwork that should outlive the chat

## When not to

- Design debate with options already known → **brainstorm**
- Build / spike code is the only way to learn → a short throwaway experiment under **implement** (not a research novel)
- Failure / flake / regression → **diagnose**
- Formal long-form report (market/policy/science deep dive) - say so; this skill stays a **decision brief**, not a whitepaper

## How it runs

**Same session by default.** Do the research here.

Opt into a background agent only when the user asks, or the source set is large enough that parallel reading clearly helps. Don’t background a 10-minute docs check by default.

## Steps

1. **Frame the question** - one sentence; success criteria (“enough to pick among A/B/C”).
2. **List candidate options** (usually 2-3). Don’t boil the ocean.
3. **Gather evidence** - primary-first (below). Timebox: prefer finishing a brief over exhaustive coverage.
4. **Write the decision brief** to disk (path below).
5. **Hand off** - point to the file; next skill is usually **brainstorm** (sharpen) or **planning** (if the what is already frozen).

## Sources

| Prefer | Use carefully |
|--------|----------------|
| Official docs, RFCs/specs, first-party API references | Blog posts, SO answers, secondary roundups - **leads only** |
| Library/source in the repo or upstream | Vendor marketing pages - verify in docs/code |
| Release notes / changelogs from the owner | LLM memory with no URL - not a cite |

Every hard claim in the brief needs a **primary** cite (URL or path). If you only have secondary noise, say so under open questions / uncertainty.

## Deliverable - decision brief

One Markdown file. Structure:

```markdown
# Research: <question>

**Date:** YYYY-MM-DD
**Status:** findings | lean

## Question
…

## Options
- A - …
- B - …

## Findings
- … ([source](url))

## Trade-offs
| Option | Pros | Cons |
|--------|------|------|

## Open questions
- …

## Lean (optional)
One short paragraph - or “no lean; needs brainstorm.”
```

No copy-pasteable production code required. No full POC unless the user explicitly asked for one (then keep it throwaway and tiny).

## Where to save

1. Match the **target repo’s** existing notes/docs convention if there is one.
2. Else: `docs/research/YYYY-MM-DD-<slug>.md` (create `docs/research/` if needed).
3. Tell the user the path when done.

## Guardrails

1. Hard claims need a **primary** cite (URL or path); secondary sources are leads only.
2. Deliver a **decision brief** on disk (not chat-only, not a whitepaper).
3. Stay in research - feature build / spikes belong in **implement**.

**Done when:** brief saved, path reported, next skill proposed.

## References

- [`references/brief-template.md`](references/brief-template.md) - copy-paste stub

## Next

- Sharpen approach → **brainstorm**
- What already frozen → **planning** (or **create-tickets** if multi-slice)
- Small clear change already decided → **implement**

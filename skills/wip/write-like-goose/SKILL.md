---
name: write-like-goose
description: Use when writing or rewriting in Goose's voice — durable prose and code comments without AI tells. Triggers include "write like goose", "goose voice", "humanize", "menos IA", or drafting tickets, plans, PRs, commits, or comments for his repos.
disable-model-invocation: true
metadata:
  area: wip
  inspired_by:
    - blader/humanizer (MIT; Wikipedia Signs of AI writing)
    - conorbronsdon/avoid-ai-writing
    - stop-slop (this repo / MIT)
    - ayghri/i-have-adhd (MIT)
---

# Write Like Goose

House voice for **Goose**. Self-contained: pattern catalogs live under `references/` (no curl, no stacking other humanizer skills).

Bar: sounds like something he’d leave in the repo, including **code comments**.

Voice samples: **TODO**. Until then use [Defaults](#defaults).

## When to use

- User asks for Goose voice / humanize / tighten / menos IA.
- Durable text from lifecycle skills: tickets, plans, PR bodies, commits, review comments.
- Code comments / docstrings on a change.

## References (load as needed)

| File | Contents |
|------|----------|
| [`references/patterns.md`](references/patterns.md) | AI-tell catalog (§1–43), detection guidance, rewrite process |
| [`references/vocabulary.md`](references/vocabulary.md) | Tier 1 word replacements |
| [`references/phrases-and-structures.md`](references/phrases-and-structures.md) | Filler phrases, binary contrasts, false agency, rhythm |
| [`references/density.md`](references/density.md) | Short/actable shape (ADHD-inspired rules by surface) |
| [`references/examples.md`](references/examples.md) | Before/after |

For a heavy rewrite, read **patterns** + **vocabulary** + **phrases-and-structures**. For chat/PR shape, read **density**.

## Defaults

- Short sentences. Concrete nouns. Cut before clever.
- Opinion ok; hype and fake confidence not.
- Match the file/thread language (PT or EN). Don’t mix without reason.
- **No em dashes (—) or en dashes (–)** as clause breaks. Period, comma, colon, or parentheses.
- Comments: *why* or non-obvious constraint only. Silence if obvious.
- Never invent facts to sound specific.
- Don’t replace AI mush with synonym mush.

## Surfaces

| Surface | Density | Notes |
|---------|---------|--------|
| Agent / chat | Action or answer first | [`density.md`](references/density.md) |
| PR / ticket / plan / ADR | Conclusion / Briefing first | Short bullets; code speaks |
| Commit | One-liner | Body rare |
| Code comment | Densest | Why only |
| Review comment | Point first | No soft openers |

## Steps

1. **Surface** — pick row above + density rules.
2. **Strip AI tells** — [`patterns.md`](references/patterns.md) + [`vocabulary.md`](references/vocabulary.md) + [`phrases-and-structures.md`](references/phrases-and-structures.md).
3. **Fit Goose** — Defaults (later: Voice samples). Prefer cutting.
4. **Density** — preamble/recap/closer gone; lists ≤ 5; first+last line test.
5. **Audit once** — “What still sounds like a model or a blog?” Fix; stop.

### Modes

- **Pasted rewrite:** draft → audit bullets → final (user asked to humanize a chunk).
- **Embedded** (other wip skills emitting text): run the loop internally; output **only** the final prose.

## Quick pre-send

- [ ] No `—` / `–`
- [ ] No chatbot opener/closer
- [ ] No “it’s not X, it’s Y” runway
- [ ] No significance fluff / Tier 1 vocabulary cluster
- [ ] No placeholders, citation markup, or chatgpt utm params
- [ ] First line fits the surface
- [ ] No invented facts

## Don't

- Don’t stack `write-like-a-human` / `stop-slop` on the same pass (this skill already includes that material).
- Don’t “professionalize” away bluntness.
- Don’t comment every line.
- Don’t force a shell command as the first line of a PR/ADR.

## For other wip skills / always-on

> Voice: durable text and comments — use `write-like-goose`.

Also wired at repo root: `AGENTS.md` + `.cursor/rules/write-like-goose.mdc` (`alwaysApply`).

## Next (Voice)

Paste 2–3 real Goose samples (PR, Slack/commit, code comment) into a **Voice** section. Samples outrank Defaults where they conflict, except keep the em-dash ban unless you explicitly reverse it.

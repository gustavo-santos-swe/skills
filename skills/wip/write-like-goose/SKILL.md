---
name: write-like-goose
description: Use when writing or rewriting in Goose's voice — durable prose and code comments without AI tells. Triggers include "write like goose", "goose voice", "humanize", "menos IA", or drafting tickets, plans, PRs, commits, or comments for his repos.
disable-model-invocation: true
metadata:
  area: wip
  inspired_by:
    - blader/humanizer
    - conorbronsdon/avoid-ai-writing
    - stop-slop / write-like-a-human (this repo)
    - ayghri/i-have-adhd
---

# Write Like Goose

House voice for **Goose**. Not a generic humanizer: after stripping AI tells, the bar is “sounds like something he’d leave in the repo,” including **code comments**.

Voice samples: **TODO** — until then use [Defaults](#defaults) + the anti-AI / density passes below.

## When to use

- User asks for Goose voice / humanize / tighten / menos IA.
- Durable text from lifecycle skills: tickets, plans, PR bodies, commits, review comments.
- Code comments / docstrings on a change.

## Relationship to other skills

- Prefer **this skill** over `write-like-a-human` / `stop-slop` when the audience is Goose’s repos. Don’t stack all three on one pass.
- Full AI-pattern encyclopedia: [blader/humanizer](https://github.com/blader/humanizer) — optional curl once per session. Local short list: [`references/ai-tells.md`](references/ai-tells.md).
- Density / action-first shape: [`references/density.md`](references/density.md).

## Defaults

Until Voice is filled with real samples:

- Short sentences. Concrete nouns. Cut before clever.
- Opinion ok; hype and fake confidence not.
- Match the file/thread language (PT or EN). Don’t mix without reason.
- **No em dashes** (—) or en dashes (–) as clause breaks. Prefer period, comma, colon, or parentheses.
- Comments explain *why* or a non-obvious constraint — never narrate the next line.

## Surfaces

| Surface | Notes |
|---------|--------|
| Prose (PR, ticket, plan, ADR) | Conclusion / Briefing first; short Changes; see density.md |
| Commit | Conventional one-liner; rare body |
| Code comment | Why only; omit if obvious |
| Review comment | Pointed; no soft openers |

## Steps

1. **Know the surface** — table above; pick density rules from [`references/density.md`](references/density.md).
2. **Strip AI tells** — [`references/ai-tells.md`](references/ai-tells.md); pull humanizer if the draft is still “model-shaped.”
3. **Fit Goose** — [Defaults](#defaults) (later: Voice samples). Prefer cutting over synonym swaps.
4. **Density pass** — first/last line test; kill preamble, recap, closers; lists ≤ 5.
5. **Audit once** — “What still sounds like a model or a blog post?” Fix; stop.

## Don't

- Don’t replace AI mush with synonym mush.
- Don’t “professionalize” away bluntness.
- Don’t comment every line.
- Don’t force a shell command as the first line of a PR/ADR (conclusion first is enough).
- Don’t invent facts to sound specific.

## For other wip skills

Emitters should point here with one line:

> Voice: durable text and comments — use `write-like-goose`.

## Next (when evolving Voice)

Paste 2–3 real Goose samples (PR, Slack/commit, code comment) into a **Voice** section and let them outrank Defaults where they conflict (except keep the em-dash ban unless you explicitly reverse it later).

---
name: write-like-goose
description: Goose voice (ASD-STE100 + anti-AI + density) for durable prose and code comments. Use when humanizing tickets, plans, PRs, commits, or comments, or when asked for goose voice / menos IA / STE rewrite.
metadata:
  area: goose
  inspired_by:
    - ASD-STE100 Issue 8 (Simplified Technical English)
    - blader/humanizer (MIT; Wikipedia Signs of AI writing)
    - conorbronsdon/avoid-ai-writing
    - stop-slop (this repo / MIT)
    - ayghri/i-have-adhd (MIT)
    - s-anand.net "Simple writing hurts thinking" (2026)
---

# Write Like Goose

House voice for **Goose**. Self-contained: pattern catalogs live under `references/` (no curl, no stacking other humanizer skills).

**Prose standard:** [**ASD-STE100**](references/ste100.md) (Simplified Technical English). Short, active, unambiguous. Then strip AI tells. Then apply surface density.

Voice samples: **TODO**. Until then use [Defaults](#defaults).

## When to use

- User asks for Goose voice / humanize / tighten / menos IA.
- Durable text from lifecycle skills: tickets, plans, PR bodies, commits, review comments.
- Code comments / docstrings on a change.
- Skill bodies during distill (`evolve-goose-skills`, `writing-great-skills` pass).

## References (load as needed)

| File | Contents |
|------|----------|
| [`references/ste100.md`](references/ste100.md) | **Primary.** Sentence limits, voice, tense, structure (ASD-STE100) |
| [`references/technical-names.md`](references/technical-names.md) | Approved domain terms for skills / SDLC prose |
| [`references/patterns.md`](references/patterns.md) | AI-tell catalog (§1-43), detection guidance, rewrite process |
| [`references/vocabulary.md`](references/vocabulary.md) | Tier 1 word replacements (STE-aligned swaps) |
| [`references/phrases-and-structures.md`](references/phrases-and-structures.md) | Filler phrases, binary contrasts, false agency, rhythm |
| [`references/density.md`](references/density.md) | Short/actable shape (ADHD-inspired rules by surface) |
| [`references/examples.md`](references/examples.md) | Before/after |

| Task | Load |
|------|------|
| Heavy rewrite (pasted text) | ste100 + technical-names + patterns + vocabulary + phrases-and-structures |
| Chat / PR / ticket / plan shape | ste100 + technical-names + density |

## Defaults

- Follow [`ste100.md`](references/ste100.md) for **English** prose: short sentences, active voice, one topic per sentence, American spelling.
- **Portuguese prose:** keep STE's simplicity (short sentences, one topic per sentence, active voice) without the English word list; STE does not cover PT.
- Concrete nouns. Cut before clever.
- Opinion ok in chat, review comments, and PR Notes. Keep ticket/ADR Briefing and code comments neutral. Hype and fake confidence not, anywhere.
- Match the file/thread language (PT or EN). Do not mix without reason.
- **No em dashes ( — ) or en dashes (–)** as clause breaks. Period, comma, colon, or parentheses.
- Comments: *why* or non-obvious constraint only. Silence if obvious.
- Never invent facts to sound specific.
- Do not replace AI mush with synonym mush.

## Surfaces

| Surface | STE type | Density | Notes |
|---------|----------|---------|--------|
| Agent / chat | Description (≤25); Procedure (≤20) per step | Action or answer first | [`density.md`](references/density.md); multi-step answers use Procedure shape per step |
| PR / ticket / plan / ADR | Mixed (see [ste100.md §Mixed](references/ste100.md#mixed-shape-pr-ticket-plan-adr)) | Conclusion / Briefing first | Short bullets; code speaks |
| Commit | Label ([`git-practices`](../git-practices/SKILL.md) owns format) | One-liner | git-practices sets `type(scope): description`; STE caps description length (≤20) and word choice only |
| Code comment | Description (≤25) | Densest | Why only |
| Review comment | Procedure (≤20) | Point first | No soft openers |
| Skill step | Procedure (≤20) | Imperative command | One instruction per step |

## Steps

1. **Surface**: pick row above, plus its STE type and density rules.
2. **STE pass**: apply [`ste100.md`](references/ste100.md) + [`technical-names.md`](references/technical-names.md): length, voice, articles, noun clusters, one name per referent.
3. **Strip AI tells**: apply [`patterns.md`](references/patterns.md) + [`vocabulary.md`](references/vocabulary.md) + [`phrases-and-structures.md`](references/phrases-and-structures.md).
4. **Fit Goose**: apply Defaults (later: Voice samples). Prefer cutting.
5. **Density**: cut preamble/recap/closer; cap lists at 5; run the first+last line test.
6. **Audit once**: ask "What still sounds like a model or a blog?" Recheck word limits (20 procedure / 25 description) since steps 3-5 can push a sentence back over. Fix; stop.

### Modes

- **Pasted rewrite:** draft → audit bullets → final (user asked to humanize a chunk).
- **Embedded** (other Goose skills emitting text): run the loop internally; output **only** the final prose.

## Quick pre-send

- [ ] STE limits (20 proc / 25 desc) and active/imperative where required
- [ ] No ` — ` / `–`
- [ ] No chatbot opener/closer
- [ ] No "it's not X, it's Y" runway
- [ ] No significance fluff / Tier 1 vocabulary cluster
- [ ] No placeholders, citation markup, or chatgpt utm params
- [ ] First line fits the surface
- [ ] No invented facts
- [ ] One technical name per referent

## Guardrails

1. Run this skill alone for voice - do not stack other humanizer skills on the same pass.
2. Keep bluntness; comments only when they carry a *why*.
3. PR/ADR first line = substance (not a shell command theater opener).
4. STE governs structure and word choice; density governs chat shape. Both apply.
5. **Precedence when layers conflict:** `git-practices` / `pr-raise` format wins for commit and PR-title shape. STE wins on word choice and sentence length elsewhere. Density wins on first-line and closer shape for chat. Never let STE block a required field or a skill's completion criterion (same escape `writing-great-skills` uses).
6. **Voice pass on final prose only.** Do not put STE constraints on reasoning or research. Think and draft at full complexity first, then rewrite. Constrained generation lowers reasoning quality.

## For other Goose skills / always-on

> Voice: durable text and comments - use `write-like-goose` (ASD-STE100 + anti-AI + density).

Also wired at repo root: `AGENTS.md` + `.cursor/rules/write-like-goose.mdc` (`alwaysApply`).

## Next (Voice)

Paste 2-3 real Goose samples (PR, Slack/commit, code comment) into a **Voice** section. Samples outrank Defaults where they conflict, except keep the em-dash ban and STE limits unless you explicitly reverse them.

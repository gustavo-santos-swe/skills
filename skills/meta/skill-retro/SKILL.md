---
name: skill-retro
description: Use when the user wants a skill retro, says capture this lesson, learn that into skills, or update skills from this session, or when you notice the same correction twice and should offer one retro (wait for OK before writing skill files). Covers Goose-wide absorb and product-repo local skills.
metadata:
  area: meta
---

# Skill Retro

Turn session lessons into skill updates. Prefer **absorb** into an existing Goose skill when the rule is house-wide. Use **local** for product-repo rules (brownfield deltas, team conventions). Hand big new Goose areas to **`evolve-goose-skills`**.

Voice: **`write-like-goose`**.  
Craft when drafting patches: **`writing-great-skills`**.

## When to use

- User says retro, capture this, learn that into skills, or update skills from this session
- End of a build or review with reusable house rules
- Brownfield “do it this way for new code” that must not change Goose defaults
- Same correction appeared twice: **offer once**, then wait

## When not to

- Greenfield skill area or full invent/garden → **`evolve-goose-skills`**
- Gap audit pitches only → **`suggesting-skills`**
- Prose craft of one body with no new lesson → **`writing-great-skills`**
- Fix product code from PR comments → **`pr-iterate`** (then retro if the rule should stick)

## Offer rule

When you see the same correction twice in a session, offer **skill-retro** once. Do not nag. Do not write skill files until the user OK.

## Steps

1. **Harvest** lessons from this session (corrections, house rules, “do it this way”). Use the [lesson card](references/lesson-card.md). Cap the list at 5; ask which to keep if more.
2. **Scope** each lesson: **Goose-wide** or **this product repo only**. Recommend + why; wait if unclear.
3. **Dispose** each lesson: **absorb** / **local** / **evolve** / **defer** / **drop**. See [absorb map](references/absorb-map.md) and [local skills](references/local-skills.md). Recommend + why; wait if ownership is unclear.
4. **Draft** proposed edits (path + short patch summary). Absorb → Goose `SKILL.md` or `references/`. Local → product `.claude/skills/…`. Evolve → one-paragraph pitch only.
5. **Get OK** before any skill file write. No silent edits.
6. **Apply** approved patches. Run **`writing-great-skills`** + **`write-like-goose`** on durable prose. For absorb: wire Goose inventory/`ask` only if a new pointer is required. For local: optional one-line pointer in the product `CLAUDE.md` / `AGENTS.md` if agents will not find the skill otherwise.
7. **Hand off** evolve dispositions to **`evolve-goose-skills`** (user must start or confirm that run).
8. **Offer ship** in the repo you edited (Goose skills repo and/or product repo) only if the user wants it. Leave dirty when they say leave dirty.

**Done when:** every kept lesson is absorb-applied, local-applied, evolve-handed, deferred with a one-line why, or dropped. No hanging “we should remember that.”

## Disposition ladder

| Disposition | When | Next |
|-------------|------|------|
| **absorb** | Goose-wide rule; an existing Goose skill owns the topic | Patch that Goose skill after OK |
| **local** | This product only (brownfield delta, team path, legacy vs new) | Write under product `.claude/skills/` after OK |
| **evolve** | Goose-wide; no owner, or needs a new Goose skill / area | Pitch → **`evolve-goose-skills`** |
| **defer** | Real lesson, not ready to encode | One-line why; stop |
| **drop** | One-off, taste-only, or already covered | Say so; stop |

Prefer **absorb** over **evolve**. Prefer **local** over **absorb** when the rule must not change Goose defaults.

## Don't

- Do not write skill files before the user OK
- Do not paste chat transcripts into the repo
- Do not create a new Goose skill when an existing Goose owner fits
- Do not put product-only rules into the Goose skills repo
- Do not use the name “goose” in product-repo skill paths or prose
- Do not offer a retro more than once for the same repeated correction
- Do not invent Goose web/mobile SOTA from one nit (need inspirations + evolve grill)

## Related

- Invent / garden → **`evolve-goose-skills`**
- Gap pitches → **`suggesting-skills`**
- Skill craft → **`writing-great-skills`**
- Voice → **`write-like-goose`**
- Router → **`ask`**

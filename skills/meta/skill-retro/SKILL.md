---
name: skill-retro
description: Use when the user wants a skill retro, says capture this lesson, learn that into skills, or update skills from this session, or when you notice the same correction twice and should offer one retro (wait for OK before writing skill files).
metadata:
  area: meta
---

# Skill Retro

Turn session lessons into Goose skill updates. Prefer **absorb** into an existing skill. Hand big new areas to **`evolve-goose-skills`**.

Voice: **`write-like-goose`** (**ASD-STE100**).  
Craft when drafting patches: **`writing-great-skills`**.

## When to use

- User says retro, capture this, learn that into skills, or update skills from this session
- End of a build or review with reusable house rules
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
2. **Dispose** each lesson: **absorb** / **evolve** / **defer** / **drop**. Prefer absorb. See [absorb map](references/absorb-map.md). Recommend + why; wait if ownership is unclear.
3. **Draft** proposed edits (skill path + short patch summary). For absorb: target `SKILL.md` or `references/`. For evolve: one-paragraph pitch; do not invent the full skill here.
4. **Get OK** before any skill-repo file write. No silent edits.
5. **Apply** approved absorb patches. Run **`writing-great-skills`** + **`write-like-goose`** on durable prose. Wire inventory/`ask` only if a new pointer is required.
6. **Hand off** evolve dispositions to **`evolve-goose-skills`** (user must start or confirm that run).
7. **Offer ship** (branch / commit / PR) only if the user wants it. Leave dirty when they say leave dirty.

**Done when:** every kept lesson is absorb-applied, evolve-handed, deferred with a one-line why, or dropped. No hanging “we should remember that.”

## Disposition ladder

| Disposition | When | Next |
|-------------|------|------|
| **absorb** | An existing Goose skill owns the topic | Patch that skill after OK |
| **evolve** | No owner, or needs a new skill / area | Pitch → **`evolve-goose-skills`** |
| **defer** | Real lesson, not ready to encode | One-line why; stop |
| **drop** | One-off, taste-only, or already covered | Say so; stop |

## Don't

- Do not write skill files before the user OK
- Do not paste chat transcripts into the repo
- Do not create a new skill when an existing owner fits
- Do not offer a retro more than once for the same repeated correction
- Do not invent Goose web/mobile SOTA from one nit (need inspirations + evolve grill)

## Related

- Invent / garden → **`evolve-goose-skills`**
- Gap pitches → **`suggesting-skills`**
- Skill craft → **`writing-great-skills`**
- Voice → **`write-like-goose`**
- Router → **`ask`**

---
name: evolve-goose-skills
description: Evolve this skills repo - iterate (inspire → decide → grill → distill → ship) or garden (prune / absorb / fill). Use when adding skill areas, sharing inspirations, or cleaning inventory.
metadata:
  area: meta
---

# Evolve Goose Skills

House process for **this repo** (`gustavo-santos-swe/skills`). Stops re-teaching how we invent, grill, absorb, and ship Goose skills.

Voice: **`write-like-goose`**.  
Craft of one `SKILL.md`: **`writing-great-skills`** (load when drafting bodies).  
Gap pitches only: **`suggesting-skills`** (optional helper inside garden).

## When to use

- New topic / stack / area (“I have inspirations for web…”)
- “Evolve skills”, “garden the repo”, “what should we prune”
- End of a session that changed how we work on skills - capture the lesson
- Before teaching the agent the ritual again from scratch

## When not to

- Writing one skill’s prose craft only → **`writing-great-skills`**
- Product feature SDLC in an app repo → **`goose/ask`** and lifecycle
- Blind import of upstream trees without distill + grill

## Branches

Pick one (or run iterate then garden):

| Branch | Job |
|--------|-----|
| **`iterate`** (default) | Inspirations → need → questionnaire → distill → voice → ship |
| **`garden`** | Inventory, absorb/delete/fill stubs, ownership drift, README sync |

Load the playbook once per run: [`references/playbook.md`](references/playbook.md).  
Questionnaire shape: [`references/questionnaire.md`](references/questionnaire.md).

---

## Branch: iterate

**Done when:** user picked what to build (or deferred); grilled decisions frozen; skill(s) drafted or planned; ship path clear (or explicit “leave dirty”).

1. **Orient** - skim `skills/goose/README.md`, root inventory, relevant area. Note filled vs stubs.
2. **Inspirations** - collect what the user shared (repos, skills, notes). Summarize candidates; don’t copy wholesale.
3. **Need** - for each candidate: keep / absorb into existing / defer / drop. Prefer absorb over a parallel skill. Rank by frequency × pain if many.
4. **Questionnaire** - grill **one decision at a time** per [`questionnaire.md`](references/questionnaire.md). Recommend + why; wait. Cover purpose, non-goals, ownership, branches, invocation.
5. **Approaches** - always 2-3 shapes before locking (even for “small”).
6. **Freeze** - Established so far: purpose, non-goals, approach, key decisions. Get explicit OK.
7. **Distill** - draft Goose-owned `SKILL.md` (+ refs). Self-contained body; `inspired_by` in metadata only. Apply **`writing-great-skills`**. Voice pass **`write-like-goose`**.
8. **Wire** - area README, root inventory, cross-refs (`ask` / pack maps if lifecycle).
9. **Ship** - feature branch, commit (`git-practices`), PR (`pr-raise`). Merge only if user says ship/merge.

Update [`references/playbook.md`](references/playbook.md) when this session **changes the ritual** (new rule that should stick). Don’t append noise.

---

## Branch: garden

**Done when:** inventory actions proposed; user picks which to apply; applied changes wired; ship path clear.

1. **Inventory** - list areas and skills; flag stubs, duplicates, stale paths, orphan READMEs.
2. **Triage** - buckets: remove / absorb into Goose / keep as satellite / fill later / leave alone.
3. **Ownership** - check SoT conflicts (voice, git, PR, grounding, simplify, deep-modules). One owner each.
4. **Optional** - run **`suggesting-skills`** if the user wants gap pitches from recent chats.
5. **Apply** - only what the user approved. Prefer delete+absorb over “keep both and document.”
6. **Wire + ship** - same as iterate steps 8-9.

---

## Guardrails

1. Do not invent Goose SOTA for web/mobile - wait for user’s inspirations + grill.
2. Do not stack duplicate upstream skills when a Goose owner exists.
3. One question at a time in questionnaires; recommend first.
4. Playbook is SoT for *process*; don’t fork a second process doc in AGENTS.md (pointer only).

## Related

- Craft → **`writing-great-skills`**
- Gap audit → **`suggesting-skills`**
- Lifecycle map → **`goose/ask`** / [`goose/README`](../../goose/README.md)
- Voice → **`write-like-goose`**

# Goose skills playbook

How we evolve **this** skills repo. Distilled from the sessions that built `goose/` and pruned upstream duplicates. Update this file when the ritual itself changes.

## North star

- Goose owns the **SDLC** (`skills/goose/`) and filled **stack packs** (today: `database`, `dotnet`).
- Web / mobile structure vs stylish stay split; fill when the user brings SOTA inspirations - don’t invent.
- Prefer **fewer trusted skills** over a museum of imports.

## Ritual (iterate)

```
survey inspirations → decide need → grill questionnaire → distill Goose skill
  → writing-great-skills pass → write-like-goose → wire inventory → PR → [merge if ship]
```

1. **Survey, don’t clone.** Popular upstream skills are raw ore. Extract the job and the few rules that change agent behavior.
2. **Decide need first.** Keep / absorb / defer / drop. Absorb into an existing Goose skill when the job overlaps (example: review smells → `pr-review`, simplify → `implement`).
3. **Grill before draft.** One question per message; multiple choice when options are real; always give a recommendation + why. Same energy as product brainstorm, scoped to skill design.
4. **Freeze the what.** Established so far (purpose, non-goals, approach, ownership). Explicit OK before writing files.
5. **Distill self-contained Goose skills.** Body has no “see Matt/obra for the real process.” Metadata may list `inspired_by`. `disable-model-invocation: true` for lifecycle / meta process skills unless there’s a clear auto-trigger need.
6. **Craft + voice.** `writing-great-skills` for predictability; `write-like-goose` for durable prose.
7. **Wire the map.** Root README + area README + `goose/ask` (if routing changes). Dead links are bugs.
8. **Ship.** Feature branch → conventional commit → PR. User says **ship** / **merge** before landing on `main`. Agent does not merge by default (`pr-raise`).

## Ritual (garden)

```
inventory → triage (remove / absorb / keep / fill later) → fix ownership → apply approved → wire → PR
```

- **Remove soon:** duplicates of Goose lifecycle, unused routers, tools we won’t run.
- **Strong candidates:** near-duplicates (TDD, debug, humanizers) once Goose covers the job.
- **Leave alone:** intentional satellites (`improve-codebase-architecture`, deep `mobile/*` technique) until the user decides.
- After absorb: delete the upstream copy; retarget refs; don’t leave “prefer X” wrappers forever.

## Ownership (single SoT)

| Concern | Owner |
|---------|--------|
| House voice | `write-like-goose` (+ AGENTS / Cursor rule) |
| Branch + commit messages | `git-practices` |
| PR title/body/open | `pr-raise` |
| PR review | `pr-review` |
| PR feedback loop | `pr-iterate` |
| Build + dirty tree + optional polish | `implement` |
| Ticket grounding / SoT drift | `create-tickets` |
| Domain glossary / CONTEXT | `brainstorm` (+ `documentation:adr`) |
| Greenfield shape + platform presence (in/out/later) | `brainstorm` branch `greenfield` (surfaces in pack `references/greenfield-decision-surface.md`) |
| Deep-module vocabulary | `codebase-design` |
| Skill craft (predictability) | `writing-great-skills` |
| Skill-repo evolution ritual | **this skill** (`evolve-goose-skills`) |

If two skills claim the same concern, garden until one owns it.

## Pack load

- `implement` loads the active pack’s README + every `SKILL.md` (refs on demand).
- Context cost is accepted on large windows; revisit only if dogfooding shows agents ignore half the pack.
- Stubs (RN / frontend) are OK until the user brings inspirations.

## Anti-patterns

- Importing a full upstream tree “for later”
- Parallel skills for the same job (“Matt brainstorm” + `goose/brainstorm`)
- Teaching the ritual in chat every session instead of loading this playbook
- Filling web/mobile SOTA from model priors without user inspirations + grill
- Expanding AGENTS.md into a second playbook (link here instead)

## Session capture

When a chat **changes** how we work (new absorb rule, new ship meaning, new area split):

1. Patch this playbook (short bullet or ownership row).
2. Mention the change in the PR Briefing.
3. Don’t dump transcripts into the repo - distill the rule only.

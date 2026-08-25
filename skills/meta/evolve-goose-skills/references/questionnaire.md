# Skill questionnaire

Grill **one question per message**. Prefer A/B/C when options are real. Always lead with **your recommendation + why**, then wait.

Word every ask per **`write-like-goose` Question surface**: what is being decided, what each option changes, recommendation + why. Use the harness question form when the choice is real. Do not ask a label plus "Which?".

Use for new skills, new packs, or absorb-vs-keep decisions. Skip sections the freeze already settled.

## Core (almost always)

1. **Job** - What repeated failure or repeated explanation does this skill remove?
2. **Trigger** - When does the user invoke it? (phrases / situations)
3. **Non-goals** - What must it refuse so it doesn’t sprawl?
4. **Owner vs existing** - New skill, or absorb into which Goose skill? (recommend absorb when overlap is real)
5. **Invocation** - User-invoked (`disable-model-invocation: true`) vs model-invoked? Default user-invoked for process/lifecycle.
6. **Branches** - One path or named branches? (only if runs differ enough to earn the split)
7. **SoT / refs** - What lives in `SKILL.md` vs `references/`?

## Placement

8. **Area** - `goose` lifecycle, `goose/implement/<pack>`, `meta`, satellite (`design` / `mobile` / `engineering`)?
9. **Router** - Does `goose/ask` need a new row? Pack README map?

## Quality bar

10. **Done-when** - Checkable completion for a run of this skill?
11. **Failure modes** - Premature completion, duplication, sediment - what should Guardrails block?

## After freeze

- 2-3 approaches if shape still open
- Established so far → user OK → draft with `writing-great-skills` + `write-like-goose`

## Example shape (agent → user)

> **Q3. Owner.** Where should the review-smell baseline live?
>
> A second review skill next to `pr-review` will rot: two owners, two checklists, neither stays current.
>
> Absorbing into `pr-review` keeps one SoT. A thin satellite only pays off if another surface (local diff, not a PR) needs the same smells without loading PR review.
>
> I recommend absorb. Goose already owns PR review.
>
> **A)** Absorb into `pr-review` _(recommended)_
> **B)** Keep a thin satellite skill
> **C)** Drop the idea

Put that whole ask in the harness question form when the choice is real.

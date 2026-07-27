# Skill questionnaire

Grill **one question per message**. Prefer A/B/C when options are real. Always lead with **your recommendation + why**, then wait.

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

> **Q3 - Owner:** Absorb the smell baseline into `pr-review` rather than keep `code-review`.  
> **Why:** Goose already owns PR review; a second review skill will rot.  
> **A)** Absorb into `pr-review` _(recommended)_  
> **B)** Keep a thin satellite skill  
> **C)** Drop the idea  
>
> Which?

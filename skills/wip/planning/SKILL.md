---
name: planning
description: Use when an agreed design or frozen what needs a concrete implementation plan (ordered tasks, files, risks, done-when) before tickets or code. Not for sharpening the idea (brainstorm) or building yet (implement).
disable-model-invocation: true
metadata:
  area: wip
---

# Planning

Goose handbook for turning a frozen **what** into a durable **how**: ordered tasks, touch points, risks, and a clear next skill.

Voice: **`write-like-goose`**.

## When to use

- Brainstorm (or equivalent) already froze purpose, approach, non-goals
- Need task order, files, risks, and done-when before **create-tickets** or **implement**
- Work is multi-step enough that chat alone will lose the thread

## When not to

- Design still fuzzy → **brainstorm**
- Need facts/libraries first → **research**, then return (or brainstorm)
- Single obvious change, already decided → **implement** (skip the plan file)
- Failure / flake / regression → **diagnose**
- Ticket graph is the ask and the plan already exists → **create-tickets**

## How it runs

**Same session by default.** Write the plan here.

Opt into a background agent only when the user asks, or the plan is large enough that parallel codebase recon clearly helps. Don't background a short slice plan by default.

## Prerequisites

You need a frozen **what**. Acceptable sources:

- Brainstorm **Established so far** (chat or brief)
- ADR / research lean already locked
- User-supplied spec that states purpose, approach, and non-goals

If the what is still open, stop and run **brainstorm** (or **research** for a fact gap). Don't invent design decisions inside the plan.

## Steps

1. **Confirm the freeze**: one sentence goal + approach + non-goals. If anything material is open, bounce out (above).
2. **Scope check**: multiple independent subsystems? Split into separate plans (one working, testable outcome each). Don't plan a platform as one blob.
3. **Orient on the repo**: relevant files, patterns, ADRs, `CONTEXT.md`. Prefer existing seams; no unrelated refactors in the plan.
4. **Map files**: list create / modify / test paths and what each is for. Lock decomposition here before task prose.
5. **Write ordered tasks**: vertical slices when the work spans layers. Each task gets files, done-when, dependencies, test seams (below).
6. **Risks + open questions**: only what could block or reshape the build. Defer execution unknowns to **implement**.
7. **Self-review**: coverage vs freeze, no placeholders, names/types consistent across tasks.
8. **Save + hand off**: path below; next skill by size (below).

## Plan depth (Goose default)

Enough that a fresh session can start without re-deriving the design. Not a novel, not a paste of production code.

| Include | Skip |
|---------|------|
| Goal, architecture (2-3 sentences), constraints worth repeating | Re-arguing the brainstorm approaches |
| Exact repo-relative file paths | Absolute machine paths |
| Ordered tasks with dependencies | 2-5 minute micro-steps and full code dumps |
| Done-when / acceptance per task | "Add appropriate error handling" placeholders |
| Test seams + scenarios the implementer must cover | Full red-green-commit choreography (that is **implement** / TDD) |
| Interface sketches only when signatures are the decision | Copy-pasteable production implementations |
| Risks that change sequencing or design | Speculative polish |

Right-size: a small change can be a short plan (goal + file map + 2-4 tasks). Large work gets more tasks, not denser prose.

## Task shape

Prefer **vertical slices** (narrow path through the layers that leaves something demoable or verifiable) over horizontal "all schema, then all API, then all UI."

Wide mechanical renames / shared-type rewrites are the exception: sequence expand → migrate batches → contract so each step can stay green. Deep ticket graphs with blockers belong in **create-tickets**; the plan should still show that sequence.

Each task:

```markdown
### Task N: <short name>

**Files:**
- Create: `path`
- Modify: `path`
- Test: `path`

**Depends on:** none | Task K, …

**Done when:**
- …

**Test seams:** what to prove (scenarios / commands if known). Test-first at these seams during **implement**.

**Notes:** interface sketch or constraint only if the signature *is* the decision.
```

## Deliverable: implementation plan

One Markdown file. Structure:

```markdown
# Plan: <feature>

**Date:** YYYY-MM-DD
**Status:** ready | blocked
**Source:** link or pointer to freeze / ADR / brief

## Goal
One sentence.

## Approach
2-3 sentences. Constraints that every task inherits.

## File map
| Path | Action | Responsibility |
|------|--------|----------------|

## Tasks
### Task 1: …
### Task 2: …

## Risks
| Risk | Why it matters | Mitigation |
|------|----------------|------------|

## Open questions
- … (empty if none; otherwise set Status: blocked)

## Next
create-tickets | implement (and why)
```

No TBD / TODO / "similar to Task N" / "handle edge cases" without saying which. If a fact is missing, Status: **blocked** and list the question (then **research** or human).

## Where to save

1. Match the **target repo’s** existing plans/docs convention if there is one (`AGENTS.md`, existing `docs/plans/`, etc.).
2. Else: `docs/plans/YYYY-MM-DD-<slug>.md` (create `docs/plans/` if needed).
3. Tell the user the path when done.

## Self-review

- [ ] Every freeze requirement maps to a task (or an explicit non-goal)
- [ ] No placeholder language
- [ ] Names, types, and paths stay consistent across tasks
- [ ] Each task leaves a verifiable state; order respects dependencies
- [ ] Multi-subsystem work was split or explicitly sequenced

## Handoff

| Plan shape | Next |
|------------|------|
| Several slices, parallel tracks, or needs a tracker graph | **create-tickets** |
| One small slice, clear files, can finish in one implement pass | **implement** |
| Hard-to-reverse decision still unsettled | **documentation:adr** first, then return |
| Fact gap blocks the plan | **research**, then revise |

Point at the file. Don't start coding under the guise of planning. Don't open the PR from here.

## Don't

- Don't invent product/design decisions the freeze didn't make
- Don't dump full production code into the plan
- Don't choreograph every TDD micro-step here; name seams, build under **implement**
- Don't skip the file and leave the plan only in chat (unless the user asked for chat-only and the slice is tiny)
- Don't use absolute paths
- Don't jump to **implement** when the work clearly needs tickets first

## References

- [`references/plan-template.md`](references/plan-template.md): copy-paste stub

## Next

- Multi-slice → **create-tickets**
- Single small slice → **implement** (load stack packs by concern)
- Missing decision → **documentation:adr** or **brainstorm**
- Missing fact → **research**

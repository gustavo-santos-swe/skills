---
name: planning
description: Use when an agreed design or frozen what already exists and you need a concrete implementation plan before tickets or code — ordered tasks, files, risks, verification.
disable-model-invocation: true
metadata:
  area: wip
---

# Planning

Goose handbook for turning a frozen *what* into a durable *how*: ordered tasks, touch points, risks, verification.

Voice: **`write-like-goose`**.

## Hard gate

Do **not** write production code, scaffold apps, open PRs, or run **`implement`** / **`create-tickets`** until the plan is written and the user OKs the handoff path.

Sketching a signature or SQL shape in the plan file is fine when that *is* the decision. Shipping code under the guise of planning is not.

## When to use

- Brainstorm (or equivalent) already froze purpose, approach, non-goals
- Need task order, files, risks, and verify steps before building
- Work is bigger than “one obvious edit” but not yet tickets

## When not to

- Design still fuzzy → **`brainstorm`**
- Need facts / library truth first → **`research`**
- Single small clear change already decided → skip; go **`implement`**
- Tickets already exist and are agent-ready → **`implement`** per ticket
- Failure / flake / regression → **`diagnose`**

## How it runs

**Same session by default.** Write the plan here.

Opt into a background agent only when the user asks, or the scope is large enough that parallel reading clearly helps. Don’t background a short plan by default.

## Steps

1. **Confirm the freeze** — purpose, chosen approach, non-goals, done-when. Missing or contested → back to **`brainstorm`** (or **`research`** if it’s a fact gap).
2. **Scope check** — multiple independent subsystems? Split into separate plans (one working slice each). Don’t stuff a platform into one plan.
3. **Map files** — list creates / modifies / tests and what each is for. Prefer existing patterns; propose a split only when a file you’re touching is already unwieldy and the split serves this goal.
4. **Slice vertically** — each task is a narrow end-to-end path that leaves the system working and testable. Not “all schema, then all API, then all UI.”
5. **Order + risks** — dependency order; put high-risk work early. Note blast-radius / expand-contract when a wide mechanical change can’t stay green as a tracer bullet.
6. **Write the plan** to disk (path below). Use the deliverable shape.
7. **Self-review** (below). Fix inline.
8. **Handoff** — point at the file; pick next skill (below). Wait for user OK before invoking it.

## Deliverable — implementation plan

One Markdown file. Structure:

```markdown
# Plan: <feature>

**Date:** YYYY-MM-DD
**Status:** draft | ready
**Source:** path to brainstorm brief / ADR / ticket (if any)

## Goal
One sentence.

## Approach
2–3 sentences. Link settled decisions; don’t re-litigate brainstorm.

## File map
| Path | Action | Responsibility |
|------|--------|----------------|
| `src/…` | create / modify | … |

## Tasks

### Task 1: <title>
**Delivers:** end-to-end behaviour this slice makes work
**Files:** create/modify/test paths
**TDD seam:** where (or “none — config/docs only”)
**Depends on:** none | Task N
- [ ] Steps (one action each)
- [ ] Verify: exact command + expected signal

### Task 2: …
…

## Risks
| Risk | Why it matters | Mitigation |
|------|----------------|------------|

## Out of scope
- …

## Open questions
- … (blockers only; otherwise decide and record)
```

No novel-length code dumps. Exact paths and verify commands yes. Interface sketches only when the signature *is* the lock.

## Task depth (Goose default)

| Include | Skip |
|---------|------|
| Exact file paths | Full test/impl source for every micro-step |
| Ordered checkbox steps | “Add appropriate error handling” vagueness |
| Verify command + expected signal | TBD / TODO / “similar to Task N” |
| Named TDD seams | Red-green ritual spelled out (that’s **`implement`**) |
| Risks + out of scope | Machine ID taxonomies (REQ-001…) unless the repo already uses them |

Right-size: each task fits one focused session. If you can’t state acceptance in ~3 bullets, or the title needs “and,” split it.

## Where to save

1. Match the **target repo’s** existing plans/docs convention if there is one.
2. Else: `docs/plans/YYYY-MM-DD-<slug>.md` (create `docs/plans/` if needed).
3. Tell the user the path when done. Commit only if they want it committed.

## Self-review

After writing the plan:

1. **Freeze coverage** — every settled requirement maps to a task?
2. **Placeholder scan** — TBD, TODO, “handle edge cases,” “write tests later”? Fix or cut.
3. **Order** — dependencies respected; each task leaves something verifiable?
4. **Consistency** — names/types/paths agree across tasks?

Fix inline. No second ceremony pass.

## Handoff

| Situation | Next |
|-----------|------|
| Multi-slice / multi-session / needs blockers on a tracker | **`create-tickets`** |
| Single small slice; build now in this session | **`implement`** |
| Hard decision still unresolved | **`documentation:adr`** or return to **`brainstorm`** |
| Fact gap blocks a task | **`research`**, then amend the plan |

Offer the path; don’t auto-start implement or ticket publish without an OK.

## Don't

- Don’t implement or scaffold during planning
- Don’t skip the file and leave the plan only in chat
- Don’t paste a full codebase into the plan
- Don’t force TDD micro-steps into the plan doc (**`implement`** owns the ritual)
- Don’t re-open settled brainstorm choices without a new fact
- Don’t plan horizontal layers as the primary breakdown
- Don’t invent file paths that aren’t in the repo (or clearly new)

## References

- [`references/plan-template.md`](references/plan-template.md) — copy-paste stub

## Next

- Multi-slice → **`create-tickets`**
- One small slice → **`implement`**
- Freeze cracked → **`brainstorm`** / **`research`**

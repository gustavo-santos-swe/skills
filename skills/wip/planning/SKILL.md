---
name: planning
description: Turn an agreed design into a concrete implementation plan — ordered tasks, files, risks, verify steps. Use when the what is frozen and you need the how before tickets or build. Do not implement during this skill.
disable-model-invocation: true
metadata:
  area: wip
---

# Planning

Goose handbook for the **how** after the **what** is settled (**brainstorm** / research / clear spec).

Voice: **`write-like-goose`**.

## When to use

- Design is frozen; need ordered build steps before coding
- Scope is bigger than a one-liner change
- User asks for a plan, breakdown, or “don’t code yet”

## When not to

- Still choosing among approaches → **brainstorm** (or **research** for facts)
- Single obvious file tweak → **implement** (skip a formal plan)
- Failure / flake → **diagnose**
- Already have agent-ready tickets → **implement** per ticket

## Hard rule

**Plan file only.** Read and explore the repo as needed. Write **only** the plan markdown — no feature implementation, no “quick start” commits, no drive-by refactors.

## Depth

**Actionable, not a novel.**

Include:

- Goal (one sentence)
- Approach (2–3 sentences) + assumptions
- File map (create / modify / test paths)
- Ordered tasks with **acceptance** (how you know the task is done)
- Verify commands where useful (exact enough to run)
- Risks, open questions, out of scope

Sketch interfaces/signatures when they unblock later tasks. **Do not** paste full production implementations for every step. Call out **TDD at agreed seams** (failing test → minimal code → pass) without turning the plan into 2–5 minute micro-essays.

No placeholders: no TBD/TODO, no “add validation later,” no “similar to Task N” without repeating the needed detail.

## Steps

1. Confirm the **what** is frozen. If not, stop and route back.
2. Scope check — independent subsystems → separate plans (or note split for **create-tickets**).
3. Map files and dependencies (foundations before dependents; prefer **vertical** slices over “all DB then all API then all UI”).
4. Write tasks (above depth bar).
5. Self-check: every requirement has a task; no placeholders; names/types consistent across tasks.
6. Save the plan; state the path; propose next skill (below).

## Where to save

1. Match the **target repo’s** existing plans convention if there is one.
2. Else: `docs/plans/YYYY-MM-DD-<slug>.md` (create `docs/plans/` if needed).

## Next

| Situation | Next |
|-----------|------|
| Multi-slice, multi-session, or parallelizable work | **create-tickets** |
| One small slice that fits a single context | **implement** |

Ask which path if unclear — default is size-based as above.

## Don't

- Don’t implement during planning
- Don’t write novel-length plans with full code in every step
- Don’t leave findings only in chat — save the file
- Don’t plan horizontal “layers first” when vertical slices would demo sooner
- Don’t invent file paths that don’t match the repo’s layout

## References

- [`references/plan-template.md`](references/plan-template.md) — starter skeleton

## Related

- Facts before design → **research**
- Freeze the what → **brainstorm**
- Split for tracker → **create-tickets**
- Build → **implement** (+ stack packs)

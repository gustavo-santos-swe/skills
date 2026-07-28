---
name: planning
description: Actionable implementation plan (tasks, files, verify) - no feature code. Use when the what is frozen and you need the how.
metadata:
  area: goose
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

**Plan file only.** Read and explore the repo as needed. Write **only** the plan markdown - no feature implementation, no “quick start” commits, no drive-by refactors.

## Depth

**Actionable, not a novel.**

Include:

- Goal (one sentence)
- Approach (2-3 sentences) + assumptions
- File map (create / modify / test paths)
- Ordered tasks with **acceptance** (how you know the task is done)
- Verify commands where useful (exact enough to run)
- Risks, open questions, out of scope

Sketch interfaces/signatures when they unblock later tasks. **Do not** paste full production implementations for every step. Call out **TDD at agreed seams** (failing test → minimal code → pass) without turning the plan into 2-5 minute micro-essays.

No placeholders: no TBD/TODO, no “add validation later,” no “similar to Task N” without repeating the needed detail.

## Steps

1. Confirm the **what** is frozen. If not, stop and route back.
2. If the freeze came from **`brainstorm`** branch **`greenfield`**: copy **in / out / later** into Assumptions / Out of scope. Do not plan work for **out**/**later** unless the user reopens them. Do not re-grill Shape.
3. Scope check - independent subsystems → separate plans (or note split for **create-tickets**).
4. Map files and dependencies (foundations before dependents; prefer **vertical** slices over “all DB then all API then all UI”).
5. Write tasks (above depth bar).
6. Self-check: every requirement has a task; no placeholders; names/types consistent across tasks; greenfield **in** concerns have tasks.
7. Save the plan; state the path; propose next skill (below).

## Where to save

1. Match the **target repo’s** existing plans convention if there is one.
2. Else: `docs/plans/YYYY-MM-DD-<slug>.md` (create `docs/plans/` if needed).

## Next

| Situation | Next |
|-----------|------|
| Multi-slice, multi-session, or parallelizable work | **create-tickets** |
| One small slice that fits a single context | **implement** |

Ask which path if unclear - default is size-based as above.

## Guardrails

1. Write **only** the plan file this run (explore the repo as needed; no feature code).
2. Prefer vertical slices and real repo paths; save the plan (never chat-only).
3. Depth = actionable tasks + acceptance + verify - not a code novel.

**Done when:** plan saved at the chosen path, self-check passed, next skill proposed.

## References

- [`references/plan-template.md`](references/plan-template.md) - starter skeleton

## Related

- Facts before design → **research**
- Freeze the what → **brainstorm**
- Split for tracker → **create-tickets**
- Build → **implement** (+ stack packs)

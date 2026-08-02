---
name: create-tickets
description: Tracer-bullet issues with blockers, grounded in a source of truth. Use to split a plan/spec for implement; tracker or plan markdown - not a local ticket tree.
metadata:
  area: goose
---

# Create Tickets

Goose handbook for turning a plan (or frozen spec) into **agent-ready vertical slices** with blockers and a clear **source of truth**.

Voice: **`write-like-goose`**.

This skill owns **grounding / drift** for the lifecycle. **implement** and **pr-iterate** point here when reality diverges from the cited source of truth.

## When to use

- Plan is multi-slice, multi-session, or parallelizable
- Need tracker issues (or an ordered slice list on the plan) before **implement**
- User says “break into tickets”, “make Linear issues”, “tracer bullets”
- **verify** (full audit) produced a Drift/Gap report to turn into a fixable backlog

## When not to

- One small slice that fits a single context → **implement** from the plan
- Design still mushy → **brainstorm** (or **research** for facts)
- Already have agent-ready tickets → **implement** on the frontier

## Hard rules

1. **Approve the breakdown before publish.** Quiz titles, blockers, and what each delivers. Iterate until the engineer says go. Then create.
2. **No parallel local ticket tree.** If no tracker tool is chosen, keep slices on the **plan markdown** (checkboxes / task status). Do not write `.scratch/.../issues/` or `docs/tickets/` as a second backlog.
3. **Ground before you invent.** Search the repo for the source of truth (OpenAPI/proto, ADR, project brief, existing ticket). If a new API or greenfield has none, stop and ask: path to use, or “open - freeze the contract in the ticket/plan.”
4. **Tickets describe outcomes**, not a second plan novel. File maps stay in **planning**.

## Slice shape

**Vertical tracer bullets.** Each issue is a narrow end-to-end path (schema + API + UI + tests as needed for *that* behaviour). Demoable or verifiable alone. Sized for one fresh context window.

Prefer vertical over “all DB, then all API, then all UI.”

**Exception - wide mechanical refactors** (rename/retype with huge blast radius): don’t fake a vertical slice. Sequence **expand → migrate batches → contract**. Each batch is its own issue; contract blocked by every migrate. If batches can’t stay green alone, share an integration branch and a final integrate-and-verify issue.

Prefactors that unblock the slices come first.

## Hierarchy (Linear-shaped)

Target shape: **Epic → Feature → Issues**, with **blocking edges** between issues (native blocker links when the tracker has them; otherwise a “Blocked by” field).

At quiz time, **propose Features** - engineer merges/splits/skips. Soft default: skip Feature when there is only one workstream (Epic → Issues). Don’t invent empty Features.

If the tracker isn’t Linear, map as close as you can (GitHub: parent issue / sub-issues or linked issues + labels). Same content, different buttons.

## Input: a verify report

A **verify** full-audit report is a valid plan input, but it is rows, not slices - one row per rule by design (verify's own hard rule). Turning it into a backlog needs one extra pass this skill owns and verify does not:

1. **Dedup by root cause, not by row.** Many Drift rows across different skills point at the same fix (e.g. "domain entities returned raw" shows up under `application-layer`, `db-integration`, `endpoint-conventions`, and `serialization` as four rows - it is one slice, not four). Group rows whose evidence converges on the same file/handler/pattern; list every `skill: rule` the slice closes so traceability back to the report survives.
2. **Source of truth is the pack rule + the report row, not a fresh preflight search.** Skip the generic grounding preflight for this input type - the SoT is already the cited `SKILL.md` rule plus the report's `path:line` evidence. Cite both on the slice.
3. **Order by severity tier, not skill alphabetical order or row count.** Auth-bypass / secrets-in-logs / IDOR first, then data-integrity (missing FKs, no transaction boundary, no concurrency control), then convention drift (naming, layering, missing DTOs), then test coverage. A slice with 15 rows behind it is not automatically higher priority than a 1-row auth bug.
4. **AC = the row goes green on the next gate.** Acceptance criteria for a verify-sourced slice is concrete by construction: "rows `X, Y, Z` read Followed (not Drift) when **verify** (gate) re-runs against this diff." No separate AC invention needed.
5. **Gap rows are backlog, not urgency.** Per verify's own classification, Gap ≠ Drift. Don't fold Gap rows into the same slice or priority tier as Drift unless the engineer asks for the work anyway.

## Grounding (required)

Before final titles, run a short **Grounding** pass. Every **issue** (and the epic brief) must answer:

| Field | Meaning |
|-------|---------|
| **Source of truth** | Path or URL to contract/brief/ADR - or `open - model proposes; frozen below` |
| **Implement checks** | How build proves alignment (tests, contract test, manual scenario) |
| **Review checks** | How **pr-review** re-checks the same source of truth |
| **Drift** | If reality diverges: **ask the engineer** - (1) update the source of truth, (2) separate drift log + follow-up, or (3) addendum on the existing doc. Don’t auto-pick. Lean: intentional product/API change → update; need history without rewrite → addendum; other team owns contract → log + follow-up |

**Preflight examples**

- New API → find OpenAPI/proto/ADR; if missing, ask before inventing routes
- New project / big feature → find project brief / PRD / `docs/…`; if missing, ask
- Drift mid-build → pause implement/review; ask the three options above; note the choice on the issue

## Issue body

Outcome-first. Use [`references/issue-template.md`](references/issue-template.md).

Include:

- What to build (end-to-end behaviour, user/system perspective)
- Acceptance criteria (concrete, checkable - avoid “properly” / “as expected”)
- Blocked by
- Grounding fields above

**Do not** paste the plan’s file map or production code. Exception: a tiny prototype snippet that *is* the decision (schema, state machine, type shape) - trim to the decision-rich bits.

**Touch list** (likely files/areas) only if the engineer asks at quiz time - mark as hints, not acceptance criteria.

## Steps

1. **Gather** - plan path, spec, or conversation. Fetch linked issues/docs if given.
2. **Grounding preflight** - locate or request the source of truth (above).
3. **Explore lightly** - enough domain vocabulary and layout to name slices; don’t re-plan the world.
4. **Draft slices** - vertical bullets + blockers; propose Epic / Features / Issues.
5. **Quiz** - numbered list: title, blocked by, what it delivers, source of truth (epic-level ok if shared). Ask: granularity, edges, Feature merge/split, any touch list?
6. **Publish** (only after approval):
   - **Tracker chosen** (Linear MCP, `gh`, etc.) → create Epic → Features (if any) → Issues in dependency order (blockers first). Wire native blockers when possible. Apply “ready for agent” (or repo equivalent) if the project uses it.
   - **No tracker chosen** → update the **plan markdown**: ordered slices with blockers, grounding, and checkboxes. That file is the backlog. Say so explicitly.
7. **Hand off** - list the **frontier** (unblocked slices). Next: **implement**, preferably one ticket/slice per fresh context. Do not start feature code in this skill.

Do not close or rewrite a parent plan/issue unless asked.

## Tracker discovery

1. Ask which tracker (or “stay on the plan”).
2. Prefer MCP for that tracker when configured; else CLI (`gh`, Linear CLI, …).
3. If tools fail auth, stop and say what to run - don’t invent a local ticket tree.

## Guardrails

1. Publish only after the engineer approves the breakdown.
2. Backlog = chosen tracker **or** the plan markdown (never a parallel `docs/tickets/` / `.scratch/.../issues/` tree).
3. Prefer vertical tracer bullets; file maps stay in **planning**; feature code stays in **implement**.

**Done when:** approved slices are published (tracker or plan), grounding filled, frontier listed for **implement**.

## References

- [`references/issue-template.md`](references/issue-template.md) - issue / plan-slice skeleton
- [`references/grounding.md`](references/grounding.md) - source-of-truth + drift (canonical)

## Related

- Plan the how → **planning**
- Build a slice → **implement**
- Check PR vs source of truth → **pr-review**
- Drift/Gap backlog source → **verify** (full audit)
- Voice → **write-like-goose**

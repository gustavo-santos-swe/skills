---
name: ask
description: Use when unsure which Goose wip skill or flow fits — router over lifecycle stubs and implement stack packs (database, dotnet, react-native, frontend).
disable-model-invocation: true
metadata:
  area: wip
---

# Ask

You don't remember every skill, so ask.

A **flow** is a path through the skills. Most work rides one **main flow**; **on-ramps** merge onto it. **Stack packs** load under **`implement`** by concern. **Anytime** skills sit beside the flow (voice), not as steps.

Sibling skills are still stubs — route by **intent**; open the skill and follow what body exists. Full map: [`../README.md`](../README.md).

## The main flow: idea → ship

```
research → brainstorm → [documentation:adr?] → planning → create-tickets → implement
  → [documentation:ship-docs?] → [security-check?] → git-practices
  → pr-raise → pr-review ⇄ pr-iterate
```

| Step | Skill | When |
|------|--------|------|
| Explore options (cited) | **`research`** | Need primary sources / library choice before locking design |
| Sharpen the idea | **`brainstorm`** | Relentless Q&A + 2–3 approaches; freeze *what* before **planning** |
| Record a hard decision | **`documentation`** → branch **`adr`** | Pre-build ADR / glossary decision |
| Plan the build | **`planning`** | Ready for an implementation plan |
| Split into tickets | **`create-tickets`** | Multi-slice work; tracer bullets + blockers |
| Build | **`implement`** | Ticket or small plan in hand — load stack packs by concern |
| Ship docs | **`documentation`** → branch **`ship-docs`** | Post-build user/ops docs |
| Trust boundary? | **`security-check`** | Auth, secrets, tenancy, uploads, public APIs — optional gate |
| Branch / commits | **`git-practices`** | Conventional Branch + Commits |
| Open PR | **`pr-raise`** | Title/body + open (MCP or `gh`) — **never merge** |
| Review PR | **`pr-review`** | Review an existing PR |
| Address feedback | **`pr-iterate`** | Author loop: fix, push, re-request |

Self-check of the branch diff lives inside **`implement`** or **`pr-raise`** — not a separate skill.

### Shortcuts

- **Small, clear change** → skip research/brainstorm/tickets; go **`implement`** (still pick pack skills).
- **Already have tickets** → **`implement`** per ticket; don't re-triage them.
- **Unsure of stack concern** → open the pack **README map**, load **one** skill, not the whole pack.

## On-ramps

- **Incoming bug / raw request** → **`bug-triage`** → then **`create-tickets`** or **`implement`**.
- **Hard failure in code** (flake, regression, no tight loop yet) → engineering **`diagnosing-bugs`** / **`systematic-debugging`**, then merge back to **`implement`** or **`bug-triage`**.

## Stack packs (under `implement`)

Load from **`implement`** by concern. Prefer progressive disclosure — one skill at a time.

| Pack | Use when | Map |
|------|----------|-----|
| **`database`** | Schema, integrity, indexes, isolation, expand/contract (language-agnostic) | [`../implement/database/`](../implement/database/README.md) |
| **`dotnet/*`** | C# / ASP.NET / EF adapter (`db-integration`), APIs, workers | [`../implement/dotnet/`](../implement/dotnet/README.md) |
| **`react-native/*`** | Expo / RN screens, navigation, device APIs | [`../implement/react-native/`](../implement/react-native/README.md) |
| **`frontend/*`** | Next.js App Router web tier | [`../implement/frontend/`](../implement/frontend/README.md) |

### Quick pack routing

- **Tables / SQL / migrations as data decisions** → `database` (+ `dotnet/db-integration` + `dotnet/migrations-and-compat` if EF).
- **Backend .NET behavior** → `dotnet/<concern>` (e.g. `async`, `error-handling`, `endpoint-conventions`).
- **Mobile UI / device** → `react-native/<concern>`; deep technique may also use [`../../mobile/`](../../mobile/).
- **Next.js web** → `frontend/<concern>`; visual craft may also use [`../../design/`](../../design/).
- **Same feature, multiple tiers** → load one skill per tier (e.g. `database` + `dotnet/db-integration` + `frontend/server-actions-and-forms`).

## Anytime (not a lifecycle step)

- **`write-like-goose`** — house voice for prose **and** code comments. Default when humanizing or drafting durable text in this workflow.
- Fallback only if asked: `write-like-a-human`, `stop-slop` — **don't stack** with goose on the same pass.

## Crossing sessions

- Prefer engineering / productivity **`handoff`** when the window is full or you need a fresh session with continuity.
- Built-in **compact** only at intentional phase breaks — not mid-brainstorm or mid-implement slice.

## Related (outside wip)

Matt / obra flows still exist under `engineering/` and `workflow/` (`ask-matt`, `grill-with-docs`, `tdd`, …). Prefer **wip** skills when doing Goose lifecycle; use upstream skills when you explicitly want that playbook or a wip stub has no body yet.

## Later

Not stubbed yet: **`verify`** / done gate after implement.

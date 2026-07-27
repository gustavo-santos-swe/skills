---
name: ask
description: Router for Goose lifecycle skills and implement stack packs. Use when unsure which skill or flow fits.
disable-model-invocation: true
metadata:
  area: goose
---

# Ask

You don't remember every skill, so ask.

A **flow** is a path through the skills. Most work rides one **main flow**; **on-ramps** merge onto it. **Stack packs** load under **`implement`**. **Anytime** skills sit beside the flow (voice), not as steps.

**Lifecycle skills are filled.** Pack stubs remain under `implement/react-native/` and `implement/frontend/` - route by intent; open the skill and follow what body exists. Full map: [`../README.md`](../README.md).

## The main flow: idea → ship

```
research → brainstorm → [documentation:adr?] → planning → create-tickets → implement
  → [documentation:ship-docs?] → [security-check?] → git-practices
  → pr-raise → pr-review ⇄ pr-iterate
```

| Step | Skill | When |
|------|--------|------|
| Explore options (cited) | **`research`** | Need primary sources / library choice before locking design |
| Sharpen the idea | **`brainstorm`** | Relentless Q&A + 2-3 approaches; freeze *what* before **planning** |
| Record a hard decision | **`documentation`** → branch **`adr`** | Pre-build ADR / glossary decision |
| Plan the build | **`planning`** | Ready for an implementation plan |
| Split into tickets | **`create-tickets`** | Multi-slice work; tracer bullets + blockers |
| Build | **`implement`** | Ticket or small plan in hand - load the active stack pack (README + every `SKILL.md` in that pack) before coding |
| Ship docs | **`documentation`** → branch **`ship-docs`** | Post-build user/ops docs |
| Trust boundary? | **`security-check`** | Auth, secrets, tenancy, uploads, public APIs - optional gate |
| Branch / commits | **`git-practices`** | Conventional Branch + Commits |
| Open PR | **`pr-raise`** | Title/body + open (MCP or `gh`) - never merge |
| Review PR | **`pr-review`** | Review an existing PR |
| Address feedback | **`pr-iterate`** | Author loop: fix, push, re-request |

Self-check of the branch diff lives inside **`implement`** or **`pr-raise`** - not a separate skill.

### Shortcuts

- **Small, clear change** → skip research/brainstorm/tickets; go **`implement`** (still load the active pack as that skill requires).
- **Already have tickets** → **`implement`** per ticket; don't re-triage them.
- **Unsure which pack** → open the pack **README map**, then follow **`implement`** load rules (full pack for the active stack).

## On-ramps

- **Something broken / flake / regression / test red** → **`diagnose`** (evidence → fix → lock), then **`git-practices`** / **`pr-raise`** when shipping the fix.
- **Fuzzy request that isn't a failure** → **`brainstorm`** or **`create-tickets`**, not diagnose.

## Stack packs (under `implement`)

Canonical load rules live in **`implement`**. Summary: pick the pack(s) for the work; before feature code, read that pack’s `README` and **every** `SKILL.md` under it (second pack if both apply, e.g. `database` + `dotnet/db-integration`).

| Pack | Use when | Map |
|------|----------|-----|
| **`database`** | Schema, integrity, indexes, isolation, expand/contract (language-agnostic) | [`../implement/database/`](../implement/database/README.md) |
| **`dotnet/*`** | C# / ASP.NET / EF adapter (`db-integration`), APIs, workers | [`../implement/dotnet/`](../implement/dotnet/README.md) |
| **`react-native/*`** | Expo / RN screens, navigation, device APIs (stubs) | [`../implement/react-native/`](../implement/react-native/README.md) |
| **`frontend/*`** | Next.js App Router web tier (stubs) | [`../implement/frontend/`](../implement/frontend/README.md) |

### Quick pack routing

- **Tables / SQL / migrations as data decisions** → `database` (+ `dotnet` pack when EF/.NET).
- **Backend .NET behavior** → `dotnet` pack.
- **Mobile UI / device** → `react-native` pack; deep technique may also use [`../../mobile/`](../../mobile/).
- **Next.js web** → `frontend` pack; visual craft may also use [`../../design/`](../../design/).

## Always-on / anytime (not lifecycle steps)

- **`write-like-goose`** — durable Goose prose (also root **AGENTS.md** / `.cursor/rules/write-like-goose.mdc`).
- **`codebase-design`** — deep-module vocabulary when shaping seams/interfaces (also used by `engineering/improve-codebase-architecture`).

## Crossing sessions

- When the window is full: write a short durable brief in the target repo (or paste a compact summary for the next chat), then start fresh with that file.
- Built-in **compact** only at intentional phase breaks - not mid-brainstorm or mid-implement slice.

## Related (outside goose)

Optional complements under `engineering/` (architecture / review helpers) and `workflow/doc-coauthoring`. Prefer **goose** for Goose lifecycle.

## Later

Not stubbed yet: **`verify`** / done gate after implement.

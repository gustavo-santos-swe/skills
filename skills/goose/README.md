# goose

House lifecycle for Goose — idea → ship. No upstream sync (`inspired_by` only). Prefer `disable-model-invocation: true`; invoke via **`ask`** or by name.

**Still stubs:** `implement/react-native/*`.  
`implement/frontend/*` is **partially filled** (`project-structure`, `styling`; rest stubs).  
`database` + `dotnet` packs are filled.

## How to use

1. Unsure which skill → **`ask`**
2. Follow the main flow (or an on-ramp) below
3. Durable prose/comments always → **`write-like-goose`** (**ASD-STE100**; also root `AGENTS.md` + Cursor rule)

## When to use which

| Situation | Skill |
|-----------|--------|
| Don’t know where to start | **ask** |
| Need cited options / library facts before deciding | **research** |
| Idea fuzzy; freeze the *what* | **brainstorm** |
| New product / empty repo / greenfield | **brainstorm** → branch **`greenfield`** (Shape → Product → Platform) |
| Hard-to-reverse decision | **documentation** → `adr` |
| *What* is frozen; need ordered *how* | **planning** |
| Multi-slice work with blockers | **create-tickets** |
| Something broken / flaky / red | **diagnose** |
| Build a ticket or clear small change | **implement** (+ stack pack) |
| Check code against the active pack skills | **verify** |
| Trust boundary before ship | **security-check** |
| Branch / commit messages | **git-practices** |
| Open a PR (never merge) | **pr-raise** |
| Review an open PR | **pr-review** |
| Address review feedback | **pr-iterate** |
| Post-build user/ops docs | **documentation** → `ship-docs` |
| Module seams / depth language | **codebase-design** |
| Goose voice on durable text | **write-like-goose** (ASD-STE100) |

### Shortcuts

- Small clear change → **implement** (still load the active pack)
- Already have tickets → **implement** per ticket
- After local OK on dirty tree → **git-practices** → **pr-raise**

## Main flow

```
research? → brainstorm → [documentation:adr?] → planning → create-tickets
  → implement (+ packs) → verify (gate) → [documentation:ship-docs?] → [security-check?]
  → git-practices → pr-raise → pr-review (verify + other axes) ⇄ pr-iterate
```

On-ramp: **diagnose** → fix + lock → git-practices → pr-raise.

## Inventory

| Skill | Role |
|-------|------|
| [ask](./ask/) | Router |
| [research](./research/) | Cited decision brief |
| [brainstorm](./brainstorm/) | Freeze the what (`product` / `greenfield`) |
| [documentation](./documentation/) | ADR + ship-docs |
| [planning](./planning/) | Implementation plan |
| [create-tickets](./create-tickets/) | Tracer bullets + blockers |
| [diagnose](./diagnose/) | Evidence → fix → lock |
| [implement](./implement/) | Build (+ [database](./implement/database/), [dotnet](./implement/dotnet/), [react-native](./implement/react-native/), [frontend](./implement/frontend/)) |
| [verify](./verify/) | Gate (diff) or full audit: code vs active pack skills, rule by rule |
| [security-check](./security-check/) | Optional trust-boundary gate |
| [git-practices](./git-practices/) | Branch + commits |
| [pr-raise](./pr-raise/) | Open PR |
| [pr-review](./pr-review/) | Review PR |
| [pr-iterate](./pr-iterate/) | Author feedback loop |
| [write-like-goose](./write-like-goose/) | Always-on voice |
| [codebase-design](./codebase-design/) | Deep-module vocabulary |

Optional outside this area: `engineering/improve-codebase-architecture` (uses **codebase-design**), `design/frontend-design`, `mobile/*` deep technique.

---
name: solution-structure
description: Use when changing .NET solution layout, project boundaries, references, or Directory.Build/CPM — or when implement loads the dotnet pack for where code should live.
metadata:
  area: goose
---

# Solution Structure

Goose defaults for .NET solution layout and project boundaries. Calibrated against Monetis; some rules are **elevated** above today’s App graph (see [Legacy note](#legacy-note-monetis)).

**Target repo wins:** if the solution already has a clear layout, follow it unless the user asks to migrate.

Voice: **`write-like-goose`**. Target-repo `AGENTS.md` may override paths/names.

## When to use

- Adding a project, host, or vertical
- Debating where a type lives
- Reviewing a PR that changes the project graph
- **`implement`** loading this pack

## Layers (per vertical)

| Project | Holds |
|---------|--------|
| **Domain** | Entities, value objects, enums, domain services, **domain-pure ports** |
| **Application** | Feature use cases, **app/integration ports**, orchestration |
| **Infrastructure** | Port adapters (EF, HTTP clients, email, blobs…). Start as **one** project; [split when fat](#infrastructure-splits) |
| **Api / Host** | Composition root, HTTP, auth wiring, middleware |
| **AppHost** + **ServiceDefaults** | Aspire orchestration + shared host defaults (when using Aspire) |

### Dependency rule

```
Api / Host  →  Application  →  Domain
                 ↑                ↑
           (ports only)     (no outward refs)
Infrastructure → Domain (+ Application ports it implements)
```

- **Application** references **Domain** and abstractions (ports). It does **not** reference Infrastructure projects.
- **Infrastructure** implements ports; registered in the host.
- Enforce with **Architecture** tests (see [Tests](#tests)).

### Ports (by kind)

| Kind | Lives in | Examples |
|------|----------|----------|
| Domain-pure | **Domain** | Repository interfaces next to aggregates; domain clocks if needed |
| App / integration | **Application** | Email, payments gateway, file storage, external APIs |

## Naming and folders

**Projects:** `{Product}.{Vertical}.{Layer}`  
Examples: `Monetis.App.Domain`, `Monetis.Admin.Api`.

### Polyglot monorepo (default)

Calibrated against Monetis. Surfaces live **under `src/`**, not as siblings of `src/`:

```
src/
  backend/     # all .NET projects + test projects + Directory.*.props
  frontend/    # Next.js (when Web is in)
  mobile/      # Expo / RN (when Mobile is in)
  admin/       # optional extra web surfaces
```

- **Don’t** put the Next app at repo-root `web/` while `.NET` alone occupies `src/`.
- **Don’t** put test projects in a repo-root `tests/` folder.
- `TestResults/` is runner output — gitignore it; never treat it as layout.

### On disk (.NET)

- One vertical → `src/backend/{Product}.{Vertical}.{Layer}/` is fine (flat Monetis style).
- **Two+ verticals** → prefer `src/backend/{Vertical}/…` so App and Admin don’t mix.
- Test projects colocate under **`src/backend/`** (same folder as production projects).

### Inside Application (feature slices)

Organize by **feature**, not by `Commands/` / `Handlers/` type buckets.

```
Application/
  CreditCards/
    Statements/
      Get.cs              # request, response, handler (colocated)
    Shared/
      Errors.cs
  CheckingAccounts/
    Transactions/
      …
```

Colocate request/response/handler (and feature errors) in the feature folder. Shared cross-feature app helpers go under `Common/` or feature `Shared/` sparingly.

### Inside Domain (classic / shared)

Domain objects are reused across features → **type-oriented** (and small area folders when useful):

```
Domain/
  Entities/
  ValueObjects/
  Enums/
  Shared/
  Auth/                 # optional area clusters
  Finances/
```

Don’t invent a new top-level layer for one type.

## Verticals and hosts

- Separate verticals when **audiences** differ (e.g. App vs Admin), not for every new screen.
- Admin-style verticals may use read models / `IsTableExcludedFromMigrations` against the primary DB when that is the product choice.
- Prefer Aspire **AppHost** + **ServiceDefaults** for local multi-service orchestration when the repo already uses them.

## Infrastructure splits

Default: **one** Infrastructure project.

Split when a slice is fat or has a different lifecycle, for example:

- `*.Infrastructure.Persistence` — EF, mappings, migrations
- External API client projects — generated/hand-written clients + DTOs for one vendor
- Other adapters that pull heavy package graphs

Don’t split preemptively for one adapter.

## Shared code across verticals

Prefer duplication until it hurts (third copy or ownership fight). Then extract a **narrow** shared project — not a junk-drawer SharedKernel.

## Tests

| Project | Role | Location |
|---------|------|----------|
| `*.Tests.Unit` | Fast, no I/O | `src/backend/` (next to production) |
| `*.Tests.Integration` | Real DB/containers as needed | `src/backend/` |
| `*.Architecture.Tests` | Dependency rule + layer rules | `src/backend/` |

Architecture tests are required for the ports-only rule. Do **not** invent a repo-root `tests/` tree for greenfield .NET.

## Build mechanics

Under the backend solution folder (e.g. `src/backend/`):

- **`Directory.Packages.props`** — Central Package Management (required)
- **`Directory.Build.props`** — baseline: lang version, nullable, treat warnings as errors (or explicit allow-list). Deeper analyzer packs → **`code-style`** skill

Repo-root CPM only if every .NET project in the monorepo should share versions (unusual for Monetis-shaped repos).

## Legacy note (Monetis)

Monetis **App** today still has Application → Infrastructure / Persistence references. **Goose standard is ports-only.** When editing Monetis: don’t add new Application → Infra edges; prefer ports + adapters; tighten Architecture tests over time. Admin/other greenfield verticals should follow this skill from the start.

## Don't

- Don’t reverse the dependency rule “just this once”
- Don’t add a layer for a single file
- Don’t put Stripe/email ports in Domain
- Don’t create SharedKernel on day one
- Don’t use Application type-bucket folders (`Handlers/`, `Commands/`) as the primary layout
- Don’t scaffold `src/` = backend-only with root `tests/` and root `web/` — use `src/backend` + `src/frontend` (+ `src/mobile` when needed)
- Don’t put `Directory.Packages.props` / `Directory.Build.props` at repo root unless every .NET project in the monorepo should share them (unusual)

## References

- [`references/layout-sketch.md`](references/layout-sketch.md) — example trees (single / multi-vertical / Persistence split)

## Related

- Domain modeling details → **`domain-modeling`**
- Use-case / handler shape → **`application-layer`**
- EF / DbContext → **`db-integration`**
- Analyzers beyond Build.props → **`code-style`**

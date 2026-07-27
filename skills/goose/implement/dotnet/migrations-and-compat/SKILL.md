---
name: migrations-and-compat
description: Use when adding or reviewing EF Core migrations, expand/contract deploy order, or schema apply in CI — or when implement loads the dotnet pack for migration work.
metadata:
  area: goose
---

# Migrations and Compat

Goose handbook for **EF Core migration mechanics** and deploy order. Schema design / expand-contract *principles* → **`database`**. API JSON breaks → **`api-contracts`**.

**Target repo wins** if migrate-on-startup or bundle flow is already settled.

Voice: **`write-like-goose`**.

## When to use

- New EF migration; renaming/dropping columns; rolling deploys
- CI/CD apply steps; seed vs migrate
- **`implement`** loading this pack

## Ownership

| Concern | Skill |
|---------|--------|
| Tables, FKs, indexes, expand/contract rules | **`database`** |
| `Migration` classes, `dotnet ef`, apply order | **this skill** |
| Dual-write / backfill jobs in app code | **`background-work`** |

## EF hygiene

- Migrations live in **Infrastructure** (or the agreed persistence project)
- **Generate** with EF tools (`dotnet ef migrations add …`) — don’t hand-author opaque diffs as the default
- **Never edit** a migration already applied to shared/staging/prod; add a new migration instead
- Don’t squash/rewrite history that’s left the developer laptop

## Apply

- **Production/CD:** explicit apply step — typically `dotnet ef database update` (or equivalent) in the pipeline / release Job. **Don’t** rely on the first app instance calling `Database.Migrate()` under scale-out
- **Local/dev:** `dotnet ef` (or a repo script) is fine; startup migrate only if the target already does it for DX
- **Bundles** (`dotnet ef migrations bundle`) are **optional** — use when deploy wants a standalone migrator without SDK/project; not required Goose-wide

## Expand / contract (with EF)

Follow **`database`** expand/contract:

1. **Expand** migration (additive / dual-write columns) → apply
2. Deploy app that reads/writes both shapes
3. Backfill (migration SQL and/or **`background-work`**)
4. **Contract** migration (drop old) only after backfill + app no longer needs the old shape

Never run destructive contract steps before backfill completes. Rolling deploys must survive old and new app binaries during the expand window.

## Seed data

- Reference/seed data: dedicated migration or **idempotent** seed path — not one-off prod fixes buried in unrelated migrations
- Don’t use migrations as an unstructured data-entry tool for production incidents

## Don't

- Don’t edit applied migrations
- Don’t auto-migrate on startup as the prod strategy
- Don’t drop/rename columns in one step when old binaries are still live
- Don’t point migrate at the wrong database “to save time”

## References

- [`references/examples.md`](references/examples.md) — expand/contract + apply sketch

## Related

- Schema rules → **`database`**
- EF mapping / DbContext → **`db-integration`**
- Backfill jobs → **`background-work`**
- Public API compat → **`api-contracts`**

---
name: database
description: Language-agnostic database rules — modeling, integrity, indexes, transactions, schema evolution, SQL-level performance. Use when designing or changing schema, writing migrations/SQL, or reviewing data model decisions (not ORM/C# wiring).
metadata:
  area: goose
---

# Database

Goose handbook for **schema and engine truth**. How .NET talks to that model → [`../dotnet/db-integration/`](../dotnet/db-integration/). EF migrate/apply mechanics → [`../dotnet/migrations-and-compat/`](../dotnet/migrations-and-compat/).

**Target repo wins** if the project already standardized on types, soft-delete, or naming.

Voice: **`write-like-goose`**.

## When to use

- New or changed tables, constraints, indexes, migrations (as *data* decisions)
- Reviewing “does this schema tell the truth?”
- Pagination, isolation, concurrency at the **data** layer
- **`implement`** loading this pack

## When not to

- DbContext, LINQ, DI of repositories → **`db-integration`**
- Mapping DB errors to HTTP → **`error-handling`** / **`db-integration`**
- `dotnet ef` apply / never-edit-applied → **`migrations-and-compat`**

## Keys and modeling

| Rule | Default |
|------|---------|
| **Primary key** | **Surrogate** — opaque id (UUID/Guid v7 or identity/sequence). Align id generation with **`time-and-ids`** when on .NET |
| **Natural / business keys** | **UNIQUE** constraints (and indexes), not the PK — so keys can rename without rewriting FKs |
| **Ownership** | Clear owner (user/tenant/aggregate). Prefer FK to the owning row over duplicated owner ids without constraints |

Normalize until joins hurt; denormalize with a measured reason (and a plan to keep copies consistent). Don’t invent a second source of truth for the same fact.

## Integrity (in the database)

App validation is UX. The database is the last line:

- **PK**, **FK** (unless a deliberate soft boundary with a written reason)
- **UNIQUE** for business keys
- **NOT NULL** where the domain requires it
- **CHECK** for cheap, stable invariants (positive amounts, allowed status sets when not using an enum type)

Don’t skip FKs/uniques “because FluentValidation / the handler checks it.”

## Indexes

- Index for **known** access paths (filter, join, sort) — not every column
- **FK columns indexed** unless you can justify the write savings
- Composite: equality columns left → range/sort right; avoid leading with low-selectivity noise
- Unique constraints already create supporting indexes — don’t double up blindly

Prove with a plan when unsure; don’t wait for prod fire for every greenfield path you already know you’ll query.

## Types and nulls

| Kind | Default |
|------|---------|
| Money | **decimal / numeric** — never `float`/`double` |
| Instant / “when” | **timestamptz** (UTC) — or engine equivalent |
| Calendar date | **date** — not a midnight timestamp pretending to be a date |
| Enums | DB enum **or** text + CHECK **or** lookup table — one style per domain; document it |
| Null | Meaningful absence only; don’t nullable-everything “for flexibility” |

.NET wire mapping of Instant/LocalDate/decimal → **`serialization`** / **`time-and-ids`**.

## JSON columns

**Sparse and justified.** Relational columns for anything you filter, join, unique, or treat as money/status/id.

JSON is OK for vendor payloads or truly schemaless bags — write down why. Don’t hide the domain model in a blob.

## Soft-delete

**Opt-in per aggregate.** Hard delete by default.

Use `deleted_at` (or equivalent) + query filters only when product needs undelete, audit, or retention. Soft-delete + UNIQUE needs a partial unique index (or equivalent) so “live” rows stay unique. Matches **`db-integration`**.

## Transactions and isolation

- One business use case → **one transaction** (handler owns the boundary → **`application-layer`**)
- Default isolation: provider / **read committed** (or engine default) — don’t jump to serializable without a reason
- Keep transactions short; don’t hold locks across external HTTP calls

## Concurrency

Contested aggregates (balances, inventory, “current status”): **optimistic** concurrency — version / rowversion / `xmin`-style token.

Map conflicts to the product’s conflict path (**`error-handling`** / **`db-integration`**). Pessimistic `SELECT … FOR UPDATE` is rare and explicit. Don’t silent last-write-wins on money/state rows.

## Schema evolution

**Expand → migrate data → contract.** Dual-write / backfill when readers and writers roll independently.

- Never edit a migration already applied to shared envs — **`migrations-and-compat`**
- Breaking drops/renames need a deploy order that keeps old and new app versions safe
- Every schema change should have a rollback or forward-fix story

## Queries and pagination (SQL)

- Prefer **keyset / cursor** for large lists (stable sort key + seek) — aligns with **`endpoint-conventions`**
- Offset is OK for small admin grids; don’t offset deep into huge tables as the default feed
- Watch SQL-level N+1 (chatty round-trips) and accidental full scans on hot paths
- Parameterize everything — no string-concat SQL

## Data security (schema/ops)

- Least-privilege DB roles for app vs migrate vs admin
- PII columns: minimize; encryption/tokenization is a product decision — never log them (**`observability`**)
- No ad-hoc prod DDL without a reviewed migration / rollback path

## Schema / PR checklist

1. Who owns this data?
2. What uniqueness does the business require? (unique constraint)
3. What filters/sorts will queries use? (indexes)
4. What if two writers hit the same row? (version / conflict)
5. How do we reverse or expand/contract this change?

## Failure modes (agent traps)

| Temptation | Why it hurts | Do instead |
|------------|--------------|------------|
| Natural key as PK | Rename rewrites the graph | Surrogate PK + UNIQUE |
| Skip FK/unique “app checks” | Orphans / dupes under race | Constraints in DB |
| Index every column | Write amp, bloat | Index known paths + FKs |
| Money as float | Rounding bugs | decimal/numeric |
| Soft-delete everywhere | Broken uniques / every query pays | Opt-in per aggregate |
| Domain only in JSON | Can’t constrain or index truth | Relational for real fields |
| Edit applied migration | Divergent environments | New migration |

## Don't

- Don’t put ORM tutorials here
- Don’t copy the SQL manual — only Goose hard rules and anti-patterns
- Don’t skip integrity because the app validates it
- Don’t use float for money
- Don’t soft-delete every table by default
- Don’t store large binaries in the DB — **`file-storage`**

## References

- [`references/examples.md`](references/examples.md) — keys, indexes, expand/contract, soft-delete unique

## Related

- EF / LINQ / SaveChanges → **`db-integration`**
- Migrate apply / never-edit-applied → **`migrations-and-compat`**
- Handler TX boundary → **`application-layer`**
- Ids / clocks → **`time-and-ids`**
- List pagination at HTTP → **`endpoint-conventions`**
- Blobs → **`file-storage`**

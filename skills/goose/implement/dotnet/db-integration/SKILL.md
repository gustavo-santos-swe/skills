---
name: db-integration
description: Use when writing or reviewing EF Core / .NET data access — DbContext, mappings, tracking, transactions, concurrency — or when implement loads the dotnet pack for persistence code.
disable-model-invocation: true
metadata:
  area: goose
---

# DB Integration (.NET)

How .NET talks to the database. **Schema / SQL / indexes / isolation** → [`../../database/`](../../database/SKILL.md). Migrations mechanics → **`migrations-and-compat`**.

**Target repo wins** if persistence is already standardized.

Voice: **`write-like-goose`**.

## When to use

- DbContext, mappings, queries, `SaveChanges`, concurrency in C#
- Choosing EF vs raw SQL
- **`implement`** loading this pack

## Split of responsibility

| Concern | Skill |
|---------|--------|
| Tables, FKs, indexes, expand/contract | [`database`](../../database/SKILL.md) |
| Generate/apply migrations | **`migrations-and-compat`** |
| DbContext, tracking, Fluent config, SaveChanges | **this skill** |

## Access style

**EF Core** for almost all reads and writes.

Dapper / `FromSql` / ADO only for proven hot paths or SQL EF can’t express cleanly — always **parameterized**. Those queries still obey [`database`](../../database/SKILL.md).

Who the handler calls (ports vs `DbContext`) → **`application-layer`** + **`solution-structure`**.

## Tracking

- Read/project paths: **`AsNoTracking()`** (or `AsNoTrackingWithIdentityResolution` when you need graph identity without write tracking)
- Load-then-mutate: normal tracking, then `SaveChanges`
- Never return tracked entities across process boundaries (API responses, messages)

## Queries (avoid N+1 and client eval)

**N+1** is the usual EF footgun: load parents, then touch collections in a loop (especially with lazy-loading proxies).

| Pattern | Prefer |
|---------|--------|
| Need related data for a write/graph | `Include` (single query) or **`AsSplitQuery()`** when multiple Includes / large children risk cartesian blow-up |
| Read/list shapes | **Project** with `Select` into DTOs — often better than Include+map |
| Existence | `.AnyAsync` — not `.CountAsync() > 0` |
| Filter | Filter **before** `ToListAsync` — never materialize then filter in memory |
| Include + Select | Projection wins; drop redundant `Include` when you `Select` |

Ban lazy-loading proxies on Goose greenfield (`Microsoft.EntityFrameworkCore.Proxies`) unless the target repo already depends on them — they hide N+1.

**Compiled queries** (`EF.CompileAsyncQuery`) only on measured hot paths — not a default style.

When LINQ can’t express it cleanly: parameterized `FromSqlInterpolated` / `ExecuteSql` (never string-concat SQL). Bulk updates: prefer `ExecuteUpdateAsync` / `ExecuteDeleteAsync` when you don’t need a tracked graph.

See query traps in [references](references/examples.md). Schema/index truth stays in [`database`](../../database/SKILL.md).

## Mapping

Fluent **`IEntityTypeConfiguration<T>`** in Infrastructure / Persistence. Apply via `ApplyConfigurationsFromAssembly` (or explicit registration).

- No EF data annotations on Domain types
- Value converters for strongly typed ids, NodaTime (`Instant` / `LocalDate`), enums as needed — align with **`time-and-ids`** / **`serialization`**
- Owned types / JSON columns when the schema skill allows them; don’t invent document blobs to avoid tables

## Query filters

- **Ownership / tenant** global filters are OK when the product is user-scoped (Monetis-style `UserId`)
- **Soft-delete** filters only on aggregates that need them — not a tax on every table
- Admin, jobs, and migrations need an explicit **ignore filter** path when they must see all rows

## Transactions and SaveChanges

- Handler owns the use-case write boundary (**`application-layer`**)
- Prefer **one `SaveChangesAsync` per use case**
- Ban ambient **`TransactionScope`** unless you truly need a distributed transaction
- Explicit `BeginTransaction` when multiple saves or contexts must commit atomically
- Don’t open nested transactions casually

## Concurrency

Optimistic concurrency on aggregates that can race: rowversion / provider token (`IsConcurrencyToken`).

Map `DbUpdateConcurrencyException` (and known unique violations) to **`Conflict`** per **`error-handling`**. Don’t silently last-write-wins on contested money/state rows.

## Testing

Persistence / handler integration tests that hit EF: **real engine** via Testcontainers (or equivalent). 

- Ban EF **InMemory** for anything beyond a throwaway smoke
- Domain unit tests: no DB
- Broader test layout → **`testing`**

## Failure modes (agent traps)

| Temptation | Why it hurts | Do instead |
|------------|--------------|------------|
| Lazy load in a loop | N+1 | Include / split / project |
| `ToList` then `Where` | Full table load | Filter in SQL first |
| `Include` + `Select` | Include ignored | Projection only |
| `FromSqlRaw` + concat | Injection | `FromSqlInterpolated` |
| Sensitive SQL logging in prod | Leaks data | Dev-only detailed/sensitive logs |

## Don't

- Don’t invent schema in C# that contradicts [`database`](../../database/SKILL.md)
- Don’t return tracked entities from handlers
- Don’t use unbounded raw SQL string concat
- Don’t rely on EF InMemory for filter/concurrency truth
- Don’t soft-delete every table by default
- Don’t enable lazy-loading proxies on greenfield

## References

- [`references/examples.md`](references/examples.md) — mapping, no-track, N+1 fixes, concurrency catch

## Related

- Schema → **`database`**
- Handlers / UoW boundary → **`application-layer`**
- Ports-only layout → **`solution-structure`**
- NodaTime / ids → **`time-and-ids`**
- Migrations → **`migrations-and-compat`**
- Test project shape → **`testing`**
- Deep EF how-to (plugin) → Cursor **`dotnet-data`** / `optimizing-ef-core-queries`

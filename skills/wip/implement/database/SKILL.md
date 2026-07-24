---
name: database
description: Language-agnostic database rules — modeling, integrity, indexes, transactions, schema evolution, SQL-level performance. Use when designing or changing schema, writing migrations/SQL, or reviewing data model decisions (not ORM/C# wiring).
disable-model-invocation: true
metadata:
  area: wip
---

# Database

Status: **stub** — outline below is the reminder of what belongs here. Fill with Goose conventions later. .NET/EF wiring → [`../dotnet/db-integration/`](../dotnet/db-integration/).

## When to use

- New or changed tables, constraints, indexes, migrations (as *data* decisions).
- Reviewing “does this schema tell the truth?”
- Pagination, isolation, concurrency at the **data** layer.

## When not to

- DbContext, LINQ, DI of repositories → **db-integration**.
- Mapping DB errors to HTTP → **error-handling** / **db-integration**.

## Topics to fill (checklist)

### Modeling
- Keys (natural vs surrogate), how far to normalize, when to denormalize
- Ownership of data across bounded contexts

### Integrity
- PK / FK / unique / check / NOT NULL — what never lives only in the app

### Indexes
- Selective vs covering; composite column order; when *not* to index
- FK side always indexed unless justified

### Types & nulls
- Money/decimal, timestamps (UTC), enums vs lookup tables, JSON columns with criteria

### Transactions & isolation
- One business unit of work = one TX
- When read committed vs stricter levels; deadlock habits

### Concurrency
- Optimistic (version/rowversion) vs pessimistic; lost updates

### Schema evolution
- Expand → migrate data → contract; dual-write; deprecate columns
- Zero-downtime habits; no edit of applied migrations

### Queries & plans
- Reading a plan (seq scan vs index); SQL-level N+1; keyset vs offset pagination

### Data performance (when it hurts)
- Cardinality, skew, hot rows; partitioning only with real pain

### Ops (light)
- Migrations vs ad-hoc DDL; seeds; idempotent data fixes
- What never to run in prod without a rollback path

### Data security
- Least-privilege DB roles, PII columns, encryption policy (not driver APIs)

## Schema / PR checklist (force later)

1. Who owns this data?
2. What uniqueness does the business require? (unique constraint)
3. What filters/sorts will queries use? (indexes)
4. What if two writers hit the same row?
5. How do we reverse this schema change?

## Don't

- Don’t put ORM tutorials here.
- Don’t copy the SQL manual — only **our** hard rules and anti-patterns.
- Don’t skip integrity “because the app validates it.”

## References

Optional later: `references/indexing.md`, `references/expand-contract.md`.

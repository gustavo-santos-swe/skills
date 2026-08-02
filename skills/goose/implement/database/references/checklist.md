| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Primary key is a surrogate (opaque id: UUID/Guid v7 or identity/sequence) | verify | Keys and modeling |
| Natural/business keys get UNIQUE constraints (and indexes), not the PK | verify | Keys and modeling |
| Every EF entity has an explicit primary key configured | architecture-test | Keys and modeling — EF model metadata (`FindPrimaryKey()`) |
| Don't skip FKs/uniques "because the handler/FluentValidation checks it" — PK, FK, UNIQUE, NOT NULL, CHECK live in the database | verify | Integrity |
| A missing FK target is rejected by the database | regression-test | Integrity |
| A duplicate natural key is rejected by a UNIQUE constraint | regression-test | Integrity |
| NOT NULL / CHECK constraints reject invalid rows | regression-test | Integrity |
| Index for known access paths (filter, join, sort); FK columns indexed unless write savings justify skipping | verify | Indexes |
| Money is `decimal`/`numeric` — never `float`/`double` | analyzer | Types and nulls — banned-type analyzer on property/param type |
| Instant/"when" values stored as `timestamptz` (UTC); calendar dates as `date`, not a midnight timestamp | verify | Types and nulls |
| JSON columns are sparse and justified — relational columns for anything filtered, joined, uniqued, or treated as money/status/id | verify | JSON columns — "deliberately" vs "escape hatch" needs schema-design judgment |
| Soft-delete is opt-in per aggregate; hard delete by default | verify | Soft-delete |
| Soft-deleted rows are excluded by the default query filter | regression-test | Soft-delete |
| Soft-delete + UNIQUE needs a partial unique index so "live" rows stay unique | verify | Soft-delete |
| One business use case maps to one transaction; keep transactions short, no locks held across external HTTP calls | verify | Transactions and isolation |
| Contested aggregates (balances, inventory, current status) use optimistic concurrency (version/rowversion/`xmin`-style token) | verify | Concurrency |
| Optimistic concurrency conflict raises `DbUpdateConcurrencyException` | regression-test | Concurrency |
| Schema changes follow expand → migrate data → contract, with a rollback or forward-fix story | verify | Schema evolution |
| Prefer keyset/cursor pagination for large lists; parameterize every query, no string-concat SQL | verify | Queries and pagination |
| Least-privilege DB roles for app vs migrate vs admin; no ad-hoc prod DDL without a reviewed migration | verify | Data security |
| Don't use float for money | analyzer | Don't — same banned-type analyzer as above |
| Don't soft-delete every table by default | verify | Don't |
| Don't store large binaries in the DB | verify | Don't |

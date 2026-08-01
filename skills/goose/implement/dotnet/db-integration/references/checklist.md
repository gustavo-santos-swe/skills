| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| EF Core for almost all reads/writes; Dapper/`FromSql`/ADO only for proven hot paths, always parameterized | verify | Access style |
| Read/project paths use `AsNoTracking()`; never return tracked entities across process boundaries (API responses, messages) | verify | Tracking |
| Queries avoid N+1 — use `Include`/`AsSplitQuery()` or project with `Select`, filter before `ToListAsync`, use `.AnyAsync` for existence checks | verify | Queries — needs reading the actual query plan/access pattern |
| Ban lazy-loading proxies (`Microsoft.EntityFrameworkCore.Proxies`) on greenfield unless the target repo already depends on them | verify | Queries |
| Mapping is Fluent `IEntityTypeConfiguration<T>` in Infrastructure/Persistence; no EF data-annotation attributes on Domain entities | architecture-test | Mapping — reflection scan of Domain types for `[Table]`/`[Column]`/`[Key]` |
| Ownership/tenant global query filters are OK when the product is user-scoped; soft-delete filters only on aggregates that need them | verify | Query filters |
| Soft-deleted rows are excluded by the default query filter | regression-test | Query filters |
| Prefer one `SaveChangesAsync` per use case; ban ambient `TransactionScope` unless a true distributed transaction is needed | verify | Transactions and SaveChanges |
| Optimistic concurrency (rowversion/provider token) on aggregates that can race; conflict raises `DbUpdateConcurrencyException` | regression-test | Concurrency |
| Persistence/handler integration tests hit EF via a real engine (Testcontainers); ban EF InMemory beyond a throwaway smoke test | architecture-test | Testing — assembly-dependency ban on `Microsoft.EntityFrameworkCore.InMemory` in test projects |
| Don't invent schema in C# that contradicts the `database` skill | verify | Don't |
| Don't use unbounded raw SQL string concat (`FromSqlRaw` + concat) | verify | Don't |
| Don't soft-delete every table by default | verify | Don't |

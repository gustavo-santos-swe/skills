---
name: db-integration
description: EF Core / ADO.NET / Dapper adapter for .NET — DbContext, repositories, transactions in code. Schema truth lives in implement/database. Use when writing or reviewing .NET data-access code, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# DB Integration (.NET)

Status: **stub** — topic list below is what to define later. **Schema / SQL / integrity / indexes** → [`../../database/`](../../database/SKILL.md). This skill = how .NET talks to that schema.

## When to use

- DbContext, repositories, unit of work, raw SQL from C#, EF config that maps to an existing schema.
- **`implement`** loading this pack for a .NET change that touches persistence.

## Split of responsibility

| Concern | Skill |
|---------|--------|
| Tables, FKs, indexes, isolation, expand/contract principles | [`database`](../../database/SKILL.md) |
| EF migrations generate/apply mechanics | [`migrations-and-compat`](../migrations-and-compat/SKILL.md) |
| DbContext, tracking, repos, SaveChanges, concurrency tokens in C# | **this skill** |

## Topics to fill (checklist)

### Access style
- EF Core only vs Dapper/ADO for hot paths — our rule
- Repository vs DbContext-from-handler — our line

### DbContext
- One context vs bounded contexts; pooling
- No-tracking defaults for reads; when tracking is required
- Global query filters (soft delete, etc.) — yes/no and how

### Mapping
- Fluent API vs attributes; where configurations live
- Value converters / strong IDs
- Owned types / JSON columns — when allowed

### Transactions & UoW
- Who starts the transaction (handler vs infra)
- `SaveChanges` once per use case — enforce?
- Ambient `TransactionScope` — banned or not

### Concurrency (C# side)
- RowVersion / xmin mapping; handling `DbUpdateConcurrencyException`
- Align with database skill isolation/locking choices

### Raw SQL
- When `FromSql` / Dapper is allowed; parameterization always
- Still must satisfy [`database`](../../database/SKILL.md) query/plan rules

### Testing
- Testcontainers vs InMemory — align with testing skill

## Don't

- Don't invent schema in C# that contradicts [`database`](../../database/SKILL.md).
- Don't return tracked entities across process boundaries.
- Don't open nested transactions casually.

## References

Optional: `references/` for EF patterns. Schema checklists stay in the database skill.

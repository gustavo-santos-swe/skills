---
name: domain-modeling
description: Use when shaping C# domain types — entities, value objects, aggregates, invariants, domain events — or when implement loads the dotnet pack for domain code.
disable-model-invocation: true
metadata:
  area: wip
---

# Domain Modeling

Goose handbook for the **C# shape** of the domain. Ubiquitous language and ADRs stay in **`brainstorm`** / **`documentation`**.

**Target repo wins:** if the project already models the domain a certain way, follow it unless the user asks to migrate.

Voice: **`write-like-goose`**.

## When to use

- New aggregates, VOs, invariants, or domain events
- Reviewing whether logic belongs in Domain vs Application
- **`implement`** loading this pack

## Building blocks

| Kind | Criteria |
|------|----------|
| **Entity** | Identity over time; equality by id |
| **Value object** | Equality by value; immutable after create |
| **Aggregate root** | Consistency boundary; outsiders reference **roots by id** only — not every entity is a root |

Prefer a **rich** model: state changes and invariants live on entities/VOs as methods. Application orchestrates; it doesn’t set every property from the outside.

Folders: classic Domain layout (`Entities/`, `ValueObjects/`, …) per **`solution-structure`**.

## IDs

**Strongly typed IDs** by default (`CreditCardId`, `CheckingAccountId`), not bare `Guid` on public domain APIs.

Underlying generation (Guid vs ULID, who creates them) → **`time-and-ids`**.

## Avoid primitive obsession

Don’t pass domain meaning as bare `string` / `int` / `bool` / `Guid` when a type would catch mistakes.

| Prefer | Instead of |
|--------|------------|
| **Enum** (or closed union of cases) | Magic strings/ints for a **fixed** set (`TransactionType`, `StatementStatus`) |
| **Value object** | Validated strings/numbers (`Email`, `Cpf`, `Money` via NodaMoney or equivalent) |
| **Typed id** | Bare `Guid` on public APIs |

Use an **enum** when the set is closed and owned by the domain. Prefer a VO when there are rules/formatting beyond “one of N labels.” Don’t invent a VO for every string if an enum or a well-named parameter is enough — target the confusion (wrong id type, invalid email, status typos).

## Invariants and failures

Align with **`error-handling`**:

| Situation | Signal |
|-----------|--------|
| Invariant that App/API should already have blocked (e.g. empty name on `Rename`) | **Throw** — unexpected / bug |
| Parsing raw input into a VO (`Cpf.Create`) | **Result / union** |
| Expected refusal from **current state** (already paid, can’t archive) | **Result / union** |

Don’t rely on edge validators alone for rules that must hold for every entry point (HTTP, jobs, imports) — keep the real invariant on the domain type; choose throw vs Result using the table above.

## Domain events

1. Raise on the aggregate (`AddDomainEvent` / equivalent)
2. Persist the aggregate
3. Dispatch **after** successful save; then clear
4. Start **in-process**; durable / cross-service delivery → **`messaging`** (outbox when needed)

Name events as facts in past tense (`CreditCardRenamed`). Keep payloads small; ids over fat graphs.

## Persistence ignorance

Domain must **not** reference:

- EF Core / DbContext / data annotations as the model
- ASP.NET / `HttpContext`
- `ILogger` or other infra SDKs

**Allowed:** narrow **Domain ports** (e.g. `IClock`, id factory) implemented in Infrastructure. Protected parameterless constructors for EF are OK when the ORM requires them.

Mappings and column config live in Infrastructure / Persistence.

## Don't

- Don’t make every entity an aggregate root
- Don’t span multiple consistency boundaries in one aggregate for convenience
- Don’t put use-case orchestration in entities
- Don’t use EF attributes as the only expression of the model
- Don’t return Result from every mutator when the failure is truly unexpected after validation
- Don’t thread raw primitives through the domain where a typed id, enum, or VO would make illegal states harder

## References

- [`references/examples.md`](references/examples.md) — sketches for VO, entity mutator, typed id, event

## Related

- Project layout / ports → **`solution-structure`**
- Failure unions / HTTP → **`error-handling`**
- Clocks & id generation → **`time-and-ids`**
- Handlers / use cases → **`application-layer`**
- Glossary → **`brainstorm`** (`CONTEXT.md`)

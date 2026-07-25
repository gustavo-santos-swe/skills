---
name: testing
description: Use when writing or reviewing .NET tests — TUnit, NSubstitute, Testcontainers, architecture tests, naming — or when implement loads the dotnet pack for test work.
disable-model-invocation: true
metadata:
  area: wip
---

# Testing

Goose handbook for .NET test mechanics. Process/TDD flow stays in lifecycle skills; this pack is **how** we structure and run tests.

**Target repo wins** if the project already standardized on xUnit/Moq/etc.

Voice: **`write-like-goose`**.

## When to use

- Adding unit, integration, or architecture tests
- Choosing doubles vs real DB
- **`implement`** loading this pack

## Stack (greenfield)

| Piece | Choice |
|-------|--------|
| Runner | **TUnit** |
| Substitutes | **NSubstitute** (ports / interfaces) |
| Persistence integration | **Testcontainers** (real engine) |
| Architecture | **NetArchTest** (or maintained successor) |
| Clock in tests | **`FakeTimeProvider`** when time matters (**`time-and-ids`**) |

Ban EF **InMemory** for anything beyond throwaway smoke (**`db-integration`**). Ban mocking `DbSet` / EF internals.

## Pyramid

| Layer | Project | Covers |
|-------|---------|--------|
| **Unit** | `*.Tests.Unit` | Domain, pure Application logic with substituted ports |
| **Integration** | `*.Tests.Integration` | Handlers + real DB; host wiring / critical HTTP via `WebApplicationFactory` when needed |
| **Architecture** | `*.Architecture.Tests` | Dependency rule, no forbidden references — run on CI |

Prefer **DAMP** over clever shared hierarchies. Shared builders/fixtures are fine when they reduce noise without hiding the scenario.

Don’t ship I/O-heavy features with only happy-path unit tests.

## Naming and layout (Monetis-shaped)

**Folders:** mirror production areas under the test project (`Domain/Entities/`, `Application/CreditCards/`, …).

**Classes:** `{Sut}Tests` or `{Feature}{Scenario}Tests`  
Examples: `CreditCardTests`, `SettleStatementTests`, `GetFinancialInsightsRequestHandlerTests`.

**Methods:**

```text
{UnitUnderTest}_Should_{Expected}_When_{Scenario}
```

Examples:

- `AddTransaction_Should_DecrementAvailableLimit_When_SettledExpenseIsAdded`
- `Settle_Should_CreatePaymentAndLinkedTransaction_When_ManualUser`

Use TUnit `[Test]` (and setup/teardown attributes as needed). Prefer `async Task` test methods when awaiting.

## Unit tests

- Substitute **ports** and external boundaries — not the database
- Domain tests: real entities/VOs, no DI required
- Assert on observable outcomes; avoid brittle interaction-only tests unless the interaction *is* the contract

## Integration tests

- One container/scope strategy that keeps tests isolated (reset DB or fresh scope per test/class — pick one and document in the repo)
- Don’t point tests at a shared production/staging database
- Prefer testing through the handler (or HTTP) with real persistence over re-testing EF mappings alone

## Architecture tests

Enforce **`solution-structure`** rules at minimum:

- Application does not reference Infrastructure (ports-only)
- Domain has no outward infra/ASP.NET references
- Add rules when a recurring footgun appears

## Don't

- Don’t mock EF `DbSet` / change tracker
- Don’t use production databases for tests
- Don’t invent a second naming style next to `Should_When`
- Don’t skip Architecture tests on CI “to go faster”
- Don’t force 100% mock coverage of trivial code

## References

- [`references/examples.md`](references/examples.md) — naming + substitute sketch

## Related

- Layer projects → **`solution-structure`**
- Testcontainers / no InMemory → **`db-integration`**
- Clock fakes → **`time-and-ids`**
- TDD process → lifecycle **`test-driven-development`** / implement flow

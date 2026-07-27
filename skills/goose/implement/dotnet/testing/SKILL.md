---
name: testing
description: Use when writing or reviewing .NET tests — TUnit, NSubstitute, Testcontainers, architecture tests, naming — or when implement loads the dotnet pack for test work.
disable-model-invocation: true
metadata:
  area: goose
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
| Mutation | **Stryker.NET** (or equivalent) on **Unit** projects |
| Clock in tests | **`FakeTimeProvider`** when time matters (**`time-and-ids`**) |

Ban EF **InMemory** for anything beyond throwaway smoke (**`db-integration`**). Ban mocking `DbSet` / EF internals.

## Pyramid

| Layer | Project | Covers |
|-------|---------|--------|
| **Unit** | `*.Tests.Unit` | Domain, pure Application logic with substituted ports |
| **Integration** | `*.Tests.Integration` | Handlers + real DB; host wiring / critical HTTP via `WebApplicationFactory` when needed |
| **Architecture** | `*.Architecture.Tests` | Dependency rule, no forbidden references — run on CI |
| **Mutation** | Stryker vs Unit suite | Kills weak asserts — **CI gate** on PRs (see below) |

Prefer **DAMP** over clever shared hierarchies. Shared builders/fixtures are fine when they reduce noise without hiding the scenario.

Don’t ship I/O-heavy features with only happy-path unit tests.

## Mutation testing

**Scope:** mutate production code covered by **`*.Tests.Unit`** (Domain **and** Application unit tests) — not Domain-only.

**CI:** run on PRs that touch that code; **fail** below a mutation-score threshold configured in the target repo (Stryker config / pipeline).

**Out of PR gate by default:** Integration / Testcontainers suites (too slow and flaky for mutant fan-out). Optional slower lane (nightly) later if a critical path has almost no unit coverage.

Mutation is a protection layer on top of the pyramid — it does not replace Integration or Architecture tests.

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

## Quality traps (flaky / hollow tests)

| Trap | Fix |
|------|-----|
| `Thread.Sleep` / fixed delays for async | Await the real signal; condition-based wait |
| `DateTime.Now` / `UtcNow` in SUT or assert | Inject `TimeProvider` / `FakeTimeProvider` (**`time-and-ids`**) |
| Shared mutable statics across tests | Isolate; no order-dependent suites |
| Assert-less or tautological asserts | Assert the observable outcome that would fail if broken |
| Swallowing exceptions in act | Let failures surface; assert typed Result when that’s the contract |
| Mocking `DbSet` / change tracker | Ports + Testcontainers (**`db-integration`**) |

Deep audit catalogs stay in the Cursor **`dotnet-test`** plugins (`test-anti-patterns`, etc.) — this pack lists Goose’s recurring bans.

## Don't

- Don’t mock EF `DbSet` / change tracker
- Don’t use production databases for tests
- Don’t invent a second naming style next to `Should_When`
- Don’t skip Architecture tests on CI “to go faster”
- Don’t skip mutation on Unit just because Integration is green
- Don’t force 100% mock coverage of trivial code
- Don’t point Stryker at the full Integration suite on every PR
- Don’t sleep to “wait for” async work
- Don’t let wall-clock time make tests flake

## References

- [`references/examples.md`](references/examples.md) — naming, substitute, mutation sketch

## Related

- Layer projects → **`solution-structure`**
- Testcontainers / no InMemory → **`db-integration`**
- Clock fakes → **`time-and-ids`**
- TDD process → parent **`implement`** (red-green-refactor at agreed seams)
- Broader test audits (plugin) → Cursor **`dotnet-test`**

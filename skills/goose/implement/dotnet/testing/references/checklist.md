| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Architecture tests are required for the ports-only rule (dependency direction, no forbidden references), and run on CI | architecture-test | Pyramid / Architecture tests — `AppLayerTests`, `DomainPurityTests`, `ApplicationPurityTests` |
| Ban EF InMemory for anything beyond throwaway smoke; ban mocking `DbSet` / EF internals | architecture-test | Stack — assembly-dependency ban on `Microsoft.EntityFrameworkCore.InMemory` in test projects |
| `dotnet format` (or IDE equivalent) clean on CI | editorconfig | Naming and layout — IDE0055, see `code-style` skill |
| Mutation testing runs on PRs that touch Unit-tested code (Domain + Application); CI fails below the configured mutation-score threshold | verify | Mutation testing |
| Test classes named `{Sut}Tests` or `{Feature}{Scenario}Tests`; methods `{UnitUnderTest}_Should_{Expected}_When_{Scenario}` | verify | Naming and layout |
| Unit tests substitute ports and external boundaries — not the database | verify | Unit tests |
| Integration tests use one documented container/scope strategy; don't point tests at a shared production/staging database | verify | Integration tests |
| `Thread.Sleep`/fixed delays for async are a trap — await the real signal or a condition-based wait | verify | Quality traps |
| `DateTime.Now`/`UtcNow` in the SUT or an assertion is a trap — inject `TimeProvider`/`FakeTimeProvider` | verify | Quality traps |
| Assert the observable outcome that would fail if broken — no assert-less or tautological asserts | verify | Quality traps |
| Don't invent a second naming style next to `Should_When` | verify | Don't |
| Don't skip Architecture tests on CI "to go faster" | verify | Don't |
| Don't skip mutation on Unit just because Integration is green | verify | Don't |
| Don't let wall-clock time make tests flake | verify | Don't |

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Use `TimeProvider` wherever production code needs "now" in Domain or Application; don't call `DateTime.Now`/`UtcNow`/`DateTimeOffset.Now` on those paths | analyzer | Clock — banned-API analyzer (`BannedApiAnalyzers`), exact symbol match |
| Register `TimeProvider.System` (or a test fake) in DI | verify | Clock |
| Process and store instants in UTC; keep a user/tenant `DateTimeZone` when the product needs "today for this user" | verify | Time types |
| Strongly typed IDs used instead of raw `Guid`/`int` on public domain APIs, where it matters | verify | IDs — "where it matters" is a per-type judgment call |
| Aggregate/entity identity uses app-generated `Guid` version 7 (`Guid.CreateVersion7()`), wrapped in a typed id | verify | IDs |
| Human-facing numbers (invoice #, ticket #) use a DB sequence — not a random Guid shown to users | verify | IDs |
| Prefer `FakeTimeProvider` (or an advanceable test double) when behavior depends on time | verify | Testing |
| Don't store local wall time as if it were UTC | verify | Don't |
| Don't mix `DateTime` Kind-unspecified with NodaTime `Instant` without an explicit conversion | verify | Don't |
| Don't show raw DB sequences as security tokens | verify | Don't |

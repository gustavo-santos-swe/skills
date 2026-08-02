| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Aggregate roots are the consistency boundary; outsiders reference roots by id only — not every entity is a root | verify | Building blocks |
| Prefer a rich model: state changes and invariants live on entities/VOs as methods; Application orchestrates, it doesn't set every property from the outside | verify | Building blocks |
| Strongly typed IDs by default on public domain APIs (e.g. `CreditCardId`), not bare `Guid` | verify | IDs — needs per-type "where it matters" judgment |
| Don't pass domain meaning as bare `string`/`int`/`bool`/`Guid` when a type (enum, value object, typed id) would catch mistakes | verify | Avoid primitive obsession |
| Invariant the app/API should already have blocked → throw; parsing raw input into a VO, or an expected refusal from current state → Result/union | verify | Invariants and failures |
| Domain events: raise on the aggregate, persist, dispatch after successful save, then clear | verify | Domain events |
| Domain events start in-process; durable/cross-service delivery goes through `messaging` (outbox when needed) | verify | Domain events |
| Domain must not depend on EF Core / DbContext / data annotations as the model | architecture-test | Persistence ignorance |
| Domain must not depend on ASP.NET / `HttpContext` | architecture-test | Persistence ignorance |
| Domain must not depend on `ILogger` or other infra SDKs | architecture-test | Persistence ignorance |
| Don't make every entity an aggregate root | verify | Don't |
| Don't span multiple consistency boundaries in one aggregate for convenience | verify | Don't |
| Don't put use-case orchestration in entities | verify | Don't |
| Don't use EF data-annotation attributes as the only expression of the domain model | architecture-test | Don't — see `db-integration` for the matching reflection check on Domain types |
| Don't return Result from every mutator when the failure is truly unexpected after validation | verify | Don't |

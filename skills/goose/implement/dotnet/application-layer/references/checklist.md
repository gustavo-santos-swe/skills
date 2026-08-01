| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| One use case = one file; colocate request, response, validator, and handler interface/impl | verify | Shape of a use case |
| Don't use MediatR (or equivalent) unless the target repo already standardized on it — explicit handler interfaces, registered in DI | verify | Shape of a use case / Don't |
| Requests/responses are Application DTOs; handlers must not return raw Domain entities | architecture-test | DTOs and mapping — `HandlerContractTests.Handlers_ShouldNotReturnDomainEntitiesDirectly_BeyondKnownBaseline` |
| Manual mapping in the handler (or small private helpers); never return tracked EF entities from a handler | verify | DTOs and mapping |
| Per-use-case request/response types — don't share "read models" across GET/LIST to DRY | verify | DTOs and mapping |
| FluentValidation runs first in the handler; failure returns `ValidationFailed` → 422 | verify | Validation |
| Greenfield/ports-only: handler calls repositories, UoW, gateways, clock, current user via ports — no raw `HttpClient`, no Infrastructure project references | architecture-test | What the handler may call — `AppLayerTests.Application_ShouldNotDependOn_Infrastructure` |
| Application must not depend on `Microsoft.AspNetCore.Http` or raw broker SDKs (Hangfire, bus clients) | architecture-test | What the handler may call — `ApplicationPurityTests` |
| The handler owns the write boundary: one use case ≈ one commit unless explicitly documented otherwise | verify | Transactions |
| Host owns authentication + coarse authorization; handler owns resource/ownership checks | verify | Authz and other cross-cutting |
| Don't skip resource checks because the endpoint already has a role check | verify | Don't |
| No default idempotency-key store — when a command can be retried/double-submitted in a way that hurts, stop and design for that case explicitly | verify | Idempotency |
| Don't add a global idempotency middleware by default | verify | Don't |
| Dispatch domain events after successful save, not before | verify | Handler flow |

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Express success/failure with a typed union or `Result<T>` with typed failure cases (`NotFound`, `ValidationFailed`, `Forbidden`, `Conflict`) | verify | Core model |
| Throw for bugs and unexpected faults; don't throw for outcomes the API should return as a stable client error | verify | Core model |
| One host-level mapper maps each `Result<T>` failure case to the documented HTTP status (422/404/403/409); unhandled → 500 | regression-test | HTTP mapping — endpoint test per failure variant |
| No stack traces or internals exposed to clients | verify | HTTP mapping |
| Per-endpoint status invention is a smell — extend the shared mapper instead | verify | HTTP mapping |
| Known infra failures (unique constraint, concurrency conflict) translate to `Conflict`; unknown/outage failures bubble to 500 + log, not swallowed | verify | Infrastructure failures |
| Expected union failures (4xx) are not logged at Error; unhandled/500s are Error + exception with trace/correlation id | verify | Logging — quiet 4xx, loud 500 is a per-path severity judgment |
| One unhandled-exception pipeline at the host; no catch-all that turns bugs into empty 200/400 | verify | Consistency |
| Don't introduce a new failure-case type for every feature when `NotFound` + a code suffices | verify | Don't |
| Don't introduce unions into a repo that already standardized on `Result` without an explicit migrate ask | verify | Don't |
| Don't log every 404 at Error level | verify | Don't |

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Enqueue/schedule from the handler/host after the decision is made — not heavy work on the request thread | verify | Hangfire |
| Persist job storage (Postgres/SQL) — don't run memory-only storage in production | verify | Hangfire |
| Retries are at-least-once — job bodies must be idempotent when re-run | verify | Hangfire |
| Hangfire dashboard is authz-gated, not anonymous | regression-test | Hangfire — integration test hitting the dashboard route unauthenticated, expects 401/403 |
| Outbox is used only where the DB write and publish/enqueue must succeed or fail together — don't dual-write `SaveChanges()` then `Enqueue()` when that atomicity matters | verify | Atomicity with DB — "must be atomic" is a product-risk judgment per use case |
| Long-running hosted-service loops use a linked `CancellationToken` and shut down promptly; don't block host shutdown waiting forever | verify | Hosted services |
| Don't start background loops from controllers/endpoints | verify | Hosted services |
| No fire-and-forget (`Task.Run`, discarded tasks) when losing the work matters — enqueue instead | verify | Request-path rules |
| Don't use Hangfire as a multi-service integration bus | verify | Don't |
| Don't assume a job runs exactly once | verify | Don't |
| Don't ignore orphan/cleanup jobs when uploads create abandoned blobs | verify | Don't |

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Register vendor clients as typed clients via `AddHttpClient<TClient>()` inside the Infra slice that owns that vendor | verify | Defaults |
| Config (base address, API keys, per-dependency timeouts) comes from typed options with `ValidateOnStart` | verify | Defaults |
| Apply `AddStandardResilienceHandler()` (or a tuned equivalent) on outbound clients | verify | Defaults |
| Application depends on the typed client or a port it implements — not `IHttpClientFactory` sprinkled through handlers | verify | Defaults |
| Don't call `new HttpClient()` per call (or a naive long-lived singleton without a factory) | analyzer | Hard bans — banned-API analyzer on the constructor symbol |
| Don't do blind retries on non-idempotent POSTs without an idempotency key | verify | Hard bans |
| Don't fetch user-supplied URLs server-side without an allowlist (SSRF) | verify | Hard bans — see `security` skill |
| Outbound DTOs are this integration's own contracts — don't reuse ASP.NET request DTOs as wire types to third parties | verify | Contracts |
| Timeouts are per dependency, not one global timeout for every vendor | verify | Contracts |
| Don't log full outbound bodies with secrets/PII | verify | Don't |
| Don't skip resilience on flaky third parties "to ship faster" | verify | Don't |

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| ASP.NET rate limiter (`AddRateLimiter`) owns product quotas; don't rely on a gateway/WAF shield alone for authenticated per-user limits | verify | Where limits live |
| Partition authenticated clients by user id, anonymous clients by IP (only with correct forwarded-headers config) | verify | Partitioning and algorithms |
| Don't use IP-only limits for logged-in traffic behind shared NATs | verify | Don't |
| Exceeded requests return 429 with a Problem Details body (+ `Retry-After` when computable) | regression-test | Responses — trigger the limiter in a test, assert response shape |
| `/alive` and `/health` are excluded from the rate limiter | regression-test | Exemptions — assert the limiter policy config excludes those routes |
| Internal/admin bypass only behind real authz — not a secret query string | verify | Exemptions |
| Store outage prefers fail-open for availability unless the endpoint is abuse-critical (then fail-closed, documented) | verify | In-process vs distributed |
| Count throttled requests as a metric; avoid Error-logging every 429 | verify | Observability |
| Don't trust `X-Forwarded-For` from the open internet without a known proxy | verify | Don't |

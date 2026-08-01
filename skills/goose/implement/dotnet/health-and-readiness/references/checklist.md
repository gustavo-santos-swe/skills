| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| `/alive` (liveness) is cheap-only, tagged `live`/`self`, and never checks downstream dependencies | verify | Endpoints |
| Readiness registers a check for every dependency the app truly can't serve without; `/health` fails if any registered check is not Healthy | verify | What readiness includes — "truly can't serve without" is a product call, not a structural fact |
| Per-check timeouts are short (seconds, not tens of seconds); timeout or failure → Unhealthy → not ready | verify | Timeouts and status |
| Readiness is binary for traffic — non-Healthy fails the probe; use `Degraded` sparingly and document it | verify | Timeouts and status |
| No expensive full-system tests on every probe tick | verify | Timeouts and status |
| Detailed dependency breakdown on open `/health` requires a conscious exposure decision (cluster-only, probe key, or status-only) | verify | Exposure and payload |
| Hard ban: no secrets, connection strings, tokens, or raw exception dumps in health JSON | verify | Exposure and payload |
| Don't run migrations or heavy queries inside a health check | verify | Don't |
| Don't point production probes at a shared staging database "for convenience" | verify | Don't |

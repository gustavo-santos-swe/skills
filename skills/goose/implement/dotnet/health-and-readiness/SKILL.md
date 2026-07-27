---
name: health-and-readiness
description: Use when adding or reviewing ASP.NET health/readiness probes — /alive vs /health, dependency checks, timeouts, exposure — or when implement loads the dotnet pack for probe work.
metadata:
  area: goose
---

# Health and Readiness

Goose handbook for ASP.NET health checks and deploy/LB probes.

**Target repo wins** if probe paths, auth, or payload style are already settled.

Voice: **`write-like-goose`**.

## When to use

- Wiring probes for K8s/ECS/Aspire/load balancers
- Adding dependency health checks
- **`implement`** loading this pack

## Endpoints (greenfield)

Aspire-shaped (matches `ServiceDefaults` when present):

| Path | Role | Checks |
|------|------|--------|
| **`/alive`** | Liveness | Cheap only — tagged `live` / `self`. **Never** downstream deps. |
| **`/health`** | Readiness | All registered dependency checks must pass. |

Optional **startup** probe may reuse readiness (or a warm-up check) when the host is slow to bind.

Map with `MapHealthChecks` + tag predicates — don’t invent a third public status API unless the target already has one.

## What readiness includes

**Register a check for every dependency the app declares** (DB, cache, bus, critical typed clients, etc.). Readiness fails if any registered check is not Healthy.

That is aggressive: a flaky optional vendor can take you out of rotation. Prefer not registering soft deps as health checks — or register them only when product truly can’t serve without them. When in doubt, ask.

Liveness stays process-only so a DB blip doesn’t restart-loop the pod.

## Timeouts and status

- Per-check **short timeouts** (seconds, not tens of seconds)
- Timeout or failure → **Unhealthy** → not ready
- Treat readiness as **binary** for traffic: non-Healthy fails the probe. Use `Degraded` sparingly (document if you do); don’t rely on “Degraded but still 200” unless the target already does
- No expensive full-system tests on every probe tick

## Exposure and payload

**Greenfield default:** detailed dependency breakdown on open `/health` (names + status; useful for ops).

**Hard ban:** secrets, connection strings, tokens, or raw exception dumps with internals in the JSON.

**Decision checkpoint (required):** when adding or changing probes — in the PR (and when `implement` touches this) — **call out exposure** so an engineer chooses consciously:

- leave detailed `/health` open but **only on the cluster/VPC** (not public ingress), or
- add a probe key / internal-only route, or
- switch public probes to status-only

Don’t ship detailed health to the public internet by accident. Target-repo patterns (auth, minimal payload) override the greenfield default.

## Don't

- Don’t put DB/cache/HTTP deps on liveness
- Don’t run migrations or heavy queries inside a check
- Don’t return connection strings or secrets in health JSON
- Don’t skip the exposure warning on greenfield detailed `/health`
- Don’t point production probes at a shared staging database “for convenience”

## References

- [`references/examples.md`](references/examples.md) — map + check registration sketch

## Related

- Telemetry on failures → **`observability`**
- Connection strings / options → **`configuration`** / **`dependency-injection`**
- DB adapter → **`db-integration`**

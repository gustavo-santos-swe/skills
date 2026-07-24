---
name: health-and-readiness
description: ASP.NET health and readiness checks for deps and deploy gates. Use when adding or changing /health, /ready, dependency checks, or Kubernetes/load-balancer probe wiring in .NET.
disable-model-invocation: true
metadata:
  area: wip
---

# Health and Readiness

Status: **stub** — topic list below is what to define later. Keep SKILL.md short; deep samples → `references/`.

## When to use

- Probes for orchestrators/LBs; “is this instance safe to receive traffic?”
- **`implement`** loading this pack when changing health endpoints or checks.

## Topics to fill (checklist)

### Endpoints
- Liveness vs readiness vs startup — paths we expose (`/health`, `/ready`, …)
- What each must (not) check (liveness stays cheap)

### Checks
- DB, cache, bus, disk — which are readiness blockers
- Timeouts per check; failure thresholds
- Degraded vs unhealthy — do we distinguish?

### Security & exposure
- Public vs internal-only probes; auth on detailed health?
- Payload: minimal status vs dependency detail (don’t leak internals publicly)

### Hosting
- K8s/ECS probe config expectations (or point to ops docs in the repo)
- Warmup / startup probes for slow hosts

### Align with
- observability (metrics on check failures), configuration (connection strings), db-integration / messaging (how we ping deps)

## Don't

- Don't make liveness depend on downstreams (causes kill loops).
- Don't run expensive full-system tests on every probe.
- Don't return secrets or connection strings in health JSON.

## References

Optional: `references/` for check registration samples. Probe URLs in charts stay in the target repo.

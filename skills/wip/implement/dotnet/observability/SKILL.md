---
name: observability
description: Use when adding or reviewing .NET telemetry — OpenTelemetry traces/metrics, MEL structured logging, correlation, PII rules — or when implement loads the dotnet pack for observability work.
disable-model-invocation: true
metadata:
  area: wip
---

# Observability

Goose handbook for logs, traces, and metrics in .NET backends. Logs live here (not a separate skill).

**Target repo wins** if the project already standardized on Serilog + a vendor APM (e.g. New Relic). Defaults below are for **greenfield**.

Voice: **`write-like-goose`**.

## When to use

- Wiring telemetry, choosing what to span/log/meter
- Incident debugging conventions
- **`implement`** loading this pack

## Stack (greenfield)

| Piece | Choice |
|-------|--------|
| Traces / metrics | **OpenTelemetry** (Aspire `ServiceDefaults` when present) |
| Logs | **MEL** (`ILogger<T>`) bridged into the OTel / host pipeline |
| Export | **OTLP** — local collector / Aspire dashboard; prod backend via config |
| Custom instrumentation | **OTel API / shim** (Tracer, span, attributes) — not a vendor SDK in app code |

Sampling and exporter endpoints are **environment config**, not hard-coded in handlers.

## Traces

**Default instrumentation:** ASP.NET request + outbound HttpClient / EF (and other OTel instrumentations you enable). That’s enough for most paths.

**Custom spans:** only when a flow is opaque. When you add them, use OTel terminology/API (shim), not New Relic / App Insights types in Application code.

Don’t create a span per handler or per validation step by default.

## Logging

- Message **templates** with named args: `"Settled {StatementId}"` — not string interpolation into the template
- Stable ids via **scopes** / baggage (`UserId`, `TenantId`) when useful across a request
- Levels: Information for lifecycle; Warning for recoverable oddities; **Error for faults**
- Align with **`error-handling`**: quiet expected 4xx (Debug/none); loud unhandled / 500 (Error + exception, once at the edge)
- Include trace/correlation id via the pipeline — don’t invent a second correlation header scheme

## PII and secrets

Hard ban in logs **and** span attributes:

- Secrets, tokens, passwords, connection strings
- Full card / CPF / PAN / raw auth headers
- Full request/response bodies by default

Prefer opaque ids. Email/phone only when product requires and with redaction/hash — default **off**. Central scrubbers are backup, not permission to log freely.

## Metrics

- Start with **RED** (and runtime) from ASP.NET / HttpClient / process instrumentations
- Add custom meters only for product KPIs / SLOs you will actually alert on
- Keep label cardinality low (no raw user ids as metric labels)

## Local vs prod

Same shape everywhere: OTel + MEL → OTLP (and console/JSON logs as configured). Only the destination and sampling change per environment. Don’t run a different mental model locally than in prod.

## Don't

- Don’t put vendor APM APIs in Application/Domain for greenfield
- Don’t log every NotFound at Error
- Don’t log secrets or full payloads “just for Debug”
- Don’t sprinkle custom spans on every use case
- Don’t invent a second correlation id beside the trace

## References

- [`references/examples.md`](references/examples.md) — log template + optional custom span sketch

## Related

- Failure logging levels → **`error-handling`**
- Outbound clients → **`http-clients`** / **`dependency-injection`**
- Retries / timeouts → **`resilience`**
- Probes → **`health-and-readiness`**

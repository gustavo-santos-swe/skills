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
| Traces / metrics | **OpenTelemetry** (Aspire `ServiceDefaults` when present — prefer that over hand-rolling) |
| Logs | **MEL** (`ILogger<T>`) bridged into the OTel / host pipeline |
| Export | **OTLP** — local collector / Aspire dashboard; prod backend via config |
| Custom instrumentation | **OTel API / shim** (Tracer, span, attributes) — not a vendor SDK in app code |

Sampling and exporter endpoints are **environment config**, not hard-coded in handlers.

### Packages (when not using Aspire defaults)

Install the hosting + instrumentations + OTLP exporter — **not** bare `OpenTelemetry` alone:

- `OpenTelemetry.Extensions.Hosting`
- `OpenTelemetry.Instrumentation.AspNetCore`
- `OpenTelemetry.Instrumentation.Http`
- `OpenTelemetry.Exporter.OpenTelemetryProtocol`

Add only what you use: `EntityFrameworkCore` / `SqlClient` / `Runtime` / `GrpcNetClient` instrumentations. Console exporter is **dev-only**, not a prod dependency.

Wire traces + metrics + logging through one `AddOpenTelemetry()` → `UseOtlpExporter()` (or Aspire equivalent). Endpoint / protocol: gRPC **4317** vs HTTP/protobuf **4318** — match the collector.

## Traces

**Default instrumentation:** ASP.NET request + outbound HttpClient / EF (and other OTel instrumentations you enable). That’s enough for most paths.

**Filter noise:** exclude probe paths from ASP.NET spans (`/alive`, `/health`, and whatever **`health-and-readiness`** uses) so dashboards aren’t flooded.

**Custom spans:** only when a flow is opaque. When you add them, use OTel terminology/API (shim), not New Relic / App Insights types in Application code.

- Register every custom `ActivitySource` name with `.AddSource("…")` — unmatched sources silently produce **null** activities (common footgun)
- Prefer `ILogger` for exceptions on the path (trace correlation via `.WithLogging`); don’t invent a second exception channel

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
- Create meters via **`IMeterFactory`** (DI); register meter names with `.AddMeter("…")` — same silent-drop footgun as ActivitySource
- Keep label cardinality low (no raw user ids / UUIDs as metric labels)

## Local vs prod

Same shape everywhere: OTel + MEL → OTLP (and console/JSON logs as configured). Only the destination and sampling change per environment. Don’t run a different mental model locally than in prod.

## Failure modes (agent traps)

| Temptation | Why it hurts | Do instead |
|------------|--------------|------------|
| Install only `OpenTelemetry` | No DI hosting | `Extensions.Hosting` + instrumentations + OTLP |
| Custom `ActivitySource` not in `AddSource` | Spans silently null | Register every source name |
| Trace every health poll | Noise / cost | Filter `/alive` + `/health` |
| UserId as metric tag | Cardinality explosion | Counts/RED; ids in logs/spans sparingly |
| Vendor SDK in Application | Lock-in | OTel API + MEL |

## Don't

- Don’t put vendor APM APIs in Application/Domain for greenfield
- Don’t log every NotFound at Error
- Don’t log secrets or full payloads “just for Debug”
- Don’t sprinkle custom spans on every use case
- Don’t invent a second correlation id beside the trace
- Don’t ship Console exporter as a production dependency

## References

- [`references/examples.md`](references/examples.md) — packages, host wiring, log template, custom span

## Related

- Failure logging levels → **`error-handling`**
- Outbound clients → **`http-clients`** / **`dependency-injection`**
- Retries / timeouts → **`resilience`**
- Probes → **`health-and-readiness`**
- Full install recipes (plugin) → Cursor **`dotnet-aspnetcore`** / `configuring-opentelemetry-dotnet`

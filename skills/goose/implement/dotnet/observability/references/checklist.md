| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Install `OpenTelemetry.Extensions.Hosting` + instrumentations + OTLP exporter — not bare `OpenTelemetry` alone | verify | Stack |
| Filter probe paths (`/alive`, `/health`) out of ASP.NET spans so dashboards aren't flooded | verify | Traces |
| Custom spans use the OTel API/shim (`Tracer.StartActiveSpan`) — not `ActivitySource`/`Activity` in Application code | architecture-test | Traces — assembly/type-dependency ban on `ActivitySource`/`Activity` in Application |
| Tracer/meter names are registered with `.AddSource(...)` / `.AddMeter(...)` on the host — unmatched names silently drop telemetry | verify | Traces / Metrics |
| Log message templates use named args (`"Settled {StatementId}"`) — not string interpolation into the template | analyzer | Logging — CA2254, built-in logging analyzer |
| Log levels: Information for lifecycle, Warning for recoverable oddities, Error for faults; quiet expected 4xx, loud unhandled/500 | verify | Logging — per-path severity judgment |
| Hard ban on secrets, tokens, passwords, connection strings, full PII, and full request/response bodies in logs and span attributes | verify | PII and secrets — "is this value sensitive" is a semantic judgment, not a fixed banned-symbol list |
| Custom meters use `IMeterFactory`; keep label cardinality low (no raw user ids/UUIDs as metric labels) | verify | Metrics |
| Don't put vendor APM SDK types (New Relic, App Insights) in Application/Domain for greenfield | verify | Don't |
| Don't sprinkle custom spans on every use case | verify | Don't |
| Don't invent a second correlation id beside the trace | verify | Don't |
| Don't ship the Console exporter as a production dependency | verify | Don't |

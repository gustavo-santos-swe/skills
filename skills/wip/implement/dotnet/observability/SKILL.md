---
name: observability
description: OpenTelemetry traces/metrics, structured logging, correlation — logs live here. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Observability

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Logging, traces, or metrics on a .NET service.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Logging
- Structured (MEL/Serilog); message templates; levels
- Correlation / trace id on every request
- PII redaction rules

### Tracing
- Activity names; important spans (handler, DB, outbound HTTP)
- Sampling policy (if any)

### Metrics
- RED/USE or our KPIs; business vs tech metrics
- Naming conventions

### Errors
- Exception logging once; align with error-handling

### Local vs prod
- Console JSON; exporters we use

## Don't
- Don't log secrets or full payloads with PII.
- Don't invent a second correlation mechanism beside the trace id.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

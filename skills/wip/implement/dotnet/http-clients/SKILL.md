---
name: http-clients
description: IHttpClientFactory, typed clients, outbound resilience. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# HTTP Clients

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Calling external HTTP APIs from .NET.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Registration
- Typed clients vs named; base addresses; auth handlers

### Resilience
- Standard pipeline (timeouts/retries) — point to resilience

### Contracts
- How we version outbound DTOs; timeouts per dependency

### Testing
- How we fake outbound HTTP

## Don't
- Don't new HttpClient() per call.
- Don't ignore Polly/standard resilience for flaky deps.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

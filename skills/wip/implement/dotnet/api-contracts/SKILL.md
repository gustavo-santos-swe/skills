---
name: api-contracts
description: OpenAPI, versioning, backward compatibility of public APIs. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# API Contracts

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Public API shape, OpenAPI, or version bumps.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Compatibility
- What counts as breaking; additive changes policy
- Deprecation headers / timeline

### Versioning
- Strategy (URL/header); when to cut vNext

### OpenAPI
- Source of truth; review checklist for PR

### Clients
- Generated clients? public vs private consumers

### Align with
- endpoint-conventions, documentation (ship-docs)

## Don't
- Don't break field meaning while keeping the same name.
- Don't ship undocumented public endpoints.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

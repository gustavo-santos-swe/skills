---
name: security
description: AuthN/Z, secrets, data protection, input at trust boundaries (.NET-specific). Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Security

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Auth, secrets, or trust-boundary handling in .NET.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### AuthN
- JWT / cookies / schemes we use; token validation rules

### AuthZ
- Policies vs roles vs resource-based; where enforced (endpoint vs handler)

### Secrets & protection
- Data Protection; secret storage; connection strings

### Input at boundaries
- Mass assignment; file upload; SSRF via user URLs

### Align with
- wip `security-check` (process gate); this skill = .NET how-to
- database (data-at-rest policies)

## Don't
- Don't trust client-sent roles/tenant ids without server checks.
- Don't disable HTTPS or certificate validation for local in shared code.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

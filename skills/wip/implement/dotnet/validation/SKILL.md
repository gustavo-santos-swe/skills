---
name: validation
description: Boundary vs domain validation, FluentValidation/DataAnnotations conventions. Use when writing or reviewing .NET/C# code in this area, or when the implement skill loads this pack.
disable-model-invocation: true
metadata:
  area: wip
---

# Validation

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Request/command validation rules.
- **`implement`** loading this pack for a .NET change.

## Topics to fill (checklist)

### Layers
- Boundary (format, required fields) vs domain invariants — split
- What FluentValidation / DataAnnotations cover vs domain methods

### Timing
- Validate before handler body; fail fast with ProblemDetails

### Messages
- User-facing vs log-facing; localization later?

### Cross-field rules
- Where they live; examples we care about

### Align with
- endpoint-conventions (binding), error-handling (400 shape), domain-modeling (invariants)

## Don't
- Don't rely on validation alone for security (authz/integrity).
- Don't duplicate domain invariants only in the validator.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.

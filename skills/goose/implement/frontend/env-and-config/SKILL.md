---
name: web-env-and-config
description: Use when adding environment variables, `NEXT_PUBLIC_*`, or runtime config in Next.js.
disable-model-invocation: true
metadata:
  area: goose
---

# Env and Config

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- New secrets, public env, env validation.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Boundaries
- Server-only vs `NEXT_PUBLIC_` — checklist
- Validate env at build/start (t3-env or zod)

### Environments
- Dev/preview/prod values; never commit secrets

### Align with
- auth, route-handlers, security

## Don't
- Don't prefix secrets with `NEXT_PUBLIC_`.
- Don't read `process.env` ad hoc in dozens of files without a validated config module.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


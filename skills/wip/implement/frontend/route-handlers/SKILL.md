---
name: web-route-handlers
description: Use when adding Next.js Route Handlers (`app/api`) or webhook endpoints.
disable-model-invocation: true
metadata:
  area: wip
---

# Route Handlers

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Webhooks, public JSON APIs, non-form HTTP endpoints.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### When
- Webhooks, external clients, non-action HTTP — vs Server Actions for first-party UI

### Design
- Versioning; error shape; auth (API keys/JWT)
- Edge vs Node runtime choice

### Align with
- api-contracts mindset; backend may own real API — when Next is BFF only

## Don't
- Don't build a second domain API in route handlers if the .NET API is source of truth — BFF only when intentional.
- Don't block the edge runtime with Node-only APIs without choosing Node explicitly.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


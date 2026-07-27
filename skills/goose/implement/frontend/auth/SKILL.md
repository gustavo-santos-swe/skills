---
name: web-auth
description: Use when implementing Next.js authentication — sessions, Auth.js/Clerk/etc., protected routes, or server auth helpers.
disable-model-invocation: true
metadata:
  area: goose
---

# Auth

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Login, session cookies, protecting RSC/actions.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Stack
- Library choice (Auth.js, Clerk, custom) — our default
- Session strategy (JWT cookie vs server session)

### Enforcement
- Where we check auth: middleware, RSC, actions, route handlers — defense in depth
- RBAC / roles claim shape

### Align with
- security, middleware, server-actions-and-forms

## Don't
- Don't trust client-passed user ids for authz.
- Don't expose session tokens to client JS if httpOnly cookies are the model.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


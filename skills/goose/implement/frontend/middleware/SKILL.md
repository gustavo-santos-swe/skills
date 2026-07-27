---
name: web-middleware
description: Use when adding or changing Next.js middleware (auth redirects, headers, geo, A/B gates).
metadata:
  area: goose
---

# Middleware

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Matcher config, auth gate at edge, security headers.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Scope
- What middleware may do (rewrite/redirect/headers) vs must not (heavy I/O)
- Matcher hygiene — don't run on every static asset

### Auth
- Session check patterns; align with auth skill
- Avoid giant JWT verification cost on every request if we have a lighter pattern

### Headers
- Security headers here vs host config

## Don't
- Don't turn middleware into a full app server.
- Don't fetch databases from middleware as a default.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


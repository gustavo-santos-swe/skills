---
name: web-security
description: Use when hardening a Next.js app — headers, XSS/CSRF, SSRF, uploads, or secret handling on the web tier.
disable-model-invocation: true
metadata:
  area: goose
---

# Security

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Trust-boundary changes on the Next app, headers, dangerous HTML.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Headers & CSP
- What we set (middleware vs host); CSP posture

### XSS / HTML
- `dangerouslySetInnerHTML` policy; sanitization
- URL/redirect validation

### Server surfaces
- Authz on actions/handlers; upload limits
- SSRF when server fetches user-provided URLs

### Align with
- `security-check`; env-and-config; auth

## Don't
- Don't render unsanitized user HTML.
- Don't expose verbose error digests or secrets in client responses.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


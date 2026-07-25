---
name: security
description: Use when adding or reviewing .NET AuthN/Z, HTTPS, trust-boundary input, or data protection — or when implement loads the dotnet pack for security work.
disable-model-invocation: true
metadata:
  area: wip
---

# Security

Goose handbook for AuthN/Z and trust boundaries in .NET backends.

**Target repo wins** if schemes/policies are already settled.

Voice: **`write-like-goose`**.

Process gate for a change/PR → wip **`security-check`**. Secrets *sources* → **`configuration`**. This skill is **.NET how**.

## When to use

- Login schemes, policies, resource ownership checks
- HTTPS, SSRF, mass assignment, upload limits
- **`implement`** loading this pack

## AuthN (greenfield)

| Client | Default |
|--------|---------|
| API / mobile / SPA calling API | **Bearer JWT** (or opaque token via IdP) — validate issuer, audience, lifetime, signing keys |
| Same-site browser app with server session | **Cookies** + **antiforgery** (CSRF) — Monetis-shaped; OK when that’s the host model |

Don’t invent custom “API key in random header” auth without a written reason. Don’t disable certificate validation in shared libraries for local convenience.

## AuthZ

Matches **`application-layer`**:

| Layer | Enforces |
|-------|----------|
| **Host** | Authenticated + coarse policies/roles/scopes (`[Authorize]`, `RequireAuthorization`) |
| **Handler** | Resource ownership / tenant — load the entity and check; **never trust** client-sent `userId` / `tenantId` as authority |

Prefer **named policies** over scattered magic role strings. Missing auth on a new endpoint is a defect, not a follow-up.

## Transport and data protection

- HTTPS outside local Development; HSTS when appropriate for the host
- ASP.NET **Data Protection** for protected cookies / time-limited payloads when you need them
- Connection strings and API keys only via options/secret store (**`configuration`**)

## Input at trust boundaries

- Bind **request DTOs**; map manually into domain — no binding client JSON straight onto entities (mass assignment)
- User-supplied URLs used for server-side fetch → **allowlist** / block internal ranges (SSRF)
- File uploads → size, content-type, and storage rules in **`file-storage`**
- Validation at the boundary → **`validation`**; don’t rely on “the client wouldn’t send that”

## Don't

- Don’t trust client-sent roles, tenant ids, or “isAdmin” flags
- Don’t put secrets in source, logs, health JSON, or span attributes
- Don’t disable HTTPS / cert validation in shared code paths
- Don’t leave new endpoints anonymous by accident
- Don’t treat the API gateway as the only security layer

## References

- [`references/examples.md`](references/examples.md) — policy + ownership sketch

## Related

- Handler ownership checks → **`application-layer`**
- Secret loading → **`configuration`**
- PII in telemetry → **`observability`**
- PR security pass → **`security-check`**

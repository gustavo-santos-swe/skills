---
name: security
description: Use when adding or reviewing .NET AuthN/Z, HTTPS, CORS, CSRF, trust-boundary input, or data protection — or when implement loads the dotnet pack for security work.
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
- HTTPS, CORS, CSRF, SSRF, mass assignment, upload limits
- **`implement`** loading this pack

## AuthN (greenfield)

| Client | Default |
|--------|---------|
| API / mobile / SPA calling API | **Bearer JWT** (or opaque token via IdP) |
| Same-site browser app with server session | **Cookies** + **antiforgery** (CSRF) — Monetis-shaped; OK when that’s the host model |

### JWT validation

Validate **all** of: **authority** (IdP metadata when available), **audience**, **lifetime**, **signing keys**. Don’t ship “lifetime + signature only” or “disable validation in Development” as a shared default.

Don’t invent custom “API key in random header” auth without a written reason. Don’t disable certificate validation in shared libraries for local convenience.

### Cookies + CSRF

| Host model | CSRF |
|------------|------|
| **JWT Bearer API** | No antiforgery dance — token isn’t sent automatically by the browser like a session cookie |
| **Cookie session** | **SameSite** (`Lax` or `Strict` as appropriate; `Secure` outside Development) **and antiforgery** on mutating endpoints (POST/PUT/PATCH/DELETE). SameSite alone is not enough when cookies are cross-site / `SameSite=None` |

## AuthZ

Matches **`application-layer`**:

| Layer | Enforces |
|-------|----------|
| **Host** | Authenticated + coarse policies/roles/scopes (`[Authorize]`, `RequireAuthorization`) |
| **Handler** | Resource ownership / tenant — load the entity and check; **never trust** client-sent `userId` / `tenantId` as authority |

### Default posture

**Authenticated by default.** Prefer a fallback authorization policy / `RequireAuthorization()` on the API group (or equivalent). Opt out with `[AllowAnonymous]` / `.AllowAnonymous()` only for an explicit allowlist: health/alive, public OpenAPI (if you expose it), login/callback.

Prefer **named policies** over scattered magic role strings. Missing auth on a new endpoint is a defect, not a follow-up.

### Current user in Application

Application reads the caller via an **`ICurrentUser`** (or equivalent) **port**. Infrastructure binds it from `HttpContext.User` / claims.

- Don’t inject `IHttpContextAccessor` into Application
- Don’t accept “acting as” user/tenant ids from the request body as authority — use the port + ownership check

## CORS

| Environment | Rule |
|-------------|------|
| **Development / non-prod** | Loose OK (`AllowAnyOrigin` when you don’t need credentials) so local frontends work |
| **Production** | **Explicit origin allowlist** from config. Never `AllowAnyOrigin` **with** `AllowCredentials`. Credentials only when a browser app truly needs cookies |

Don’t leave prod CORS as “whatever we used locally.”

## Transport and data protection

- HTTPS outside local Development; HSTS when appropriate for the host
- ASP.NET **Data Protection** for protected cookies / time-limited payloads when you need them
- Connection strings and API keys only via options/secret store (**`configuration`**)

## Input at trust boundaries

- Bind **request DTOs**; map manually into domain — no binding client JSON straight onto entities (mass assignment)
- File uploads → size, content-type, and storage rules in **`file-storage`**
- Validation at the boundary → **`validation`**; don’t rely on “the client wouldn’t send that”

### SSRF / “fetch this URL”

**Don’t build** features where the server fetches a **user-supplied** URL (import avatar by link, open proxy, scrape-this) unless the product explicitly requires it.

When required: **hard allowlist** of hosts/schemes (`https` only), block link-local / private / cloud metadata ranges, and don’t follow redirects off the allowlist. Soft “block private IPs only, any public URL OK” is not the default.

## Failure modes (agent traps)

| Temptation | Why it hurts | Do instead |
|------------|--------------|------------|
| Skip audience / authority validation | Wrong client’s tokens accepted | Full JWT validation set |
| New endpoint without auth | Data leak by default | Authenticated-by-default + explicit anonymous |
| `request.UserId` from body | Privilege escalation | `ICurrentUser` + ownership on loaded entity |
| `AllowAnyOrigin` + credentials | Invalid / wide-open browser API | Prod origin allowlist |
| Cookie auth, no antiforgery | CSRF on mutations | SameSite **and** antiforgery |
| Server fetches arbitrary user URLs | SSRF into VPC/metadata | Don’t build; else allowlist |
| Disable HTTPS / cert checks “for local” in shared code | Lands in prod | Dev-only overrides, never in shared libs |

## Don't

- Don’t trust client-sent roles, tenant ids, or “isAdmin” flags
- Don’t put secrets in source, logs, health JSON, or span attributes
- Don’t disable HTTPS / cert validation in shared code paths
- Don’t leave new endpoints anonymous by accident
- Don’t treat the API gateway as the only security layer
- Don’t use `IHttpContextAccessor` in Application
- Don’t invent open URL-fetch helpers

## References

- [`references/examples.md`](references/examples.md) — JWT, fallback policy, `ICurrentUser`, CORS, cookie+antiforgery, ownership

## Related

- Handler ownership checks → **`application-layer`**
- Secret loading → **`configuration`**
- PII in telemetry → **`observability`**
- Uploads → **`file-storage`**
- PR security pass → **`security-check`**

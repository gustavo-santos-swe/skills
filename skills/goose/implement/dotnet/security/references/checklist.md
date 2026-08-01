| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| JWT validation checks authority, audience, lifetime, and signing keys — don't ship "lifetime + signature only" or disable validation in Development as a shared default | verify | AuthN — JWT validation |
| A tampered/forged JWT (bad signature, wrong issuer, expired) must be rejected | regression-test | AuthN — JWT validation |
| Cookie-session hosts use SameSite (Lax/Strict) and antiforgery on mutating endpoints; JWT Bearer APIs skip the antiforgery dance | verify | AuthN — Cookies + CSRF |
| Authenticated by default; opt out with `[AllowAnonymous]` only for an explicit allowlist (health/alive, public OpenAPI, login/callback) | verify | AuthZ — Default posture |
| Every mapped endpoint requires auth unless on the explicit anonymous allowlist | regression-test | AuthZ — Default posture |
| Application reads the caller via an `ICurrentUser` port; don't inject `IHttpContextAccessor` into Application | architecture-test | AuthZ — Current user in Application; `ApplicationPurityTests.Application_ShouldNotHaveDependencyOn_AspNetCoreHttp` |
| Server never trusts a client-sent `userId`/`tenantId` as authority — handler loads the entity and checks ownership | verify | AuthZ — Current user in Application |
| Production CORS uses an explicit origin allowlist and never combines `AllowAnyOrigin` with `AllowCredentials` | regression-test | CORS |
| HTTPS outside local Development; use ASP.NET Data Protection for protected cookies / time-limited payloads when needed | verify | Transport and data protection |
| Bind request DTOs and map manually into domain — no binding client JSON straight onto entities (mass assignment) | verify | Input at trust boundaries |
| Don't build features where the server fetches a user-supplied URL unless required; when required, hard-allowlist hosts/schemes and block private/link-local/metadata ranges | verify | SSRF |
| Don't trust client-sent roles, tenant ids, or `isAdmin` flags | verify | Don't |
| Don't put secrets in source, logs, health JSON, or span attributes | verify | Don't |
| Don't disable HTTPS / cert validation in shared code paths | verify | Don't |

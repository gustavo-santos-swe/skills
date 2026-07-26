---
name: endpoint-conventions
description: Use when designing or reviewing ASP.NET HTTP endpoints — Minimal APIs/controllers, routes, QUERY, pagination, statuses, OpenAPI — or when implement loads the dotnet pack for API surface work.
disable-model-invocation: true
metadata:
  area: wip
---

# Endpoint Conventions

Goose handbook for the HTTP edge of .NET backends. Greenfield defaults below. **Target repo wins** if the host already standardized on controllers, unversioned routes, etc.

Voice: **`write-like-goose`**.

## When to use

- Adding or changing HTTP endpoints
- Choosing verbs, pagination, or status codes
- **`implement`** loading this pack

## Style

**Before writing:** detect the host’s existing style (`ControllerBase` / `[ApiController]` vs `MapGet`/`MapPost`). Match it.

**Greenfield:** Minimal APIs + `MapGroup`. Thin endpoints only — bind, authorize at the edge, call `I…RequestHandler`, map the Result.

**Existing controller hosts:** keep controllers; don’t mix Minimal APIs and controllers in the same host without a migration plan.

Endpoint code does **not** own business rules (see **`application-layer`**). Coarse authn/authz on the endpoint; resource checks in the handler.

**Never** bind or return EF entities / domain graphs on the wire — Application **Request/Response** DTOs only (**`serialization`**, **`application-layer`**). Timestamps on those DTOs follow **`time-and-ids`** / **`serialization`** (NodaTime Instant/LocalDate) — not a blanket `DateTimeOffset` mandate from generic Web API guides.

## Routes and verbs

- Prefix: **`/api/v1/...`** from day one for client-facing APIs. Breaking changes → `/api/v2/...` (sunset/deprecation → **`api-contracts`**).
- Resources: **plural kebab** (`/credit-cards`, `/checking-accounts`).
- Item: `/{id}` with a typed constraint when useful (`{id:guid}`).
- Verbs: `GET` read, `POST` create, `PUT` full replace, `PATCH` partial update, `DELETE` remove.
- When REST is a lie, use an explicit subpath (`…/settle`) rather than overloading `POST` on the collection without a name.

### QUERY (RFC 10008)

Safe, idempotent, **body allowed** — for list/search/filter payloads that don’t belong in a query string.

- **Greenfield default** for body-bearing list/search: **`QUERY`** (not `POST …/search`).
- Simple lists with a few filters: `GET` + query string is fine.
- Document gateway/WAF/OpenAPI caveats; add a dual `POST` only when a required client cannot speak QUERY.
- Map with `HttpMethods.Query` / `MapMethods` (or current ASP.NET helpers).

## Pagination

Never return unbounded collections. Cap `limit` / `pageSize` hard (pick a product max, e.g. 100).

| Mode | When | Inputs | Output extras |
|------|------|--------|----------------|
| **Cursor (default)** | Feeds, mobile, large tables | `cursor`, `limit` | `nextCursor` (optional `prevCursor`) |
| **Offset** | Admin grids / “page N of M” | `page` or `offset`, `pageSize` | `page`, `pageSize`, optional `totalCount` |

**Same endpoint may support both** if modes are mutually exclusive:

- Infer: `cursor` present → cursor; `page`/`offset` present → offset; neither → cursor default
- Reject `cursor` + `page` together → `ValidationFailed` / 422
- Same documented sort key for both modes
- `totalCount` opt-in (expensive) — don’t compute on every cursor page

Envelope sketch: `items` + mode-specific fields (see [references](references/examples.md)).

Fat filters/sort for lists prefer **QUERY** body; simple cursor params may live on `GET`.

## Success and errors

Shared Result → HTTP mapper (**`error-handling`**):

| Outcome | Status |
|---------|--------|
| Read / update with body | **200** |
| Create | **201** + `Location` when there is a resource URL |
| Success, no body | **204** |
| Validation | **422** Problem Details |
| Not found / forbidden / conflict | 404 / 403 / 409 Problem Details |

No `{ success, data, error }` envelope that fights Problem Details.

## Binding and validation

- Bind route/query/body into the Application **Request** DTO (or map into it in one line).
- FluentValidation runs in the **handler** (application-layer). Keep endpoint binding failures as 400; business/input rules as 422 via the handler.

## OpenAPI

Treat OpenAPI as a **first-class public contract** for `/api/v1`:

- Generate with **`Microsoft.AspNetCore.OpenApi`** (`AddOpenApi` / `MapOpenApi`) — not Swashbuckle as the greenfield default
- Interactive docs: **[Scalar](https://scalar.com/)** via `Scalar.AspNetCore` (`MapScalarApiReference`). **Do not** ship Swagger UI for new APIs
- Configure Scalar with a clear title, theme, and default HTTP client (see [references](references/examples.md)); serve at `/scalar` in Development (and anywhere else you intentionally expose the reference)
- Document auth, pagination envelopes, success types, Problem Details error responses
- Prefer OpenAPI **3.2** when documenting QUERY cleanly
- XML `<summary>` on public request/response DTOs is fine when the host already feeds comments into OpenAPI — optional, not a new tax on every type
- Versioning, deprecation, client impact → **`api-contracts`**

Optional: `.http` files next to the API for manual smoke — useful, not a substitute for Integration tests (**`testing`**).

## Failure modes (agent traps)

| Temptation | Why it hurts | Do instead |
|------------|--------------|------------|
| Mix controllers + Minimal APIs | Two styles in one host | Match existing; migrate deliberately |
| Return EF entity from endpoint | Cycles, over-post, leaks | Map to Response DTO |
| `DateTime` / wrong clock type on wire | Ambiguous TZ | Instant / LocalDate per **`serialization`** |
| Swagger UI on greenfield | Wrong docs stack | Scalar + `Microsoft.AspNetCore.OpenApi` |

## Don't

- Don’t put domain rules only in endpoint filters
- Don’t leak unmapped exceptions as opaque 500s without the host pipeline
- Don’t ship unbounded list endpoints
- Don’t use `POST …/search` for new greenfield body searches when QUERY is available
- Don’t invent a second success envelope beside Problem Details
- Don’t add Swagger UI / Swashbuckle UI on greenfield hosts — use Scalar
- Don’t expose domain/EF types as request or response bodies

## References

- [`references/examples.md`](references/examples.md) — MapGroup, QUERY, pagination envelope

## Related

- Handlers / authz split → **`application-layer`**
- Failure mapping → **`error-handling`**
- Contract evolution → **`api-contracts`**
- Cancellation on endpoints → **`async`**
- Wire JSON shape → **`serialization`**
- Generic Web API how-to (plugin) → Cursor **`dotnet-aspnetcore`** / `dotnet-webapi` — **override** their DateTimeOffset/sealed-record defaults with this pack

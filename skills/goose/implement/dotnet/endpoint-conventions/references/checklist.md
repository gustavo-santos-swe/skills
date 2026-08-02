| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| Detect and match the host's existing style (`ControllerBase`/`[ApiController]` vs Minimal APIs) before writing new endpoints | verify | Style |
| Greenfield endpoints are thin: bind, authorize at the edge, call `I…RequestHandler`, map the Result — no business rules in endpoint code | verify | Style |
| Never bind or return EF entities / domain graphs on the wire — Application Request/Response DTOs only | verify | Style — see `application-layer`'s `HandlerContractTests` for the handler-side half of this rule |
| Client-facing routes are prefixed `/api/v1/...`; resources are plural-kebab | verify | Routes and verbs |
| Body-bearing list/search endpoints default to `QUERY` (RFC 10008), not `POST .../search`, on greenfield | verify | QUERY |
| Never return unbounded collections — cap `limit`/`pageSize` hard | verify | Pagination |
| Pagination mode (cursor default vs offset) fits the resource's access pattern | verify | Pagination — product/UX judgment about the resource, not a structural property |
| No `{ success, data, error }` envelope that fights Problem Details | verify | Success and errors |
| OpenAPI generated with `Microsoft.AspNetCore.OpenApi`; interactive docs via Scalar, not Swagger UI, on greenfield | verify | OpenAPI |
| Don't leak unmapped exceptions as opaque 500s without going through the host pipeline | verify | Don't |
| Don't ship unbounded list endpoints | verify | Don't |
| Don't expose domain/EF types as request or response bodies | verify | Don't |

| Rule (one line, imperative) | Enforcement | Source |
|-------------------------------|--------------|--------|
| A given field/endpoint change is classified breaking vs additive before shipping | verify | What counts as breaking — requires understanding client behavior and semantics, not just a diff |
| Removing/renaming a field, changing its type or meaning, optional→required, or removing an endpoint is breaking for unknown consumers | verify | What counts as breaking |
| New optional response fields, new endpoints, and new optional request fields are additive and usually OK in place | verify | What counts as breaking |
| Enum members are additive only if clients tolerate unknown values — document that explicitly | verify | What counts as breaking |
| Breaking changes for public/external/unknown clients ship on a new `/api/vN+1` with a sunset plan for the old version | verify | Versioning practice |
| Deprecated shapes stay available for a documented overlap window before removal — no silent deletes on a public contract | verify | Deprecation / removal |
| When the public surface changes: OpenAPI is updated, breaking-vs-additive is called out, and no public endpoint ships undocumented | verify | OpenAPI review checklist |
| Don't open a new `/v2` when a lockstep in-place change (all Goose-owned clients updated together) would do | verify | Don't |
| Don't leave deprecated fields forever "just in case" | verify | Don't |

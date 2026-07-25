---
name: api-contracts
description: Use when reviewing public API compatibility, OpenAPI drift, deprecation, or whether a change needs a new /api/vN — or when implement loads the dotnet pack for contract work.
disable-model-invocation: true
metadata:
  area: wip
---

# API Contracts

Goose handbook for **compatibility** of HTTP APIs. Routes, verbs, status codes, OpenAPI wiring → **`endpoint-conventions`**. Wire JSON shape → **`serialization`**.

**Target repo wins** if versioning or client ownership is already settled.

Voice: **`write-like-goose`**.

## When to use

- PR touches request/response fields, status/error semantics, or OpenAPI
- Deciding additive vs breaking vs new major version
- **`implement`** loading this pack

## Ownership split

| Concern | Skill |
|---------|--------|
| `/api/v1` paths, QUERY, pagination, Problem Details, Scalar | **`endpoint-conventions`** |
| Breaking vs additive; deprecation; OpenAPI review checklist | **this skill** |
| camelCase, enums, Instant on the wire | **`serialization`** |

Don’t duplicate the endpoints handbook here.

## Versioning practice

URL versions stay **`/api/vN`** (already frozen).

| Who consumes the API | Practice |
|----------------------|----------|
| **Goose owns all clients** (API + web + mobile in lockstep) | Prefer **coordinated in-place** change in the same release train. Don’t cut `/v2` for ceremony. |
| **Public / external / unknown clients** | Additive changes in current `vN`. Real breaks → `/api/vN+1` + sunset. |

Still start greenfield at **`/api/v1`** so a future public cut has a place to go.

## What counts as breaking

Treat as breaking for unknown consumers:

- Remove or rename a field; change type or **meaning** while keeping the name
- Optional → required request field
- Change success/error status or error `code` semantics clients branch on
- Remove an endpoint or required query/header

**Additive (usually OK in place):** new optional response fields, new endpoints, new optional request fields.

**Enum members:** additive only if clients tolerate unknown values — document that. Otherwise treat new members carefully (or ship client updates in lockstep).

Don’t break field meaning while keeping the same name.

## Deprecation / removal

**Default:** document the change (OpenAPI description + changelog/PR); keep the old shape for an **overlap window**, then remove.

**Lockstep exception:** if the same release updates every Goose-owned client, **B** is OK — delete/rename in that release without a long dual-API window. Say so explicitly in the PR.

No eternal dual APIs. No silent deletes on a public contract.

## OpenAPI review (PR checklist)

When the public surface changes:

- [ ] OpenAPI updated (or regenerated) with the change
- [ ] Documented statuses/error cases match **`error-handling`**
- [ ] No undocumented public endpoint
- [ ] Breaking vs additive called out; version cut or lockstep client plan if breaking
- [ ] QUERY / pagination / auth schemes still accurate

OpenAPI remains a **first-class contract** — details in **`endpoint-conventions`**.

## Don't

- Don’t ship undocumented public endpoints
- Don’t change meaning of an existing field “because we own the mobile app” without updating those clients in the same effort
- Don’t open `/v2` when a lockstep in-place change would do
- Don’t leave deprecated fields forever “just in case”

## References

- [`references/examples.md`](references/examples.md) — breaking vs additive examples

## Related

- HTTP surface → **`endpoint-conventions`**
- JSON defaults → **`serialization`**
- Schema evolution → **`migrations-and-compat`**

---
name: validation
description: Use when defining or reviewing request/domain validation in .NET — FluentValidation placement, boundary vs invariants, uniqueness — or when implement loads the dotnet pack for validation work.
disable-model-invocation: true
metadata:
  area: wip
---

# Validation

Goose handbook for input validation vs domain invariants. Aligns with **`application-layer`** (validate in handler) and **`error-handling`** (`ValidationFailed` → **422**).

**Target repo wins** if validation is already standardized.

Voice: **`write-like-goose`**.

## When to use

- Request/command rules, cross-field checks, uniqueness UX
- Debating validator vs domain method
- **`implement`** loading this pack

## Layers

| Layer | Owns |
|-------|------|
| **FluentValidation** (Application request) | Required fields, formats, ranges, enums, cross-field rules on the DTO, “shape” of the use case |
| **Domain** (VO `Create`, entity methods) | Real invariants that must hold for every entry point (HTTP, jobs, imports) |
| **DataAnnotations** | **Options** startup validation (`ValidateOnStart`) — not the main request pipeline |

Don’t treat the HTTP validator as the only guard. Don’t duplicate the same invariant in three places without a reason — boundary checks format; domain enforces meaning.

## Timing and placement

- Colocate `XRequestValidator` with the use case (see **`application-layer`**)
- Run validation **first** in the handler; on failure → `ValidationFailed` → **422** Problem Details
- Prefer **sync, cheap** rules in FluentValidation (no DB by default)

## Uniqueness and I/O

“Already exists” / uniqueness:

1. Optional friendly check in the **handler** (port/query) → prefer **`Conflict`** (409)
2. **Always** enforce with a DB unique constraint (race-safe)
3. Translate unique violations → `Conflict` per **`error-handling`** / **`db-integration`**

Don’t put `MustAsync` DB calls in every validator by default. Async FluentValidation is an exception for UX-heavy forms, not the handbook baseline.

## Messages

- Field-keyed errors in `ValidationFailed` (`email` → messages[]) for client forms
- Stable **error codes** on the failure case where useful (`Customers.EmailTaken` on Conflict)
- User-facing wording in the message; no secrets/stack traces
- Localization of messages → **`localization`** when the product needs it — English strings are fine until then

## Cross-field rules

Live in FluentValidation (`Must` / `When` on the request). Example: `EndDate >= StartDate`, “either A or B required.”

If the rule is a lasting business invariant (not just request shape), also enforce it on the domain type.

## Security

Validation is not authorization. Authz stays host + handler resource checks (**`application-layer`** / **`security`**). Never trust “the client sent a valid-looking id” as ownership proof.

## Don't

- Don’t rely on FluentValidation alone for domain invariants
- Don’t use DataAnnotations as the primary request validation stack
- Don’t skip DB uniqueness because the handler checked once
- Don’t return 500 for expected validation/conflict outcomes
- Don’t use validation messages as a substitute for authz failures

## References

- [`references/examples.md`](references/examples.md) — validator + handler Conflict sketch

## Related

- Handler flow → **`application-layer`**
- HTTP mapping → **`error-handling`** / **`endpoint-conventions`**
- VO/entity invariants → **`domain-modeling`**
- Options validation → **`dependency-injection`** / **`configuration`**

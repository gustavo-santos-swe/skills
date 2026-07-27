---
name: application-layer
description: Use when writing or reviewing .NET use cases/handlers, DTOs, validation placement, or orchestration — or when implement loads the dotnet pack for Application code.
disable-model-invocation: true
metadata:
  area: goose
---

# Application Layer

Goose handbook for use cases: handlers, DTOs, validation, orchestration. Calibrated against Monetis; dependency rule elevated where noted.

**Target repo wins:** if the project already wires handlers a certain way, follow it unless the user asks to migrate.

Voice: **`write-like-goose`**.

## When to use

- Adding or changing a use case
- Reviewing Application PR shape (files, deps, mapping)
- **`implement`** loading this pack

## Shape of a use case

**One use case = one file** under the feature folder (see **`solution-structure`**). Colocate:

| Type | Example |
|------|---------|
| Request | `CreateCustomerRequest` |
| Response | `CreateCustomerResponse` |
| Validator | `CreateCustomerRequestValidator` |
| Handler interface + impl | `ICreateCustomerRequestHandler`, `CreateCustomerRequestHandler` |

Same pattern for reads (`GetCustomerRequest`, …). No MediatR by default — **explicit handler interfaces**, registered in DI, called from the endpoint.

Don’t bucket by type (`Handlers/`, `Commands/`). Don’t split Request/Handler across files unless a file is already huge.

## DTOs and mapping

- Requests/responses are Application DTOs — **not** domain entities over the wire
- **Manual** mapping in the handler (or small private helpers in the same file)
- **Never** return tracked EF entities from a handler
- **Per-use-case** request/response types — don’t share “read models” across GET/LIST just to DRY; drift is worse than a few duplicated fields

## Validation

**FluentValidation inside the handler** (validator colocated in the same file). Run first; on failure return `ValidationFailed` → **422** (see **`error-handling`**).

Host-level model binding checks stay thin; business/input rules for the use case live with the use case.

## What the handler may call

**Greenfield / ports-only:** repositories, UoW, gateways, clock, current user — via **ports** (Application or Domain). No raw `HttpClient`, no Infrastructure project references.

**Target already injects `DbContext` (no repos):** follow that. Don’t introduce a repository layer just to match the handbook. Prefer ports for **new** edges (email, payments, external APIs) even in those repos.

Align with **`solution-structure`** (Application → Domain + ports).

## Transactions

The **handler owns the write boundary**: one use case ≈ one commit unless the use case explicitly documents otherwise.

How EF starts/commits transactions → **`db-integration`**. Application skill only requires: don’t leave half-applied writes across a single use case.

## Authz and other cross-cutting

No MediatR pipeline behaviors.

| Layer | Owns |
|-------|------|
| **Host** | Authentication + coarse authorization (roles/policies on the endpoint) |
| **Handler** | Resource / ownership checks (“can *this* user mutate *this* aggregate?”) |

Logging/metrics via injected abstractions when needed — call them explicitly; don’t invent a handler decorator framework unless the repo already has one.

## Idempotency

Prefer **natural uniqueness**: unique constraints, client-supplied ids, “already exists” → `Conflict` / domain refusal.

There is **no** default idempotency-key store in this handbook. When a command can be **retried or double-submitted** in a way that hurts (payments, transfers, webhook side effects), **stop and design** for that use case — key, natural key, or messaging/outbox. Don’t bolt a generic store onto every write.

## Handler flow (typical command)

1. Validate request → `ValidationFailed` or continue
2. Authz / ownership check → `Forbidden` or continue
3. Load aggregate(s) via port (or DbContext if that’s the repo’s pattern)
4. Domain mutators / VO parse (Result/union per **`domain-modeling`**)
5. Persist; commit the use-case boundary
6. Map to response DTO; return `Ok`

Dispatch domain events **after** successful save (domain-modeling).

## Don't

- Don’t use MediatR (or equivalent) unless the target repo already standardized on it
- Don’t return tracked entities or leak Infrastructure types in response DTOs
- Don’t put SQL or `HttpClient` calls in Domain
- Don’t skip resource checks because the endpoint has a role
- Don’t add shared GET/LIST DTOs “to avoid duplication” without an explicit product reason
- Don’t add a global idempotency middleware by default

## References

- [`references/examples.md`](references/examples.md) — file sketch + handler outline

## Related

- Feature folders / ports → **`solution-structure`**
- Aggregates / events → **`domain-modeling`**
- Unions / HTTP mapping → **`error-handling`**
- EF / transactions → **`db-integration`**
- Endpoint wiring → **`endpoint-conventions`**

---
name: error-handling
description: Use when defining or changing how .NET APIs express failures — unions/Result, error cases, HTTP mapping, exceptions vs expected outcomes.
disable-model-invocation: true
metadata:
  area: goose
---

# Error Handling

Goose handbook for expected failures vs faults in .NET backends.

**Target repo wins:** if the project already has a Result/error/HTTP pattern, **follow it**. Defaults below are for **greenfield** or when the user asks to migrate.

Voice: **`write-like-goose`**.

## When to use

- Adding failure cases, mapping to HTTP, or reviewing error style in a PR
- Choosing exceptions vs typed outcomes
- **`implement`** loading this pack

## Core model

### New projects (.NET 11 / C# 15+)

Express success \| failure with a language **`union`**. Prefer exhaustive `switch` at the host edge.

Typed **failure cases** (not a single bag-of-codes `Error` enum as the only case):

```csharp
public sealed record Ok<T>(T Value);
public sealed record NotFound(string Code, string Message);
public sealed record ValidationFailed(string Code, IReadOnlyDictionary<string, string[]> Errors);
public sealed record Forbidden(string Code, string Message);
public sealed record Conflict(string Code, string Message);

public union Result<T>(Ok<T>, NotFound, ValidationFailed, Forbidden, Conflict);
```

Add feature-specific cases only when a core case isn’t enough (e.g. `PaywallBlocked`). See [Catalogs](#catalogs).

### Existing projects

Classic `Result<T>` / `Error` + `ErrorType` (Monetis-style) is fine. Don’t reinvent mid-feature. Migrate deliberately.

### Exceptions

**Throw** for bugs and unexpected faults (invariant broken, programming error, unrecoverable infra).

**Do not throw** for outcomes the API should return as a stable client error (not found, validation, forbidden, conflict). Those are union cases → 4xx.

## Catalogs

| Where | What |
|-------|------|
| Shared (Domain or Application common) | Core cases: `NotFound`, `ValidationFailed`, `Forbidden`, `Conflict`, … |
| Feature folder | Extra cases used only there; promote to shared at the second consumer |

Avoid one giant `Errors.cs` per feature full of duplicate `NotFound` / `ValidationFailed` factories. Prefer constructors on the shared cases + stable **string codes** (`CreditCards.NotFound`).

One-off messages used in a single handler may live next to that handler; promote on reuse.

## HTTP mapping

One host-level mapper (minimal APIs / controller helper). Prefer **Problem Details** (`application/problem+json`) when the stack makes it easy.

| Case | Status |
|------|--------|
| `ValidationFailed` | **422** |
| `NotFound` | 404 |
| `Forbidden` | 403 |
| `Conflict` | 409 |
| Unhandled exception / unknown | 500 |

Body includes stable `code` + human message (+ validation dictionary for 422). No stack traces to clients.

Per-endpoint status invention is a smell — extend the shared mapper instead.

## Infrastructure failures

- **Known, user-visible:** unique constraint / concurrency → translate to `Conflict` (or `ValidationFailed` when it’s clearly input). Return the union case.
- **Unknown / outage:** don’t swallow in the use case; let it bubble → 500 + log.
- **Transient retries:** **`resilience`**, not ad-hoc catch in every handler.

## Logging

| Outcome | Log |
|---------|-----|
| Expected union failure (4xx) | Don’t log at Error (Debug/none is enough) |
| Unhandled / 500 | Error + exception; include trace/correlation id |
| Messages | No secrets, tokens, or raw PII |

Metrics for failure kinds → **`observability`** when you add them.

## Consistency

- One unhandled-exception pipeline at the host
- No catch-all that turns bugs into empty 200/400
- Same codes in OpenAPI / clients when you document errors (`api-contracts`)

## Don't

- Don’t return 500 for expected business failures
- Don’t expose internals or stacks to clients
- Don’t introduce unions into a repo that already standardized on Result without an explicit migrate ask
- Don’t add a new failure case type for every feature when `NotFound` + a code suffices
- Don’t log every 404 at Error level

## References

- [`references/examples.md`](references/examples.md) — union shape + mapping sketch

## Related

- Input validation pipeline → **`validation`**
- Endpoint style → **`endpoint-conventions`**
- Retries / timeouts → **`resilience`**
- Structured logs / traces → **`observability`**

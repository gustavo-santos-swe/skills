---
name: serialization
description: Use when configuring or reviewing .NET JSON wire format — System.Text.Json, enums, dates, DTOs vs entities — or when implement loads the dotnet pack for serialization work.
disable-model-invocation: true
metadata:
  area: goose
---

# Serialization

Goose handbook for JSON (and related) wire format in .NET APIs.

**Target repo wins** if serializer settings are already settled.

Voice: **`write-like-goose`**.

Public contract stability / versioning → **`api-contracts`**. This skill is **how we shape JSON**.

## When to use

- Host JSON options, DTO shape, enum/date formats
- Choosing converters or rejecting Newtonsoft for new APIs
- **`implement`** loading this pack

## Defaults (greenfield)

| Setting | Choice |
|---------|--------|
| Library | **System.Text.Json** for HTTP APIs |
| Names | **camelCase** |
| Enums | **strings** (`JsonStringEnumConverter`) |
| Newtonsoft | Only when a library forces it (e.g. Hangfire) — not for new API contracts |

Configure once at the host (Minimal API / controllers JSON options). Don’t invent per-endpoint serializer settings without a reason.

## What to serialize

- **Request/response DTOs** only — never EF entities or graphs with navigation cycles
- Manual mapping in Application (**`application-layer`**)
- Don’t leak internal domain types onto the wire by accident

## Types

| Kind | Rule |
|------|------|
| Instant / timestamps | **NodaTime Instant** as ISO-8601 UTC on the wire (**`time-and-ids`**) |
| Calendar dates | **LocalDate** (date-only), not a midnight DateTime pretending to be a date |
| Money | **`decimal`** (+ currency code when multi-currency); never `double` for money |
| Polymorphism | Only when the contract needs it — explicit **discriminator**; document in OpenAPI |

Don’t silently change enum or date formats on a shipped public API — that’s a breaking change (**`api-contracts`** / **`migrations-and-compat`**).

## Don't

- Don’t use Newtonsoft for new ASP.NET JSON pipelines
- Don’t serialize domain/EF entities to clients
- Don’t use numeric enums on public APIs without an explicit migrate
- Don’t use `double` for money
- Don’t change camelCase / string-enum defaults mid-flight without a version story

## References

- [`references/examples.md`](references/examples.md) — host JSON options sketch

## Related

- Clocks / Instant → **`time-and-ids`**
- DTO mapping → **`application-layer`**
- OpenAPI / breaking changes → **`api-contracts`**

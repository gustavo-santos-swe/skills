---
name: time-and-ids
description: Use when writing or reviewing clocks, UTC/calendar time, NodaTime types, or ID generation in .NET — or when implement loads the dotnet pack for time/id code.
disable-model-invocation: true
metadata:
  area: wip
---

# Time and IDs

Goose handbook for “now”, calendar vs instant, and identifiers. Greenfield defaults below; Monetis today is mostly BCL `DateTime`/`DateOnly` + Guid v7 — **target wins** until you migrate.

Voice: **`write-like-goose`**.

## When to use

- New timestamps, “today”, scheduling, or entity IDs
- Freezing time in tests
- **`implement`** loading this pack

## Clock

Use **`TimeProvider`** wherever production code needs “now” in Domain or Application.

- Ban `DateTime.Now` / `DateTime.UtcNow` / `DateTimeOffset.Now` on those paths
- Register `TimeProvider.System` (or test fake) in DI
- Prefer passing an **`Instant`** (or `LocalDate`) into domain mutators when you want entities free of `TimeProvider`

Glue to NodaTime:

```csharp
var instant = Instant.FromDateTimeOffset(timeProvider.GetUtcNow());
var today = instant.InZone(userZone).Date; // when "today" is zone-dependent
```

Optional: wrap with NodaTime’s `IClock` in Infrastructure if a library API wants it — still backed by `TimeProvider` for tests.

## Time types (NodaTime)

| Meaning | Type |
|---------|------|
| Point on the timeline (created-at, event time) | **`Instant`** — treat as UTC |
| Calendar day (due date, statement period, “billing day”) | **`LocalDate`** |
| Time of day without a date | **`LocalTime`** when needed |
| Civil date-time in a zone (rare in core) | Convert at the edge; don’t persist ambiguous local timestamps as if they were UTC |

**Process and store instants in UTC.** Keep a user/tenant **`DateTimeZone`** (or zone id string) when the product needs “today for this user.” Convert for display / “local today” at API/UI (or a presentation mapper) — not deep in Domain as a default.

Wire/JSON and EF mapping for NodaTime → **`serialization`** / **`db-integration`** (System.Text.Json NodaTime converters; provider plugins). Don’t invent ad-hoc ISO helpers per feature.

Legacy repos on `DateTime`/`DateOnly`: follow them; new greenfield code uses NodaTime unless the user says otherwise.

## IDs

**Strongly typed IDs** on public domain APIs — see **`domain-modeling`**.

| Kind | Default |
|------|---------|
| Aggregate / entity identity | App-generated **`Guid` version 7** (`Guid.CreateVersion7()`), wrapped (`CustomerId`) |
| Human-facing numbers (invoice #, ticket #) | **DB sequence** (or equivalent) — not a random Guid shown to users |

Who creates the Guid: typically the aggregate/entity (or a tiny factory) **before** insert so the app can use the id immediately. Don’t wait on the database for v7 ids.

Sortability: v7 is enough for time-ordered ids without a separate column in most cases. Document collision assumptions: treat Guid as unique; don’t build “pretty” non-unique public ids without a uniqueness guarantee.

Serialization of typed ids (Guid string on the wire) → **`serialization`**. Column types → **`db-integration`**.

## Testing

- Prefer **`FakeTimeProvider`** (or advanceable test double) when behavior depends on time
- Convert faked UTC to `Instant` the same way production does
- Real Guid v7 in tests is fine; seed fixed ids only when asserting on identity or golden output
- Don’t require deterministic ids in every test

## Don't

- Don’t call `DateTime.Now` / `UtcNow` in Domain or Application production code
- Don’t store local wall time as if it were UTC
- Don’t mix `DateTime` Kind-unspecified with NodaTime `Instant` without an explicit conversion
- Don’t use Ulid/sequences as the default surrogate key unless the product asks
- Don’t show raw DB sequences as security tokens

## References

- [`references/examples.md`](references/examples.md) — clock glue, typed id, test fake

## Related

- Typed ids / VOs → **`domain-modeling`**
- Handlers getting “now” → **`application-layer`**
- EF columns / Npgsql NodaTime → **`db-integration`**
- JSON shape → **`serialization`**
- Locale display formatting — product/UI concern; not in this pack yet

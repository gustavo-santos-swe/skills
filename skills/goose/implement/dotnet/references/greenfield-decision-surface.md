# Greenfield decision surface (dotnet)

Load from **`brainstorm`** branch **`greenfield`** when **API / .NET** is an active pack. How-to stays in each skill; this file only forces **presence + short decisions**.

## How to grill

One concern per message (or one tightly coupled pair). Recommend + why; wait.

For each row below, status must be one of:

| Status | Meaning |
|--------|---------|
| **in** | In this cut. Ask the deepen question(s); lock answers in the freeze. |
| **out** | Not in this product (reason). |
| **later** | Skipped for this cut (POC/MVP). Reason + what unblocks it (ticket or milestone). |

**Never grill** what the pack already decides (code-style, async traps, serialization fine print, DI lifetimes as ritual). Skills apply those at **`implement`**.

**POC tip:** production concerns (rate limiting, rich health, full observability, messaging…) often start as **later**, not silent omit.

Deepen only when status is **in**. Point at the skill; do not paste the handbook.

## Concerns

Walk in order. Skip a row only after status is set.

### Always decide presence

| Concern | Skill | Default if **in** | Deepen when **in** (pick one path) |
|---------|-------|-------------------|--------------------------------------|
| Solution layout | [`solution-structure`](../solution-structure/) | Ports-only layers (Domain / Application / adapters) | Accept Goose layout, or name the override |
| Domain modeling | [`domain-modeling`](../domain-modeling/) | Rich domain where invariants live | Anemic vs rich for the first slice? |
| Application layer | [`application-layer`](../application-layer/) | Handlers + ports | Accept handlers/ports, or override |
| Time & IDs | [`time-and-ids`](../time-and-ids/) | NodaTime + Guid v7 (Goose greenfield) | Accept defaults, or name clock/ID choice |
| Data / schema | [`../../database/`](../../database/) + [`db-integration`](../db-integration/) | EF Core + explicit schema rules | DB engine; who owns migrations |
| HTTP edge | [`endpoint-conventions`](../endpoint-conventions/) | Minimal APIs + MapGroup | Accept Minimal APIs, or controllers |
| Errors | [`error-handling`](../error-handling/) | Union / Result → HTTP map | Accept Goose Result shape, or existing house type |
| Validation | [`validation`](../validation/) | FluentValidation at boundary | Accept, or other |
| AuthN/Z | [`security`](../security/) | Bearer JWT for API clients | Who authenticates; cookie session vs JWT; main policies |
| Config / secrets | [`configuration`](../configuration/) | appsettings + env; secrets not in git | Secret store for non-dev |
| API contracts | [`api-contracts`](../api-contracts/) | `/api/v1` + OpenAPI | Public vs private; versioning now? |
| Testing bar | [`testing`](../testing/) | TUnit + seam tests | What must be red/green on first slice |

### Often **later** on a POC

| Concern | Skill | Default if **in** | Deepen when **in** |
|---------|-------|-------------------|--------------------|
| Health / ready | [`health-and-readiness`](../health-and-readiness/) | `/alive` + `/health` | Detailed `/health` exposure; what dependencies |
| Observability | [`observability`](../observability/) | OTEL + MEL | Traces/metrics backend; PII rules |
| Rate limiting | [`rate-limiting`](../rate-limiting/) | ASP.NET rate limiter | Key (user/IP); 429 shape |
| Caching | [`caching`](../caching/) | HybridCache | What is cached first |
| Resilience (outbound) | [`resilience`](../resilience/) | Standard Http resilience | Which outbound calls need it |
| Outbound HTTP | [`http-clients`](../http-clients/) | Typed clients | First external dependency |
| Background work | [`background-work`](../background-work/) | Hangfire for jobs | Jobs vs in-process |
| Messaging | [`messaging`](../messaging/) | Outbox when integration events | Bus vs none this cut |
| File storage | [`file-storage`](../file-storage/) | Port + blob adapter | Upload types/size limits |
| Schema evolution ritual | [`migrations-and-compat`](../migrations-and-compat/) | Expand/contract when shipping schema | Needed on day one? |

### Do not ask (pack applies at implement)

`code-style`, `async`, `serialization` details, `dependency-injection` ritual — unless the user overrides a known Goose default.

## Freeze table (required)

Copy into **Established so far** (one row per concern walked):

| Concern | Status | Decision (if in) | Notes |
|---------|--------|------------------|-------|
| … | in / out / later | … | … |

No empty status. **later** needs a reason.

## Pack order

If Shape also picked Web/Mobile, finish this surface, then load that pack’s `greenfield-decision-surface.md` when it exists. Stub packs: mark platform rows **later** or “pack incomplete” and move on (do not invent SOTA).

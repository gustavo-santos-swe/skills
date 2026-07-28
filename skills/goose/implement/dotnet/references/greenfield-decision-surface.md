# Greenfield decision surface (dotnet)

Load from **`brainstorm`** branch **`greenfield`** when **API / .NET** is an active pack. How-to stays in each skill; this file only forces **presence + short decisions** for concerns that vary by cut.

## How to grill

One concern per message (or one tightly coupled pair). Recommend + why; wait.

For each row in **Decide presence** / **Often later**, status must be one of:

| Status | Meaning |
|--------|---------|
| **in** | In this cut. Ask the deepen question(s); lock answers in the freeze. |
| **out** | Not in this product (reason). |
| **later** | Skipped for this cut (POC/MVP). Reason + what unblocks it (ticket or milestone). |

**Never grill** pack-owned defaults (see below). Skills apply those at **`implement`**. Only reopen if the user overrides.

**POC tip:** production concerns (rate limiting, rich health, full observability, messaging…) often start as **later**, not silent omit.

Deepen only when status is **in**. Point at the skill; do not paste the handbook.

## Concerns

Walk in order. Skip a row only after status is set.

### Decide presence

| Concern | Skill | Default if **in** | Deepen when **in** |
|---------|-------|-------------------|--------------------|
| Data / schema | [`../../database/`](../../database/) + [`db-integration`](../db-integration/) | EF Core + explicit schema rules | DB engine; who owns migrations |
| AuthN/Z | [`security`](../security/) | Bearer JWT for API clients | Who authenticates; cookie session vs JWT; main policies |

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

Assumed **in** with Goose defaults unless the user overrides:

| Concern | Skill | Locked default |
|---------|-------|----------------|
| Solution layout | [`solution-structure`](../solution-structure/) | Ports-only layers |
| Domain modeling | [`domain-modeling`](../domain-modeling/) | Rich domain (invariants in the domain) |
| Application layer | [`application-layer`](../application-layer/) | Handlers + ports |
| Time & IDs | [`time-and-ids`](../time-and-ids/) | NodaTime + Guid v7 |
| HTTP edge | [`endpoint-conventions`](../endpoint-conventions/) | Minimal APIs + MapGroup |
| Errors | [`error-handling`](../error-handling/) | Union / Result → HTTP map |
| Validation | [`validation`](../validation/) | FluentValidation at boundary |
| Config / secrets | [`configuration`](../configuration/) | appsettings + env; secrets not in git |
| API contracts | [`api-contracts`](../api-contracts/) | `/api/v1` + OpenAPI |
| Testing | [`testing`](../testing/) | TUnit + seam tests |
| Code style | [`code-style`](../code-style/) | Pack conventions |
| Async | [`async`](../async/) | Pack traps / rules |
| Serialization details | [`serialization`](../serialization/) | Pack wire defaults |
| DI ritual | [`dependency-injection`](../dependency-injection/) | Pack lifetimes |

Do not put these in the freeze table unless overridden.

## Freeze table (required)

Copy into **Established so far** (one row per concern **walked**):

| Concern | Status | Decision (if in) | Notes |
|---------|--------|------------------|-------|
| … | in / out / later | … | … |

No empty status on walked rows. **later** needs a reason.

## Pack order

If Shape also picked Web/Mobile, finish this surface, then load that pack’s `greenfield-decision-surface.md` when it exists. Stub packs: mark platform rows **later** or “pack incomplete” and move on (do not invent SOTA).

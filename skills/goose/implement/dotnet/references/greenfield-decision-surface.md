# Greenfield decision surface (dotnet)

Load from **`brainstorm`** branch **`greenfield`** when **API / .NET** is an active pack. How-to stays in each skill; this file forces a **short** presence grill — not a tour of the whole pack.

## How to grill

One concern per message. Recommend + why; wait.

Status when you ask:

| Status | Meaning |
|--------|---------|
| **in** | In this cut. Ask the deepen question; lock in the freeze. |
| **out** | Not in this product (reason). |
| **later** | Skipped for this cut (POC/MVP). Reason + what unblocks it. |

**Never grill** pack-owned defaults (table at the bottom). Skills apply those at **`implement`**. Only reopen if the user overrides.

Deepen only when **in**. Point at the skill; do not paste the handbook.

### Order

1. **Core** — always ask (trust / data).
2. **Reminders** — always ask once, lightly (things people forget on a POC).
3. **Triggers** — ask only if Shape/Product already signaled the need.

Do not walk the full pack. Prefer **later** on reminders for a thin POC; the point is the engineer *chooses*, not that every concern ships day one.

---

## 1. Core (always)

| Concern | Skill | Default if **in** | Deepen when **in** |
|---------|-------|-------------------|--------------------|
| Data / schema | [`../../database/`](../../database/) + [`db-integration`](../db-integration/) | EF Core + explicit schema rules | DB engine; who owns migrations. If **in**, schema evolution follows [`migrations-and-compat`](../migrations-and-compat/) when you ship migrations — no separate row. |
| AuthN/Z | [`security`](../security/) | Bearer JWT for API clients | Auth this cut? Who authenticates; cookie session vs JWT if not a pure API client. |

---

## 2. Reminders (always, one pass)

Engineers often skip these until prod hurts. Ask **in / out / later** only — deepen only if **in**.

Recommend **later** on a thin POC unless they already care about deploy/abuse/ops.

| Concern | Skill | Default if **in** | Deepen when **in** |
|---------|-------|-------------------|--------------------|
| Health / ready | [`health-and-readiness`](../health-and-readiness/) | `/alive` + `/health` | Exposure of detailed `/health`; which dependencies |
| Observability | [`observability`](../observability/) | OTEL + MEL | Where traces/metrics go; PII rules |
| Rate limiting | [`rate-limiting`](../rate-limiting/) | ASP.NET rate limiter | Key (user/IP); public vs authenticated surface. Prefer **in** once the API has anonymous auth/search surfaces — cheap and often skipped until abuse. |

One breath each. Do not nest how-to.

---

## 3. Triggers (only if signaled)

Ask only when Shape or Product already mentioned the need (or an obvious synonym). If silent → treat as **later** without a question; note in freeze if useful.

| Signal in Shape/Product | Concern | Skill | Deepen when **in** |
|-------------------------|---------|-------|--------------------|
| Uploads, blobs, images, documents | File storage | [`file-storage`](../file-storage/) | Types/size limits; port + blob |
| Cron, queue worker, “background job”, Hangfire | Background work | [`background-work`](../background-work/) | Jobs vs in-process |
| Integration events, bus, “notify other service”, outbox | Messaging | [`messaging`](../messaging/) | Bus vs none; outbox |
| Call external HTTP API / third party | Outbound HTTP (+ resilience) | [`http-clients`](../http-clients/), [`resilience`](../resilience/) | Which dependency; timeouts/retries needed? |
| “Cache this”, hot read path, Redis | Caching | [`caching`](../caching/) | What is cached first |

No signal → no question.

---

## Freeze table (required)

One row per concern **asked** (Core + Reminders + any Triggers fired):

| Concern | Status | Decision (if in) | Notes |
|---------|--------|------------------|-------|
| … | in / out / later | … | … |

No empty status on asked rows. **later** needs a reason. Pack-owned defaults stay out of the table unless overridden.

---

## Do not ask (pack applies at implement)

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
| Testing (+ CI gates) | [`testing`](../testing/) | TUnit + Unit/Architecture/Integration/Mutation **PR CI gates** (see testing “Greenfield CI gates”) |
| Schema evolution ritual | [`migrations-and-compat`](../migrations-and-compat/) | Expand/contract when shipping schema (follows Data **in**) |
| Code style | [`code-style`](../code-style/) | Pack conventions |
| Async | [`async`](../async/) | Pack traps / rules |
| Serialization details | [`serialization`](../serialization/) | Pack wire defaults |
| DI ritual | [`dependency-injection`](../dependency-injection/) | Pack lifetimes |

---

## Pack order

If Shape also picked Web/Mobile, finish this surface, then load that pack’s `greenfield-decision-surface.md` when it exists. Stub packs: note “pack incomplete” and move on (do not invent SOTA).

---
name: security-check
description: Trust-boundary gate (or full audit): high-confidence findings, report only. Use when the change hits auth/secrets/PII/payments/uploads/public APIs, or when asked for a security pass.
disable-model-invocation: true
metadata:
  area: wip
---

# Security Check

Goose handbook for a **security pass**: default **gate** on the change, optional **full audit** when asked.

Voice: **`write-like-goose`**.

Stack **how** (AuthN recipes, CORS defaults, …) lives in pack skills. This skill owns **process, confidence, and the report**.

## When to use

**Gate (default)** - suggest or run when the diff/paths touch a trust boundary:

- Auth, sessions, tokens, cookies, CSRF
- Secrets, keys, connection strings
- PII, payments, tenancy / multi-tenant ids
- File upload/download, path construction
- Public HTTP APIs, webhooks, SSRF-prone outbound calls
- Crypto, deserialization of untrusted data

Also when the user asks for a security pass, or after a security-related review comment.

**Full audit** - only when the user asks for whole-repo / periodic / “full audit” / “OWASP everything”. Same confidence bar; wider surface.

## When not to

- Pure refactors, docs-only, copy-only (unless the user forces a run)
- Replacing pack handbooks (`implement/dotnet/security`, frontend/RN security when filled)
- Silent auto-fixes (this skill **reports**; fixes go through **implement** after the engineer asks)

## Modes

| Mode | Scope | Deliverable |
|------|--------|-------------|
| **Gate** | Branch diff, uncommitted change, or named paths/PR | Short report **in chat** |
| **Full audit** | Broader codebase (still timebox; prefer entrypoints + trust boundaries) | Markdown file (below) + chat summary |

Default = **gate**. Do not escalate to full audit unless asked.

## Hard rules

1. **Trace before flag.** Follow data flow. Confirm attacker-controlled input (or real misconfig) before reporting.
2. **High confidence only** for the main report. Medium → “needs verification.” Low / theory / pure defense-in-depth → omit (or one FYI line max).
3. **Report only.** No code changes unless the engineer explicitly asks to fix afterward.
4. **Never paste raw secrets** into chat or files - redact (`sk-…****`, env var **names** ok).
5. **Load pack security how** when the stack is known (see [Stack packs](#stack-packs)).

## Confidence

| Level | Criteria | Action |
|-------|----------|--------|
| **High** | Vulnerable pattern + attacker-controlled (or confirmed broken authz/secret) after research | **Report** with severity |
| **Medium** | Pattern present; input source or mitigation unclear | **Needs verification** |
| **Low** | Theoretical, best-practice-only, framework already mitigates | **Do not report** |

Research before flagging: other validation, middleware, framework defaults, whether the value is server-controlled config vs request data.

Do **not** flag solely on pattern match. Do **not** treat env/settings/constants as attacker input.

## Severity (report buckets)

| Bucket | Meaning |
|--------|---------|
| **Block** | Exploitable trust failure; must fix before ship |
| **Should-fix** | Real issue; ship judgment is the engineer’s |
| **FYI** | Narrow note; optional |
| **Needs verification** | Medium confidence only |

If nothing high-confidence: say explicitly **“No security blockers for this scope.”**

## Stack packs

When reviewing .NET / web / RN code, load the matching pack security skill for stack-specific tells (not the whole pack unless already loaded by **implement**):

| Stack | Skill |
|-------|--------|
| .NET | [`../implement/dotnet/security/SKILL.md`](../implement/dotnet/security/SKILL.md) |
| Frontend / Next | [`../implement/frontend/security/SKILL.md`](../implement/frontend/security/SKILL.md) (when filled) |
| React Native | pack security / auth skills when filled |

Process and confidence stay here. Pack wins on stack defaults when they conflict with generic advice.

## Steps

### Gate

1. **Scope** - diff vs base, uncommitted tree, or user-named paths. List trust boundaries in play.
2. **Heuristic** - if no trust-boundary touch and user didn’t force: say skip reason; stop.
3. **Load** - checklist ([`references/checklist.md`](references/checklist.md)) + relevant pack security skill(s).
4. **Hunt** - focus on changed code; research call sites / middleware as needed for confidence.
5. **Report** in chat using [`references/report-template.md`](references/report-template.md).
6. **Next** - blockers → back to **implement** (only if engineer wants fixes). Clean → **git-practices** / **pr-raise** (or **pr-iterate** if already in review).

### Full audit

1. Confirm the user wants full audit (not gate).
2. Map entrypoints and trust boundaries (timebox; don’t boil the ocean).
3. Same hunt + confidence rules; cover more surface using the checklist categories that apply.
4. Write `docs/security/YYYY-MM-DD-<slug>.md` (or the repo’s security-docs convention if one exists). Chat: short summary + path.
5. Same next-step routing as gate.

## Guardrails

1. **Report only** - code changes only if the engineer explicitly asks afterward.
2. **High confidence after tracing** - redact secrets; skip low/theater findings.
3. **Gate by default** - full audit only when asked; chat for gate, file for full audit (or on request).

**Done when:** scoped report delivered with an explicit verdict (blockers or “no blockers for this scope”).

## References

- [`references/checklist.md`](references/checklist.md) - trust-boundary hunt list
- [`references/report-template.md`](references/report-template.md) - report shape

## Related

- Build / fix → **implement**
- Ship → **git-practices** → **pr-raise**
- PR feedback loop → **pr-iterate**
- .NET security how → **implement/dotnet/security**

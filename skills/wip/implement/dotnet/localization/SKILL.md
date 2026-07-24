---
name: localization
description: Cultures, resource strings, and locale-aware formatting in .NET. Use when adding or changing IStringLocalizer, multi-language messages, or culture-dependent dates/numbers in ASP.NET.
disable-model-invocation: true
metadata:
  area: wip
---

# Localization

Status: **stub** — topic list below is what to define later. Keep SKILL.md short; deep samples → `references/`.

## When to use

- User-facing strings in more than one language; culture negotiation; locale-sensitive formatting.
- **`implement`** loading this pack when the change is i18n/l10n related.

## Topics to fill (checklist)

### Scope
- Which surfaces are localized (API messages, emails, UI if any)
- Default culture / fallback culture
- Monolingual repos: skill still documents “we don’t localize except X”

### Resources
- `.resx` vs other providers; naming and project placement
- `IStringLocalizer` / `IStringLocalizer<T>` conventions
- Missing key policy (throw vs key-as-string)

### Culture flow
- How culture is chosen (Accept-Language, claim, query) — and what we ignore
- Thread/async culture flow (`CultureInfo` on request)

### Formatting
- Dates/numbers/currency — format at the edge, store invariant/UTC (→ time-and-ids)
- Validation / ProblemDetails messages — localized or English-only?

### Domain vs boundary
- Domain errors as codes; localize only when mapping to the client (→ error-handling)

### Testing
- How we assert stable keys vs translated text

## Don't

- Don't localize log messages and telemetry (keep invariant for ops).
- Don't store culture-formatted strings as source of truth in the DB.
- Don't mix cultures in a single response without an explicit rule.

## References

Optional: `references/` for resource layout. Actual `.resx` files live in the target repo.

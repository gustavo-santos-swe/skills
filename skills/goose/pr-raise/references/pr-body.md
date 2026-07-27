# PR body — Goose default + repo templates

Voice: `write-like-goose`. Keep it short. Owned by **`pr-raise`**.

## Goose default (when the repo has no template)

```markdown
## Briefing

<1–3 sentences: what and why.>

## References

- <ticket URL or `#123`>
- <optional doc / ADR>

## Changes

- <bullet>
- <bullet>

<!-- UI: screenshots below if useful -->

## Notes

- <env / config / flags / migrations / rollout — or delete this section>
```

## When the repo has a PR template

1. Load it (discovery in **`pr-raise`**).
2. **Keep the template's headings** so repo bots / humans still see expected sections.
3. **Map Goose content into those headings** (don't discard required checklists):

| Goose intent | Often maps to template section |
|--------------|--------------------------------|
| Briefing | Summary / Description / Overview |
| References | Related issues / Linear / Ticket |
| Changes | Changes / What changed / Diff summary |
| Notes | Notes / Deploy / Checklist / Risk / Test plan extras |

4. If the template lacks a place for ops notes (env, flags, migrations), add a **`## Notes`** section at the end rather than stuffing them into unrelated checkboxes.
5. Fill required checkboxes honestly; leave unchecked what wasn't done — don't theater-check.

## Minimal filled example (Goose default)

```markdown
## Briefing

Adds PIX as a checkout method so BR users can pay without a card.

## References

- https://linear.app/…/ABC-42

## Changes

- New PIX path on checkout + webhook handler for payment confirmation
- Declines duplicate webhook deliveries with the existing idempotency key

## Notes

- Requires `Pix__MerchantId` in app settings (Staging + Prod)
- Flag `checkout.pix` defaults off; enable per environment after smoke
```

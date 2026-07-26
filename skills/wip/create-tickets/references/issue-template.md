# Issue / plan-slice template

Use for Linear/GitHub issues. When staying on the plan, use the same sections under each slice heading (checkboxes for AC).

## Title

Short, outcome-oriented. (`Guest cart end-to-end`, not `Wire CartService`)

## Parent

Epic / Feature (tracker ids or plan headings). Omit if flat under epic.

## What to build

End-to-end behaviour this slice makes work - from the user’s (or calling system’s) perspective. Not a layer-by-layer chore list.

## Acceptance criteria

- [ ] …
- [ ] …

Concrete and checkable. No “works correctly” / “as expected.”

## Blocked by

- … - or `None - can start immediately`

## Grounding

**Source of truth:** path/URL - or `open - frozen here:` (then paste the freeze)

**Implement checks:** how build proves alignment (test names/commands ok if stable; scenarios ok)

**Review checks:** what **pr-review** should re-read against the source of truth

**Drift:** if reality diverges, ask engineer: update source of truth | separate drift log + follow-up | addendum on existing doc

## Touch list (optional)

Only if requested at quiz time. Hints, not AC.

- …

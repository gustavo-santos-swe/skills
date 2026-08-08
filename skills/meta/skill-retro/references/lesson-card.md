# Lesson card

Fill one card per lesson (max 5 per retro). Keep each field short.

```text
Lesson:     <one line: the house rule in positive form>
Evidence:   <where it showed up: review note, failed approach, repeated ask>
Bad default:<what the agent did or would do without the rule>
Good move:  <what to do instead>
Owner guess:<skill path if known, or "unknown">
Disposition:<absorb | evolve | defer | drop>  (set after step 2)
```

## Examples

```text
Lesson:     Extend kit Button variants before adding page-local buttons
Evidence:   Review: "do not hardcode a second primary CTA"
Bad default:New styled <button> in the page
Good move:  Add or use a Button variant in components/ui
Owner guess:skills/goose/implement/frontend/styling
Disposition:absorb
```

```text
Lesson:     Missing DESIGN.md must stop UI token work
Evidence:   Agent invented CSS variables with no SoT
Bad default:Silent kit invention
Good move:  Ask user to add DESIGN.md (catalog OK)
Owner guess:skills/goose/implement/frontend/styling
Disposition:absorb
```

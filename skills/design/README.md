# design

Production-grade UI/UX, anti-slop visual design.

## In this repo

| Skill | Purpose |
|-------|---------|
| [`frontend-design`](frontend-design/) | Distinctive UI, anti-“AI slop” (vendored from Anthropic; see `metadata.upstream`) |

## Favorite upstream skills (install — do not vendor)

Goose frontend pack **assumes** Taste + Impeccable (+ vendored `frontend-design`) for craft. Structure and reuse live in [`../goose/implement/frontend/`](../goose/implement/frontend/).

Install commands and update flow live in the root [README](../../README.md#favorite-frontend--design-skills-install-upstream--do-not-vendor).

Quick install:

```bash
npx skills add leonxlnx/taste-skill --skill design-taste-frontend -g -y -a cursor
npx skills add pbakaus/impeccable --skill impeccable -g -y -a cursor
npx skills add emilkowalski/skills -g -y -a cursor --all
npx skills add https://uizze.com --skill anti-ui-slop -g -y -a cursor
```

Also vendored under mobile (aesthetic DB): [`ui-ux-pro-max`](../mobile/ui-ux-pro-max/).

DESIGN.md examples: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md).

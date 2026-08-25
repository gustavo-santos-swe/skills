---
name: web-styling
description: Use when styling Next.js UI (tokens, Tailwind, CVA variants, DESIGN.md, or reuse of shared primitives), or when implement loads the frontend pack for style work.
metadata:
  area: goose
---

# Styling

Goose defaults for Next.js styling and **reuse-first** UI. Visual craft stays upstream (Taste, Impeccable, `frontend-design`). This skill owns tokens, variants, and the reuse ladder.

**Target repo wins:** if the project already has a clear kit and token path, follow it unless the user asks to migrate.

Voice: **`write-like-goose`**. Target-repo `AGENTS.md` may override paths and names.

## When to use

- New or changed product UI, tokens, themes, or shared controls
- Temptation to add a one-off styled control
- **`implement`** loading this pack

## When not to

- Brand direction, LP taste, or polish critique → Taste / Impeccable / `frontend-design`
- Folder ownership alone → **`project-structure`**
- Contrast / a11y depth → **`accessibility`**

## Before you style

1. Locate `DESIGN.md` at the repo root (or the path `AGENTS.md` names as the design SoT).
2. If it is missing, **stop**. Ask the user to add or choose one. Point at [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) or Impeccable init. Do not invent a full kit in silence.
3. If it exists, treat it as SoT for tokens and component roles. Do not invent a parallel palette.

**Done when (gate):** `DESIGN.md` (or named SoT) is present, or the user explicitly deferred and said how to proceed.

## Reuse ladder

Walk in order. Stop at the first step that fits.

1. **Scan the kit**: shared primitives under the path from **`project-structure`** (often `components/ui`).
2. **Use an existing variant or prop** when the role already exists (primary button, ghost, size).
3. **Extend the primitive** with a named variant or prop when the role is new but the control is the same.
4. **Add a kit primitive** when no shared control fits and the role will repeat. Put it in the shared kit, not the feature folder.
5. **Feature-only markup** only for layout glue that is not a reusable control (page sections, one-off composition).

**Done when (UI pass):** every new control uses an existing primitive or variant, or adds a named kit change with a one-line why. No same-role one-off.

## Defaults

| Topic | Rule |
|-------|------|
| Utility CSS | Prefer **Tailwind** (or the repo default). Prefer tokens and kit classes over raw hex in product UI |
| Tokens | Map colors, type, space, and radius from `DESIGN.md` into CSS variables / theme. Prefer semantic names (`--color-primary`) over one-off hex on pages |
| Dark mode | Follow the repo strategy (class or media). Do not fork a second palette outside tokens |
| Class merge | Prefer a shared `cn` (or repo equivalent) for conditional classes |
| Variants | Prefer **CVA** (or the repo variant helper) on kit primitives. Named variants beat copy-pasted class strings |
| Server components | Keep style soup out of RSC trees. Prefer kit primitives and token classes over large local class blocks |

## Align with craft

For look and finish, load the assumed craft skills (install-upstream; see pack README):

- `frontend-design` (vendored under `design/`)
- `design-taste-frontend` (Taste)
- `impeccable`

Those skills do not replace this ladder. Apply craft **on** kit primitives and tokens.

## Don't

- Do not invent `DESIGN.md` or a full token kit without asking the user
- Do not add a page-local control that duplicates an existing kit role
- Do not put taste or brand rules in this skill or in kit code comments as a second SoT
- Do not add a new variant when an existing prop or variant already fits
- Do not ship large CSS for one island without need

## References

- [`references/reuse-examples.md`](references/reuse-examples.md): one-off vs variant (before / after)
- [`references/cva-patterns.md`](references/cva-patterns.md): CVA / `cn` sketches

## Related

- Where kit vs feature UI lives → **`project-structure`**
- Focus and contrast → **`accessibility`**
- Pack craft assumptions → [`../README.md`](../README.md)

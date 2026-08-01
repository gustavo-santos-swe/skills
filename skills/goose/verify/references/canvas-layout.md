# Canvas layout (verify)

Visual surface for a **full audit** report. Same sanity rules as every Goose canvas: flat host theme, clear hierarchy, accent only on classification. No gradients, emoji, or decorative chrome (Cursor **canvas** skill).

## Source of truth

Copy [`verify-canvas.template.tsx`](./verify-canvas.template.tsx) into the workspace `canvases/` dir as `<repo-or-slug>-verify.canvas.tsx`, then replace the `report` object. Do not rename its keys.

Import **only** from `cursor/canvas`. Embed all data inline (no fetch).

## Fixed section order

Same every generation (omit an empty classification section only):

1. **Header** - eyebrow `Pack conformance audit`; repo/slug; date; packs checked
2. **Stats** - Drift / Gap / Style / Followed counts (`Stat`)
3. **Callout** - where to focus first (Drift only, plain language)
4. **Findings table** - Drift, Gap, Style rows together; classification as `Pill`; Drift first
5. **Aligned** - Followed highlights table, so the report isn't only a complaint list
6. **Methodology** - packs read, files walked, scope excluded

## Locked labels

- Classification: `Drift` | `Gap` | `Style` | `Followed`
- Tone mapping: Drift -> `danger`, Gap -> `warning`, Style -> `info`, Followed -> `success`

Canvas is a **view** of the same facts as [`report-template.md`](./report-template.md), not a second audit.

## After write

Link the `.canvas.tsx` path in chat so the engineer can open it beside the conversation.

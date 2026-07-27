# Canvas layout (pr-review)

Visual surface for a multi-axis PR review. **Keep it sane:** flat host theme, clear hierarchy, accent only on severity — no gradients, emoji, or decorative chrome (Cursor canvas rules).

## Source of truth

Copy [`pr-review-canvas.template.tsx`](./pr-review-canvas.template.tsx) into the workspace canvases dir as `pr-<n>-review.canvas.tsx`, then replace the `review` object.

Live demo (sample data): open [`pr-review-template.canvas.tsx`](/Users/gusta/.cursor/projects/c-Users-gusta-Dev-projects-skills/canvases/pr-review-template.canvas.tsx) beside chat.

Import **only** from `cursor/canvas`. Embed all data inline (no fetch).

## Aesthetic (sane)

| Do | Don't |
|----|--------|
| Host theme tokens (`useHostTheme`, `Text tone=`) | Hardcoded hex, purple gradients |
| One strong header + stats strip | Wall of identical cards |
| Walk order as the visual focus | Fancy motion / glass / shadows |
| `Code` for file paths | Emoji status markers |
| Tables for findings | Rainbow pills on every row |

Tone: industrial review board — dense enough to scan, quiet enough to read.

## Fixed section order

Same every generation (omit empty finding groups only):

1. **Header** - eyebrow `PR review`; `repo#n: title`; verdict `Pill`; CI; Spec/SoT  
2. **Stats** - Block / Should-fix / Nit counts (`Stat`)  
3. **Summary** - short paragraph  
4. **Human review guide** (`Card`) - inferred structure; numbered read order; why  
5. **Findings** - Block / Should-fix / Nit tables  
6. **Axes clear** - one tertiary line  
7. **Next** - pr-iterate / security-check / post question  

## Locked labels

- Verdict: `Approve` | `Comment` | `Request changes`
- Severity: `Block` | `Should-fix` | `Nit`
- Axis tags: `correctness` | `spec` | `security` | `tests` | `guidelines` | `ship` | `ci`

Canvas is a **view** of the same facts as [`report-template.md`](./report-template.md) — not a second review.

## After write

Link the `.canvas.tsx` path in chat so the engineer can open it beside the conversation.

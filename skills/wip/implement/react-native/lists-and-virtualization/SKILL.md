---
name: rn-lists-and-virtualization
description: Use when building FlashList/FlatList feeds, infinite scroll, or list performance work in React Native.
disable-model-invocation: true
metadata:
  area: wip
---

# Lists and Virtualization

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Feeds, grids, infinite scroll, janky lists.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### List primitive
- FlashList vs FlatList — our default
- `keyExtractor`, item types, `getItemType`

### Performance
- `memo` item boundaries; avoid inline objects/functions that bust memo
- Window size / estimated item size
- Images in cells (→ images-and-media)

### Data
- Pagination / infinite query handoff (→ data-fetching)
- Empty / error / loading row patterns

## Don't
- Don't nest VirtualizedLists in ScrollViews without a justified pattern.
- Don't compute heavy work inside every row render.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


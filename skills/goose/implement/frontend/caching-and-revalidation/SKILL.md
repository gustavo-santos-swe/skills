---
name: web-caching-and-revalidation
description: Use when setting Next.js cache tags, revalidatePath/Tag, ISR, or diagnosing stale UI after mutations.
metadata:
  area: goose
---

# Caching and Revalidation

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- Stale pages after write, tag design, on-demand revalidation.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Model
- Full route cache vs fetch cache vs router cache — what we teach the team
- Tag naming conventions

### After mutations
- `revalidateTag` / `revalidatePath` rules from Server Actions
- When to use `unstable_noStore` / `connection()`

### CDN / deployment
- What Vercel (or host) assumes; purge strategy

## Don't
- Don't revalidate the world (`revalidatePath('/')`) as a habit.
- Don't mix user-specific data into statically cached shells.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


---
name: web-performance
description: Use when improving Next.js Core Web Vitals, bundle size, streaming, or client JS weight.
disable-model-invocation: true
metadata:
  area: goose
---

# Performance

Status: **stub** — topic list below is what to define later (Goose conventions + examples). Keep SKILL.md short; push deep samples to `references/`.

## When to use

- LCP/CLS/INP issues, heavy client bundles, slow TTFB.
- **`implement`** loading this pack for a matching change.

## Topics to fill (checklist)

### Measure
- Lighthouse/CWV, Next bundle analyzer, React profiler
- Budgets we care about

### Levers
- Server vs client split; dynamic `import()`
- Image/font optimization (→ images-fonts-assets)
- Streaming / Suspense boundaries
- Avoiding huge dependencies in client islands

### Align with
- caching-and-revalidation, server-and-client

## Don't
- Don't clientize a tree to “make hooks work” without measuring the JS cost.
- Don't chase micro-opts before CWV evidence.

## References

Optional: `references/` for longer examples. Project-specific paths stay in the target repo `AGENTS.md`.


# Human review guide (dynamic)

Goal: help the engineer **read the diff in a sensible order** for *this* repo - not recite a generic architecture blog.

Fill every subsection. Infer from the **actual tree + changed files**, not from assumed Clean Architecture names.

## Process (agent)

1. List files in the PR diff (exclude lockfiles, generated noise, `bin/`/`obj/` unless the change is about them).
2. Detect how *this* project groups code: folder names, project boundaries (`.csproj`, packages), existing docs/ADRs, patterns in neighboring files.
3. Assign each changed file to a **bucket** (examples - rename to match the repo):
   - Domain / core types
   - Application / use cases / handlers
   - Infrastructure / adapters / persistence
   - Host / API / UI
   - Tests
   - Config / migrations / other
4. Order buckets **dependencies first** (things others depend on before things that call them). Typical backend lean: domain → application → infrastructure → host → tests. If the repo is modular monolith / RN screens / Next app router, invent honest bucket names from the tree.
5. Within a bucket, order by: types/contracts → behaviour → wiring.
6. Call out **entry files** to open first in each bucket (1-3 paths).

## Required prose shape

```markdown
### Inferred structure
How this repo seems layered/modular (2-5 bullets). Cite folder/project names you saw.

### Suggested read order
1. **<bucket>** - `path/a`, `path/b` - <one-line why first>
2. **<bucket>** - …
3. …

### Why this order
2-4 sentences: dependency direction + what to verify at each step (e.g. “confirm invariants in domain before trusting handler mapping”).

### Optional skip
Generated, vendor, or pure formatting files - list if present.
```

## Anti-patterns

- Don’t always say “Domain → Application → Infrastructure” if the repo doesn’t use those names or the PR only touches UI.
- Don’t list every file - prioritize; group the rest as “also in this bucket: …”.
- Don’t make the guide longer than the findings when the PR is tiny (still include the three subsections; keep bullets short).

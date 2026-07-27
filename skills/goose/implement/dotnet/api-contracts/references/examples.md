# API contracts sketches

## Breaking vs additive

| Change | Kind |
|--------|------|
| Add `nickname?` to response | Additive |
| Rename `name` → `displayName` | Breaking (or lockstep rename everywhere) |
| `amount` was major units, now cents, same field name | Breaking (meaning drift) |
| New `POST /api/v1/tags` | Additive |
| Remove `GET /api/v1/legacy-report` | Breaking unless lockstep + no external callers |

## PR blurb (lockstep)

```text
Breaking JSON field rename: CardResponse.name → displayName.
Lockstep: mobile + web updated in this release; no /v2.
No external API consumers.
```

## PR blurb (public)

```text
Breaking: remove deprecated query param `page` (offset).
Clients must use cursor pagination.
Overlap: param accepted until 2026-09-01, then 400.
```

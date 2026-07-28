# Greenfield shape

Load only on **`brainstorm`** branch **`greenfield`**. One question at a time; recommend + why; wait.

Job: lock **which surfaces exist** and **which stack** each uses, before product grill and pack decision surfaces.

## Surfaces

Pick one or more. Multi is fine.

| Surface | Goose default stack | Pack |
|---------|---------------------|------|
| **API** | .NET (ASP.NET) | [`../../implement/dotnet/`](../../implement/dotnet/) |
| **Web** | Next.js App Router | [`../../implement/frontend/`](../../implement/frontend/) (stub OK) |
| **Mobile** | Expo / React Native | [`../../implement/react-native/`](../../implement/react-native/) (stub OK) |
| **Desktop** | *(no Goose pack)* | User brings stack, or **later** / out until a pack exists. Do not invent SOTA. |

## Grill order (Shape)

1. **Surfaces** — which of API / Web / Mobile / Desktop are in this cut? (multi OK)
2. **Stack per surface** — offer the Goose default; accept, override (with reason), or mark surface **later**
3. **Active packs** — derive from chosen stacks (API .NET → `dotnet` + usually `database`; Web → `frontend`; Mobile → `react-native`)
4. Stop Shape when every chosen surface has stack **or** explicit later/out

## Defaults to recommend

- New Goose backend → **API + .NET**
- Browser app → **Web + Next** (even if pack is stub; mark gaps in freeze)
- Phone/tablet app → **Mobile + Expo/RN** (stub OK)
- Desktop → prefer **later** unless the user already knows the stack

## Completion

Shape done when the freeze can list:

```
Surfaces: …
Stacks: …
Active packs (order for Platform phase): …
```

Then continue **`brainstorm`** greenfield → Product → Platform.

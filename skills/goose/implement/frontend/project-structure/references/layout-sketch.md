# Layout sketches

Examples only. Prefer the target repo tree when it already disagrees.

## Small app (route colocation)

```
src/
  app/
    layout.tsx
    page.tsx
    (auth)/
      login/page.tsx
    (app)/
      dashboard/page.tsx
  components/
    ui/
      button.tsx
      input.tsx
  lib/
    cn.ts
```

## Product with features

```
src/
  app/
    layout.tsx
    (marketing)/
      page.tsx
      pricing/page.tsx
    (app)/
      layout.tsx
      bills/page.tsx
  components/
    ui/
      button.tsx
      card.tsx
      dialog.tsx
  features/
    billing/
      BillList.tsx
      useBills.ts
    checkout/
      CheckoutForm.tsx
  lib/
    cn.ts
    api.ts
```

`BillList` composes kit `Card` / `Button`. It does not redefine a local primary button.

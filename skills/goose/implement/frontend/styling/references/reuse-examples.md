# Reuse examples (one-off vs kit)

Load when a control looks "almost" like an existing kit role.

## Bad: same role, page-local

```tsx
// app/(marketing)/pricing/page.tsx
<button className="rounded-md bg-[#4F46E5] px-4 py-2 text-sm font-medium text-white hover:bg-[#4338CA]">
  Start trial
</button>
```

Problems: hex outside tokens; duplicates primary button role; next page will copy again.

## Good: existing variant

```tsx
import { Button } from "@/components/ui/button";

<Button variant="primary" size="md">
  Start trial
</Button>
```

## Good: extend the kit when the role is new

When the product needs a new shared role (example: `destructive` on buttons):

1. Add a named variant on the kit primitive (CVA).
2. Map colors from `DESIGN.md` / tokens.
3. Use the variant at the call site.

```tsx
// components/ui/button.tsx (sketch)
const buttonVariants = cva("inline-flex items-center justify-center …", {
  variants: {
    variant: {
      primary: "bg-primary text-primary-foreground hover:bg-primary/90",
      ghost: "hover:bg-muted",
      destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
    },
    size: {
      sm: "h-8 px-3 text-sm",
      md: "h-10 px-4 text-sm",
    },
  },
  defaultVariants: { variant: "primary", size: "md" },
});
```

Call site:

```tsx
<Button variant="destructive">Remove seat</Button>
```

## Feature-only is OK for layout glue

A pricing column wrapper or hero stack may stay in the feature folder. A third "primary CTA" button must not.

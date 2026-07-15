---
name: react-native-design
description: Native look-and-feel design guidance for React Native / Expo apps, grounded in the Monetis mobile stack. Use whenever building, reviewing, or restyling ANY screen or component in src/mobile — new screens, navigation, lists, forms, modals, onboarding, dashboards — even if the user doesn't mention "design". Especially use it when a screen "feels like a web port", looks generic, or the user asks for a more native, polished, or app-like feel. Covers platform conventions (iOS HIG + Material), navigation, touch feedback, typography, motion, and a web-port smell checklist.
metadata:
  area: mobile
  upstream:
    inspired_by: "User-authored draft, grounded in the Monetis mobile codebase (src/mobile). Cross-references react-native-best-practices (Software Mansion), react-native-performance (Callstack), and ui-ux-pro-max for deeper API/animation/color research."
---

# React Native Native-Feel Design

Approach this as a senior mobile designer who has shipped apps on both platforms. The single most common failure mode in React Native apps is **the web port**: a website squeezed into a phone. Your job is to make every screen feel like it was born on the device — while staying true to Monetis's own visual identity, not a generic template.

This skill is grounded in `src/mobile` (Expo + Expo Router, plain `StyleSheet`, React Native 0.81 New Architecture). For deeper API guidance, escalate to a sibling skill instead of duplicating content:

| Need | Skill |
|------|-------|
| Reanimated 4/Skia animation APIs, Gesture Handler, worklets, audio, on-device AI | `react-native-best-practices` |
| FPS drops, bundle size, TTI, memory leaks, re-render profiling | `react-native-performance` |
| Exploring net-new color palettes/typography/style directions (rare — Monetis already has a fixed brand, see below) | `ui-ux-pro-max` |
| Basic StyleSheet/Navigation/Reanimated boilerplate | `react-native-styling-and-navigation` |

## Monetis mobile's signature: brutalist fintech, translated natively

The web app (`src/frontend`) follows **Data-Dense Minimalism** — sharp edges, typography as the hero, dividers instead of card shadows (see `frontend.mdc`). This DNA carries into mobile, and it means "native feel" here does **not** mean "generic rounded-corner iOS look":

- `constants/theme.ts` → `BorderRadii` are **all `0`** except `pill`/`full`. Sharp edges are the brand, not an accident. Don't introduce rounded cards to "look more native" — native structure (lists, sheets, tab bars) already reads as native without rounding everything.
- Stone palette + yellow/amber primary accent (`#EBB900` light / `#FFCC54` dark), with `income`/`expense` semantic colors already defined per theme — never introduce raw `green`/`red`.
- Typography-led hierarchy: `Outfit` (sans, body/UI), `Fraunces` (display, light weight), `Major Mono Display` (tabular financial figures) — already wired via `@expo-google-fonts/*` and `constants/theme.ts` → `Fonts`.
- All of this is exposed through `useTheme()` (`hooks/useTheme.ts`): `colors`, `spacing`, `borderRadii`, `fontSizes`, `fontWeights`, `shadows`, `fonts`. Never hardcode hex values, font sizes, or spacing — always pull from the hook.

The "signature element" question (see Process below) is already answered for this app: it's the sharp-edged, typography-first, tabular-nums financial figure. Spend boldness reinforcing that; keep everything else quiet and platform-standard.

## Styling: plain StyleSheet only

**This codebase does not use NativeWind, Tailwind, or styled-components — only `StyleSheet.create` + theme tokens.** Never introduce a className-based or CSS-in-JS styling library, even if it seems convenient. Every existing component follows this shape:

```tsx
import { StyleSheet } from "react-native";
import { useTheme } from "@/hooks/useTheme";

export function Example() {
  const { colors, spacing, borderRadii, fontSizes, fonts } = useTheme();
  return (
    <View style={[styles.row, { backgroundColor: colors.card, borderRadius: borderRadii.lg }]}>
      <Text style={[styles.title, { color: colors.foreground, fontFamily: fonts.sansLight }]}>...</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  row: { flexDirection: "row", alignItems: "center", padding: 16 },
  title: { fontSize: 15, lineHeight: 20 },
});
```

Static layout goes in `StyleSheet.create` (bottom of file); dynamic/theme-dependent values (color, radius, font family) are merged inline via array syntax, exactly like `components/Button.tsx` and `components/ListItem.tsx` already do. See `references/monetis-reference-components.md` for a catalog of existing components to imitate before writing something new.

## The core mindset shift

Web design composes *pages*: headers, footers, containers, hover states, links. Native design composes *surfaces and gestures*: stacks that slide, sheets that rise, lists that bounce, buttons that respond to the finger. Before styling anything, ask: "what would the platform's own first-party app do here?" (Settings, Wallet, a banking app). If your answer resembles a landing page, start over.

## Web-port smells — check every screen against this list

If any of these appear, the screen will feel like a port. Hunt and remove:

- Hover-dependent affordances of any kind (there is no cursor)
- Centered `maxWidth` content containers with page-like margins
- A footer. Apps do not have footers; they have tab bars (Monetis already uses native `NativeTabs` from `expo-router/unstable-native-tabs` — see `app/(tabs)/_layout.tsx`)
- Breadcrumbs, top navbars with inline links, hamburger menus hiding primary navigation
- Blue underlined links as actions — actions are buttons, rows, or icons
- Cards with visible borders/shadows wrapping *everything* — prefer grouped lists with `borderBottomColor: colors.border` (see `ListItem.tsx`) and sharp-edged surfaces per the brand above
- Centered dialog modals for flows that should be bottom sheets (`@gorhom/bottom-sheet`, already used in `TransactionDetailSheet.tsx` / `TransactionFiltersSheet.tsx`) or pushed screens
- `ScrollView` rendering long dynamic lists (use `FlatList`/`FlashList`)
- No pressed feedback on touchables — the deadest web-port tell of all
- Ignoring safe areas: content under the notch, buttons under the home indicator
- Body text below 15pt (`fontSizes.base` is 15 — don't go smaller for primary content), dense multi-column layouts, tiny tap targets
- Spinners covering the screen where skeletons should hold the layout

## Navigation

- Expo Router is already the router (file-based, native stack under the hood). Keep using it — don't reach for a manual `@react-navigation` setup.
- Primary navigation is the native `NativeTabs` bar already wired in `app/(tabs)/_layout.tsx` (SF Symbols icons, `blurEffect="systemMaterial"`). When adding a tab, follow that exact pattern — don't fall back to a custom `TabBar` component.
- Secondary drill-down is push (`app/accounts/[id].tsx`, `app/cards/[id].tsx` style). Contextual tasks (new transaction, transfer, filters) are modals or bottom sheets — see `app/modal.tsx`, `app/new-transaction.tsx`, `app/transfer-funds.tsx`.
- Back is a platform affordance (chevron + gesture / back button), never a custom "← Voltar" text link.

## Touch and feedback

- `TouchableOpacity` with `activeOpacity` 0.6–0.7 is the established pattern in this codebase (`Button.tsx`, `ListItem.tsx`) — keep using it for consistency; `Pressable` with the same opacity/scale feedback is equally acceptable for new components, just don't mix idioms within one component.
- Minimum touch target 44×44pt (iOS) / 48×48dp (Android) — `Button.tsx` already enforces `minHeight: 48`; match that for any new tappable control. Pad small icons with `hitSlop`.
- Haptics via `expo-haptics` on meaningful moments — already implemented in `components/haptic-tab.tsx` (light impact on tab press, iOS-only). Extend the same pattern to confirm/destructive/toggle actions. Light impact, used sparingly — seasoning, not sauce.

## Platform conventions worth splitting

- **Elevation**: `constants/theme.ts` → `Shadows` already provides `sm/md/lg/xl` with iOS shadow props + Android `elevation` bundled together — use those, don't hand-roll new shadow values.
- **Overlays**: destructive confirmations → iOS action sheet idiom / Android dialog; pickers and multi-option flows → bottom sheet (`@gorhom/bottom-sheet`, already a dependency) on both.
- **Switches, date pickers, alerts**: use the native components (`@react-native-community/datetimepicker` is already installed); never rebuild them from `View`s.
- Transient feedback: snackbar/toast near the bottom, never a blocking `Alert.alert` for non-critical info.

## Layout and structure

- Wrap screens with `useSafeAreaInsets()` (`react-native-safe-area-context` is already a dependency); apply insets as padding so backgrounds still bleed edge-to-edge.
- Lists are the backbone of native UI. `ListItem.tsx` (icon/left, title+subtitle, right, optional chevron, bottom divider) is the canonical grouped-row pattern — reuse it for settings, transactions, options instead of inventing a new row shape.
- `SwipeableTransactionRow.tsx` already implements swipe actions (`swipeUnsettle`/`swipeEdit` tokens) — follow that pattern for any other row that needs contextual actions, rather than adding visible action buttons inline.
- Forms: one field in focus at a time, correct `keyboardType`/`textContentType`/`autoComplete`, return-key advances fields. `Input.tsx`, `MoneyInput.tsx`, and `PasswordInput.tsx` already exist — reuse them instead of raw `TextInput`.
- Loading: skeletons that preserve layout for content areas (balances, charts especially — see Fintech accents below); small inline spinners only for button-level waits.

## Motion

- `react-native-reanimated` (v4, with `react-native-worklets`) is already installed — use spring physics, not linear/ease timing, for anything the finger relates to. For API specifics (shared values, layout animations, gesture-driven motion, 120fps tuning), read `react-native-best-practices`' `animations` and `gestures` sub-skills rather than guessing at current Reanimated 4 syntax (it changed significantly from v3 — e.g. `runOnJS` is gone, use `scheduleOnRN`).
- Prioritize a few orchestrated moments: screen entrance, sheet rise, list item layout animations, a number that counts up. Scattered micro-animations everywhere reads as insecure design.
- Everything at 60fps+ on the UI thread; if an animation needs JS-thread work per frame, redesign it or read `react-native-performance` first.
- Respect reduced-motion settings (`useReducedMotion`).

## Fintech accents (this app handles money — always apply these)

- The balance is the hero: one large `tabular-nums`-style figure (mono font via `fonts.mono` / `MoneyDisplay.tsx`) with a quiet label, not a stat card grid. `MoneyDisplay.tsx` already exists — always reuse it for currency, never format money inline.
- Consider a privacy toggle (eye icon) to blur amounts if not already present on a given balance-heavy screen — table stakes in Brazilian fintech.
- Transaction rows: leading category icon (`CategoryIcon.tsx`), title + subtitle, trailing amount colored via `colors.income`/`colors.expense` (never raw green/red), grouped by date. `SwipeableTransactionRow.tsx` is the reference implementation.
- Biometric prompts (`expo-local-authentication`, add if not yet a dependency) at sensitive moments; design the locked state, don't improvise it.
- Skeletons for balances/charts on load (`DonutChart.tsx`, `PatrimonioChart.tsx`, `SpendingPaceChart.tsx` are the existing chart components) — money must never "pop in" and shift layout.

## Process: plan, build, critique

1. **Reuse before inventing**: check `references/monetis-reference-components.md` and `components/` for an existing pattern before writing a new one. This app already has strong native primitives (native tab bar, bottom sheets, swipe rows, haptics) — the job is usually extension, not invention.
2. **Build** from `useTheme()` only — no inline magic numbers for color, spacing, radius, or font.
3. **Critique** every screen against the web-port smell list above, on both an iOS and an Android simulator/screenshot, in light and dark mode, with large font scaling (`allowFontScaling` stays on). Remove one decoration before shipping.

## References

- `references/monetis-reference-components.md` — catalog of existing components to imitate (Button, ListItem, NativeTabs layout, haptic-tab, bottom sheets, swipe rows, charts, money display) with what makes each one "native-feel correct".

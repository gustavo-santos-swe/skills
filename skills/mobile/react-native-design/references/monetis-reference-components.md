# Monetis mobile — canonical component reference

Before building a new screen or component, check whether one of these already covers the pattern. All live under `src/mobile/components/` unless noted, and all use `StyleSheet.create` + `useTheme()` — no exceptions.

## Buttons — `Button.tsx`

`TouchableOpacity` with `activeOpacity={0.7}`, `minHeight: 48`, four variants (`primary`/`secondary`/`destructive`/`outline`) resolved from `useTheme().colors`, `borderRadius: borderRadii.lg` (currently `0` — sharp edges by design, don't round it). Disabled state swaps to `colors.muted`/`colors.mutedForeground` rather than lowering opacity. Reuse this for any button; don't hand-roll a new `TouchableOpacity` + `Text` pair.

## Grouped list rows — `ListItem.tsx`

The canonical native-feel row: `left` slot (icon), `center` (title + optional subtitle, `numberOfLines={1}`), `right` slot, optional `chevron`. Bottom divider via `borderBottomColor: colors.border` (no card wrapper, no shadow). Wrapped in `TouchableOpacity activeOpacity={0.6}` when `onPress` is provided, otherwise renders as a static `View`. Use this for settings rows, account rows, any "icon + text + trailing content" pattern instead of inventing a new row shape.

## Tab bar — `app/(tabs)/_layout.tsx`

Uses `NativeTabs` from `expo-router/unstable-native-tabs` (not a JS-rendered tab bar) with `blurEffect="systemMaterial"` and SF Symbols icons (`default`/`selected` variants) via `<Icon sf={{ ... }} />`. This is as native as a tab bar gets — a real `UITabBar`. When adding a tab, add a `NativeTabs.Trigger`; never introduce a custom-rendered tab bar component.

## Tab press feedback — `haptic-tab.tsx`

Wraps `PlatformPressable` (`@react-navigation/elements`) and fires `Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)` on `onPressIn`, gated to `process.env.EXPO_OS === 'ios'`. This is the reference pattern for "light haptic on press, iOS-only unless the interaction is significant enough to also warrant Android feedback."

## Swipe actions — `SwipeableTransactionRow.tsx`

Uses `Swipeable` from `react-native-gesture-handler` (not a custom `PanResponder`). Right actions (settle/undo/edit/delete) render as colored `TouchableOpacity` blocks revealed by the swipe, each triggering `Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium)` before closing the swipeable and running the action after a short delay (avoids the action firing mid-animation). A `swipedRef` guards against a swipe gesture also triggering `onPress`. Follow this exact shape for any other row that needs contextual actions instead of inline visible buttons.

## Bottom sheets — `TransactionDetailSheet.tsx`, `TransactionFiltersSheet.tsx`, `AccountFormModal.tsx`, `CreditCardFormModal.tsx`

Built on `@gorhom/bottom-sheet`. Any flow that would be a centered modal dialog on web (view details, filter, edit a form) is a bottom sheet here instead. Don't introduce `Modal` with a centered card for these use cases — rising sheets are the established idiom.

## Money formatting — `MoneyDisplay.tsx`, `MoneyInput.tsx`

`MoneyDisplay` has four sizes (`hero`/`large`/`medium`/`small`), uses `fonts.display` (Fraunces) for hero/large and `fonts.sansLight` for medium/small, resolves color from `colors.income`/`colors.expense` when `showSign` is set, and supports `dimDecimals` (integer part full-strength, decimals at `opacity: 0.6` and a smaller size — the "dimmed cents" treatment used for hero balances). Always use this for any currency value; never call `formatCurrency` and render a raw `<Text>` directly. `MoneyInput` is the matching input-side component for amount entry.

## Category icon — `CategoryIcon.tsx`

Resolves a category to its icon/color chip. Reuse for any place a transaction category needs a visual identity instead of a plain label.

## Charts — `DonutChart.tsx`, `PatrimonioChart.tsx`, `SpendingPaceChart.tsx`

Existing chart components for allocation (donut), net worth over time, and spending pace. Check these before adding a new charting library — `react-native-gifted-charts` is already the dependency in use.

## Icons — `lucide-react-native`

The icon set already in use across the app (see imports like `CheckCheck, Undo2, Pencil, Trash2, Wallet, CreditCard` in `SwipeableTransactionRow.tsx`). Don't mix in a second icon library; `@expo/vector-icons` is also present but `lucide-react-native` is the primary choice for new UI.

## Inputs — `Input.tsx`, `PasswordInput.tsx`, `MoneyInput.tsx`, `MonthYearPicker.tsx`

Themed wrappers around `TextInput` and native pickers. Use these instead of a raw `TextInput` so keyboard type, focus styling, and error states stay consistent.

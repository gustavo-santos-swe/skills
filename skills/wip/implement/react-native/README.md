# react-native

Expo / React Native conventions for Goose mobile. Lives under **`implement`**.

Path: `skills/wip/implement/react-native/`. Load from **`implement`** by concern. Stubs list **Topics to fill** — Goose decisions later.

Deep vendor playbooks (animations, gestures, RN best practices) also live under [`../../../mobile/`](../../../mobile/) — use those for technique depth; this pack is **our** defaults.

## Map

### Core
| Skill | Focus |
|-------|--------|
| [`project-structure`](./project-structure/) | Expo/RN layout |
| [`navigation`](./navigation/) | Expo Router / navigators |
| [`styling`](./styling/) | StyleSheet / tokens / NativeWind |
| [`theming`](./theming/) | Light/dark / brand themes |
| [`forms-and-inputs`](./forms-and-inputs/) | Forms, keyboard |
| [`state-management`](./state-management/) | Client vs server state |
| [`data-fetching`](./data-fetching/) | API client + cache |
| [`lists-and-virtualization`](./lists-and-virtualization/) | FlashList / feeds |

### Device & platform
| Skill | Focus |
|-------|--------|
| [`auth-and-secure-storage`](./auth-and-secure-storage/) | Session + SecureStore |
| [`offline-and-sync`](./offline-and-sync/) | Offline / queues |
| [`deep-linking`](./deep-linking/) | App/Universal links |
| [`push-notifications`](./push-notifications/) | Push / tap routing |
| [`images-and-media`](./images-and-media/) | Images, picker, media |
| [`native-modules`](./native-modules/) | Expo modules / native |

### Motion & quality
| Skill | Focus |
|-------|--------|
| [`animations`](./animations/) | Reanimated defaults |
| [`gestures`](./gestures/) | Gesture Handler |
| [`error-and-boundaries`](./error-and-boundaries/) | Error UI + reporting |
| [`testing`](./testing/) | Jest / RNTL / E2E |
| [`performance`](./performance/) | Jank, TTI, re-renders |
| [`accessibility`](./accessibility/) | VoiceOver / TalkBack |

Out of scope here: full native iOS/Android apps without RN.

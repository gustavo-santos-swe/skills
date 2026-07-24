# CONTEXT.md and CONTEXT-MAP.md (Goose)

Ubiquitous language for the target repo. Owned by **`brainstorm`** when terms crystallize.

`CONTEXT.md` is a **glossary of what words mean here**. Not a spec, not ADRs, not implementation notes. Multi-context repos use a root map (bounded contexts) so each glossary stays local.

## CONTEXT.md

```md
# {Context name}

{One or two sentences: what this context is for.}

## Language

**Order**:
A customer's request to buy one or more products, accepted by the system.
_Avoid_: Purchase, transaction, cart

**Invoice**:
A request for payment sent after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

### Rules

- **One word per concept.** Synonyms go under `_Avoid_`.
- **Tight definitions.** One or two sentences. What it *is*, not the full behavior of the system.
- **Domain only.** Skip general CS (timeout, DTO, retry) even if the code is full of them.
- **Cluster when useful.** Subheadings for natural groups; flat list for small glossaries.
- **No implementation.** No schemas, endpoints, frameworks, ticket IDs, or library names.

Update **inline** when a term is settled. Create the file lazily on the first term.

## CONTEXT-MAP.md (multi-context only)

Root file. Lists contexts, where each `CONTEXT.md` lives, and how contexts relate.

```md
# Context map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — intake and lifecycle of customer orders
- [Billing](./src/billing/CONTEXT.md) — invoices and payment collection
- [Fulfillment](./src/fulfillment/CONTEXT.md) — pick, pack, ship

## Relationships

- **Ordering → Fulfillment**: Ordering publishes `OrderPlaced`; Fulfillment starts picking
- **Fulfillment → Billing**: Fulfillment publishes `ShipmentDispatched`; Billing invoices
- **Ordering ↔ Billing**: share `CustomerId` and `Money` meanings; no shared mutable aggregates
```

### Which layout

| Situation | Action |
|-----------|--------|
| `CONTEXT-MAP.md` exists | Read it; edit the matching context’s `CONTEXT.md` |
| Only root `CONTEXT.md` | Single context |
| Neither | Create root `CONTEXT.md` when the first term lands |
| Multi-context, unclear target | Ask |

`AGENTS.md` in the target repo may override paths. Update the map when a new context appears.

## Challenge the language

- Conflict with an existing definition → surface it immediately; pick one meaning.
- Overloaded everyday words ("account", "user") → force a precise term.
- Same idea, two labels across contexts → either align or document the relationship on the map.

# CONTEXT.md and CONTEXT-MAP.md

Formats for the target repo. Owned by **`brainstorm`** when terms crystallize. Adapted from Matt Pocock domain-modeling (see skill `inspired_by`).

## CONTEXT.md structure

```md
# {Context Name}

{One or two sentences: what this context is and why it exists.}

## Language

**Order**:
{One or two sentences: what the term *is*}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

## Rules

- **Opinionated.** Same concept, many words → pick one; put the rest under `_Avoid_`.
- **Tight.** One or two sentences. Define what it *is*, not what it does in the system.
- **Domain only.** No general programming terms (timeouts, error types, utils) even if the project uses them a lot. Ask: unique to this context, or general CS? Only the former.
- **Cluster when natural.** Subheadings for groups; flat list is fine for a small glossary.
- **No implementation.** No schemas, endpoints, frameworks, or ticket IDs.

## Single vs multi-context

**Single (usual):** one `CONTEXT.md` at the repo root (unless `AGENTS.md` overrides the path).

**Multiple:** root `CONTEXT-MAP.md` lists contexts, paths, and relationships:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) — generates invoices and processes payments
- [Fulfillment](./src/fulfillment/CONTEXT.md) — manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

### How to pick the structure

- `CONTEXT-MAP.md` exists → read it; update the right context’s `CONTEXT.md`
- Only root `CONTEXT.md` → single context
- Neither → create root `CONTEXT.md` when the first term is resolved
- Multi-context and unclear which file → ask

Create files lazily. Update the map when a new context appears.

# Database examples

Language-agnostic sketches. Names/types adapt to Postgres / SQL Server / etc.

## Surrogate PK + natural unique

```sql
CREATE TABLE customers (
    id              uuid PRIMARY KEY,           -- or bigint identity / Guid v7 from app
    email           text NOT NULL,
    display_name    text NOT NULL,
    created_at      timestamptz NOT NULL,
    CONSTRAINT uq_customers_email UNIQUE (email)
);
```

Don’t: `PRIMARY KEY (email)` if email can change.

## FK + index on the FK side

```sql
CREATE TABLE orders (
    id           uuid PRIMARY KEY,
    customer_id  uuid NOT NULL REFERENCES customers (id),
    status       text NOT NULL,
    total        numeric(18, 2) NOT NULL,
    row_version  bytea NOT NULL,                -- or xmin / rowversion / integer version
    CONSTRAINT ck_orders_total_nonneg CHECK (total >= 0)
);

CREATE INDEX ix_orders_customer_id ON orders (customer_id);
-- composite for a known list path: (customer_id, created_at DESC)
```

## Soft-delete (opt-in) + live uniqueness

```sql
ALTER TABLE customers ADD COLUMN deleted_at timestamptz NULL;

-- Only one *live* row per email
CREATE UNIQUE INDEX uq_customers_email_live
    ON customers (email)
    WHERE deleted_at IS NULL;
```

## Expand → contract (rename column)

1. **Expand:** add `display_name`, backfill from `name`, dual-read/write if needed  
2. Deploy app that uses `display_name`  
3. **Contract:** stop writing `name`, drop `name` in a later migration  

Never rename in place under rolling deploys without that sequence. EF apply rules → **migrations-and-compat**.

## Keyset page (SQL shape)

```sql
-- seek page after (created_at, id) cursor
SELECT id, created_at, …
FROM orders
WHERE customer_id = @customer_id
  AND (created_at, id) < (@cursor_created_at, @cursor_id)  -- tuple compare; dialect may vary
ORDER BY created_at DESC, id DESC
LIMIT @limit;
```

Prefer this over `OFFSET 100000` for feeds.

## JSON — justified bag, relational truth

```sql
-- OK: raw webhook payload for audit/replay
CREATE TABLE webhook_inbox (
    id           uuid PRIMARY KEY,
    provider     text NOT NULL,
    received_at  timestamptz NOT NULL,
    payload      jsonb NOT NULL
);

-- Don't: put order status / total only inside payload jsonb
```

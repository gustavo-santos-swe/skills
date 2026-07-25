# DB integration sketches

## Fluent mapping (Infrastructure)

```csharp
public sealed class CustomerMapping : IEntityTypeConfiguration<Customer>
{
    public void Configure(EntityTypeBuilder<Customer> builder)
    {
        builder.ToTable("customers");
        builder.HasKey(x => x.Id);
        builder.Property(x => x.Id)
            .HasConversion(id => id.Value, v => new CustomerId(v));
        builder.Property(x => x.CreatedAt); // NodaTime Instant via provider/plugin
        builder.Property(x => x.RowVersion).IsRowVersion(); // or provider equivalent
    }
}
```

## No-track read

```csharp
var list = await db.Customers
    .AsNoTracking()
    .Where(c => c.Email == email)
    .Select(c => new CustomerSummary(c.Id, c.Name))
    .ToListAsync(ct);
```

## Mutate + one SaveChanges

```csharp
var customer = await db.Customers.SingleOrDefaultAsync(c => c.Id == id, ct);
if (customer is null)
    return new NotFound("Customers.NotFound", "…");

customer.Rename(name);
await db.SaveChangesAsync(ct);
```

## Concurrency → Conflict

```csharp
try
{
    await db.SaveChangesAsync(ct);
}
catch (DbUpdateConcurrencyException)
{
    return new Conflict("Customers.Concurrency", "Customer was modified by another request.");
}
```

## Raw SQL (rare)

```csharp
// parameterized only
await db.Database.ExecuteSqlAsync(
    $"UPDATE customers SET notes = {notes} WHERE id = {id.Value}",
    ct);
```

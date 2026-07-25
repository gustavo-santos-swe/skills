# Time and IDs sketches

Illustrative greenfield shapes.

## Instant from TimeProvider

```csharp
public static Instant UtcNow(TimeProvider timeProvider) =>
    Instant.FromDateTimeOffset(timeProvider.GetUtcNow());
```

## “Today” in a user zone

```csharp
public static LocalDate TodayIn(TimeProvider timeProvider, DateTimeZone zone) =>
    UtcNow(timeProvider).InZone(zone).Date;
```

## Typed id + Guid v7

```csharp
public readonly record struct CustomerId(Guid Value)
{
    public static CustomerId New() => new(Guid.CreateVersion7());
    public override string ToString() => Value.ToString();
}

public sealed class Customer
{
    public CustomerId Id { get; private set; } = CustomerId.New();
    public Instant CreatedAt { get; private set; }

    public static Customer Register(string name, Instant createdAt) => new()
    {
        // set name…
        CreatedAt = createdAt
    };
}
```

## Handler passes Instant in

```csharp
var now = Instant.FromDateTimeOffset(_timeProvider.GetUtcNow());
var customer = Customer.Register(request.Name, now);
```

## Test: fake clock

```csharp
var time = new FakeTimeProvider(new DateTimeOffset(2026, 7, 24, 15, 0, 0, TimeSpan.Zero));
var handler = new CreateCustomerRequestHandler(/* … */, time);
// assert CreatedAt / LocalDate from that instant
```

## Human-facing number (sketch)

Invoice `Number` from a DB sequence / dedicated allocator; entity still has `InvoiceId` (Guid v7) as the surrogate key.

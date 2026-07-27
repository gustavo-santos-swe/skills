# Domain modeling sketches

Illustrative greenfield shapes. Names are examples only.

## Strongly typed id

```csharp
public readonly record struct CreditCardId(Guid Value)
{
    public static CreditCardId New() => new(Guid.CreateVersion7());
    public override string ToString() => Value.ToString();
}
```

## Value object (parse → Result)

```csharp
public sealed class Cpf : IEquatable<Cpf>
{
    public string Digits { get; }

    private Cpf(string digits) => Digits = digits;

    public static Result<Cpf> Create(string? input)
    {
        // normalize + validate…
        if (/* invalid */)
            return new ValidationFailed("Cpf.Invalid", /* … */);

        return new Ok<Cpf>(new Cpf(digits));
    }

    public bool Equals(Cpf? other) => other is not null && Digits == other.Digits;
    // GetHashCode / == …
}
```

## Entity mutator (unexpected vs expected)

```csharp
public sealed class CreditCard : AggregateRoot
{
    public CreditCardId Id { get; private set; }
    public string Name { get; private set; } = "";

    // After App validated name — broken invariant is a bug
    public void Rename(string name)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new InvalidOperationException("Rename called with empty name.");

        Name = name.Trim();
        AddDomainEvent(new CreditCardRenamed(Id, Name));
    }

    // Expected refusal from state
    public Result<CreditCard> Archive()
    {
        if (HasOpenFinanceLink)
            return new Conflict("CreditCards.CannotArchiveLinked", "…");

        // …
        return new Ok<CreditCard>(this);
    }
}
```

## Enum for a closed set

```csharp
public enum StatementStatus
{
    Open,
    Closed,
    Paid
}

// not: string status = "open";
```

## Domain event

```csharp
public sealed record CreditCardRenamed(CreditCardId CreditCardId, string Name) : DomainEvent;
```

Dispatch after `SaveChanges` succeeds; then `ClearDomainEvents()`.

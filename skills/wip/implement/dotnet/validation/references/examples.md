# Validation sketches

## Request validator (sync, colocated)

```csharp
public class CreateCustomerRequestValidator : AbstractValidator<CreateCustomerRequest>
{
    public CreateCustomerRequestValidator()
    {
        RuleFor(x => x.Name).NotEmpty().MaximumLength(200);
        RuleFor(x => x.Email).NotEmpty().EmailAddress();
        RuleFor(x => x)
            .Must(x => x.BillingCountry is not null || x.TaxId is null)
            .WithMessage("TaxId requires BillingCountry.")
            .WithName("TaxId");
    }
}
```

## Handler: validate then uniqueness

```csharp
var validation = await _validator.ValidateAsync(request, ct);
if (!validation.IsValid)
{
    var errors = validation.Errors
        .GroupBy(e => e.PropertyName)
        .ToDictionary(g => g.Key, g => g.Select(e => e.ErrorMessage).ToArray());
    return new ValidationFailed("Customers.Validation", errors);
}

if (await _customers.ExistsByEmail(email, ct))
    return new Conflict("Customers.EmailTaken", "Email already registered.");

// domain VO + persist; unique index still required
```

## Domain still guards

```csharp
public static Result<Email> Create(string? input) { /* normalize + validate */ }
```

Jobs/imports call `Email.Create` even when they never hit FluentValidation.

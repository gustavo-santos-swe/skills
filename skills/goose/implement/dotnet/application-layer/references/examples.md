# Application layer sketches

Illustrative greenfield shapes. Names are examples only.

## One file per use case

`Application/Customers/Create.cs` (or `CreateCustomer.cs` — match the feature folder style):

```csharp
public record CreateCustomerRequest(string Name, string Email);

public record CreateCustomerResponse(CustomerId Id, string Name, string Email);

public class CreateCustomerRequestValidator : AbstractValidator<CreateCustomerRequest>
{
    public CreateCustomerRequestValidator()
    {
        RuleFor(x => x.Name).NotEmpty().MaximumLength(200);
        RuleFor(x => x.Email).NotEmpty().EmailAddress();
    }
}

public interface ICreateCustomerRequestHandler
{
    Task<Result<CreateCustomerResponse>> Handle(
        CreateCustomerRequest request,
        CancellationToken cancellationToken);
}

public sealed class CreateCustomerRequestHandler : ICreateCustomerRequestHandler
{
    private readonly ICustomerRepository _customers;
    private readonly IUnitOfWork _uow;
    private readonly CreateCustomerRequestValidator _validator = new();

    public CreateCustomerRequestHandler(ICustomerRepository customers, IUnitOfWork uow)
    {
        _customers = customers;
        _uow = uow;
    }

    public async Task<Result<CreateCustomerResponse>> Handle(
        CreateCustomerRequest request,
        CancellationToken cancellationToken)
    {
        var validation = await _validator.ValidateAsync(request, cancellationToken);
        if (!validation.IsValid)
            return ToValidationFailed(validation);

        // ownership / policy checks here when the use case needs them

        var email = Email.Create(request.Email);
        if (email is not Ok<Email> okEmail)
            return email; // ValidationFailed from VO

        if (await _customers.ExistsByEmail(okEmail.Value, cancellationToken))
            return new Conflict("Customers.EmailTaken", "Email already registered.");

        var customer = Customer.Register(request.Name, okEmail.Value);
        await _customers.Add(customer, cancellationToken);
        await _uow.SaveChanges(cancellationToken);

        return new Ok<CreateCustomerResponse>(
            new CreateCustomerResponse(customer.Id, customer.Name, customer.Email.Value));
    }
}
```

Host endpoint: resolve `ICreateCustomerRequestHandler`, call `Handle`, map with the shared HTTP helper from **`error-handling`**.

## Target without repositories

If the repo already uses DbContext in Application (Monetis-style), the handler may take `AppDbContext` instead of `ICustomerRepository` / `IUnitOfWork`. Prefer ports for **new** external integrations.

## Natural uniqueness (idempotency-ish)

Second `CreateCustomer` with the same email → unique index or explicit exists check → `Conflict`, not a duplicate row. No idempotency-key table required for this case.

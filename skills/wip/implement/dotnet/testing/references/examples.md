# Testing sketches

## Method naming

```csharp
public class CreditCardTests
{
    [Test]
    public async Task AddTransaction_Should_DecrementAvailableLimit_When_SettledExpenseIsAdded()
    {
        var card = CreateCard(limit: 5000m);
        card.AddTransaction(CreateExpense(200m, settled: true));

        await Assert.That(card.AvailableLimit.Amount).IsEqualTo(4800m);
    }
}
```

## Unit: substitute a port

```csharp
public class CreateCustomerRequestHandlerTests
{
    [Test]
    public async Task Handle_Should_ReturnConflict_When_EmailAlreadyExists()
    {
        var customers = Substitute.For<ICustomerRepository>();
        customers.ExistsByEmail(Arg.Any<Email>(), Arg.Any<CancellationToken>())
            .Returns(true);

        var handler = new CreateCustomerRequestHandler(customers, /* … */);
        var result = await handler.Handle(new CreateCustomerRequest("Ada", "ada@example.com"), CancellationToken.None);

        await Assert.That(result).IsTypeOf<Conflict>();
    }
}
```

## Architecture (sketch)

```csharp
[Test]
public async Task Application_Should_NotReference_Infrastructure()
{
    var result = Types.InAssembly(application)
        .ShouldNot()
        .HaveDependencyOn("…Infrastructure")
        .GetResult();

    await Assert.That(result.IsSuccessful).IsTrue();
}
```

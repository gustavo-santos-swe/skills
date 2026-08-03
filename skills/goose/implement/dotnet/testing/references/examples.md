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

## Flaky — don’t / do

```csharp
// Don't
await Task.Delay(500); // hoping the side effect finished
Assert.That(DateTime.UtcNow - started).IsLessThan(…); // wall clock

// Do — fake clock when time matters
var time = new FakeTimeProvider();
time.SetUtcNow(DateTimeOffset.Parse("2026-01-15T12:00:00Z"));
var handler = new ExpireOffersHandler(time, /* … */);
time.Advance(TimeSpan.FromDays(8));
var result = await handler.Handle(…, CancellationToken.None);
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

## Mutation (Stryker) — Unit projects

Point Stryker at Domain / Application projects exercised by `*.Tests.Unit`. Set `break-at` (or equivalent) to the repo’s minimum score in CI so PRs fail when too many mutants survive.

Run in the pipeline, or when a human asks. Do not run mutation in the default local verify loop. It is slow.

```bash
# Illustrative — exact CLI/config lives in the target repo
dotnet tool run dotnet-stryker --config-file stryker-config.json
```

Do not mutate Integration/Testcontainers projects on every PR.

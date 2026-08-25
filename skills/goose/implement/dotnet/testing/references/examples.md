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

Point Stryker at Domain / Application projects exercised by `*.Tests.Unit`. Set `thresholds.break` (or `--break-at`) to the repo’s minimum score in CI so PRs fail when too many mutants survive.

Run in the pipeline, or when a human asks. Do not run mutation in the default local verify loop. It is slow.

```bash
dotnet tool restore
dotnet tool run dotnet-stryker --config-file stryker-config.json
# Second pass when Unit references multiple production projects:
dotnet tool run dotnet-stryker --config-file stryker-config.application.json
```

```json
{
  "stryker-config": {
    "solution": "../../../app.sln",
    "project": "MyApp.Domain.csproj",
    "test-runner": "mtp",
    "thresholds": { "high": 80, "low": 50, "break": 50 },
    "ignore-methods": ["*Log*", "ToString", "*Exception.ctor"]
  }
}
```

Stryker.NET (through at least 4.16) expects a classic **`.sln`**. If the repo’s day-to-day solution is `.slnx`, keep a generated/hand-maintained `.sln` for mutation until Stryker supports XML solutions.

TUnit (and other MTP-only runners) need `"test-runner": "mtp"` — without it Stryker reports zero tests. MTP coverage analysis is still coarser than VsTest (may run more of the suite per mutant).

Do not mutate Integration/Testcontainers projects on every PR.

## Greenfield CI sketch (PR gates)

```yaml
jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
      - run: dotnet restore app.slnx
      - run: dotnet build app.slnx --no-restore
      - run: dotnet format app.slnx --verify-no-changes --no-restore
      - run: dotnet test src/...Tests.Unit/... --no-build
      - run: dotnet test src/...Architecture.Tests/... --no-build
      - run: dotnet test src/...Tests.Integration/... --no-build  # Docker on runner

  mutation:
    needs: backend
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
      - run: dotnet tool restore
      - run: dotnet tool run dotnet-stryker --config-file src/.../stryker-config.json
```

Integration needs Docker; mutation is a separate blocking job because it is slow.

## Integration (Testcontainers) — one session container

Document the isolation strategy in the Integration project (`README` or comment): one Postgres per session, migrate once, unique keys per test (or truncate). Never point at shared staging/prod.

import {
  Callout,
  Card,
  CardBody,
  CardHeader,
  Code,
  Divider,
  Grid,
  H1,
  H2,
  H3,
  Pill,
  Row,
  Spacer,
  Stack,
  Stat,
  Table,
  Text,
  useHostTheme,
} from "cursor/canvas";

/**
 * pr-review canvas TEMPLATE (sample data).
 * Agents: copy to `pr-<n>-review.canvas.tsx`, replace the `review` object.
 * Keep section order and label strings identical every time.
 */

type Verdict = "Approve" | "Comment" | "Request changes";
type Severity = "Block" | "Should-fix" | "Nit";
type Axis =
  | "correctness"
  | "spec"
  | "security"
  | "tests"
  | "guidelines"
  | "ship"
  | "ci";

type Finding = {
  axis: Axis;
  location: string;
  text: string;
};

type WalkStep = {
  step: number;
  bucket: string;
  paths: string;
  why: string;
};

/** Replace this object per PR. Do not rename keys. */
const review = {
  prNumber: 42,
  title: "feat(orders): guest checkout slice",
  repo: "acme/api",
  verdict: "Request changes" as Verdict,
  ci: "pass - 12 checks",
  sot: "docs/plans/2026-07-20-guest-checkout.md + openapi/orders.yaml",
  summary:
    "Adds guest cart to order path end-to-end. Core flow looks sound; one authz gap on order read and a missing integration test for payment failure block merge.",
  structureLines: [
    "Modular .NET: Domain / Application / Infrastructure / Api host",
    "OpenAPI under openapi/; EF in Infrastructure",
    "Integration tests via WebApplicationFactory",
  ],
  walk: [
    {
      step: 1,
      bucket: "Domain",
      paths: "Orders/Domain/Order.cs, Orders/Domain/Cart.cs",
      why: "No deps - confirm invariants before trusting callers",
    },
    {
      step: 2,
      bucket: "Application",
      paths: "Orders/Application/CheckoutGuest.cs",
      why: "Use-case orchestration and ports",
    },
    {
      step: 3,
      bucket: "Infrastructure",
      paths: "Orders/Infrastructure/OrderRepository.cs",
      why: "Persistence mapping vs domain",
    },
    {
      step: 4,
      bucket: "Host / API",
      paths: "Api/Endpoints/OrdersEndpoints.cs",
      why: "HTTP surface vs OpenAPI",
    },
    {
      step: 5,
      bucket: "Tests",
      paths: "Orders.IntegrationTests/CheckoutTests.cs",
      why: "Main-path coverage after behaviour is clear",
    },
  ] satisfies WalkStep[],
  walkWhy:
    "Bottom-up: domain first, then application, adapters, HTTP, tests. Avoid reviewing the endpoint before the invariant it claims to enforce.",
  blocks: [
    {
      axis: "security",
      location: "Api/Endpoints/OrdersEndpoints.cs:88",
      text: "GET /orders/{id} returns any order id without ownership check (IDOR on guest upgrade path).",
    },
    {
      axis: "tests",
      location: "Orders.IntegrationTests/",
      text: "Payment failure path has no integration test; only happy path covered.",
    },
  ] satisfies Finding[],
  shouldFix: [
    {
      axis: "spec",
      location: "openapi/orders.yaml vs Endpoints",
      text: "Spec says 402 on failed payment; handler returns 400 with generic body.",
    },
  ] satisfies Finding[],
  nits: [
    {
      axis: "guidelines",
      location: "CheckoutGuest.cs:40",
      text: "Magic timeout 30 - prefer a named constant if it stays.",
    },
  ] satisfies Finding[],
  axesClear: "correctness, ship, ci - nothing high-signal",
  nextLines: [
    "Author: pr-iterate on Block items",
    "Optional: security-check on Orders endpoints",
    "Post to GitHub? Suggest: request changes",
  ],
};

function verdictTone(v: Verdict): "success" | "warning" | "deleted" {
  if (v === "Approve") return "success";
  if (v === "Request changes") return "deleted";
  return "warning";
}

function FindingsTable({
  title,
  severity,
  rows,
}: {
  title: string;
  severity: Severity;
  rows: Finding[];
}) {
  if (rows.length === 0) return null;
  const pillTone =
    severity === "Block"
      ? "deleted"
      : severity === "Should-fix"
        ? "warning"
        : "neutral";
  return (
    <Card>
      <CardHeader trailing={<Pill tone={pillTone}>{severity}</Pill>}>
        {title}
      </CardHeader>
      <CardBody style={{ padding: 0 }}>
        <Table
          headers={["Axis", "Location", "Finding"]}
          columnAlign={["left", "left", "left"]}
          rows={rows.map((r) => [r.axis, r.location, r.text])}
          rowTone={rows.map(() =>
            severity === "Block"
              ? "danger"
              : severity === "Should-fix"
                ? "warning"
                : undefined,
          )}
        />
      </CardBody>
    </Card>
  );
}

function WalkRow({ step }: { step: WalkStep }) {
  return (
    <Row gap={12} align="start">
      <Pill tone="info" size="sm">
        {String(step.step)}
      </Pill>
      <Stack gap={2} style={{ flex: 1, minWidth: 0 }}>
        <Text weight="semibold">{step.bucket}</Text>
        <Code>{step.paths}</Code>
        <Text size="small" tone="secondary">
          {step.why}
        </Text>
      </Stack>
    </Row>
  );
}

function StructureList({ lines }: { lines: string[] }) {
  return (
    <Stack gap={4}>
      <H3>Inferred structure</H3>
      <Text size="small">{lines[0] ?? ""}</Text>
      {lines[1] ? <Text size="small">{lines[1]}</Text> : null}
      {lines[2] ? <Text size="small">{lines[2]}</Text> : null}
      {lines[3] ? <Text size="small">{lines[3]}</Text> : null}
      {lines[4] ? <Text size="small">{lines[4]}</Text> : null}
    </Stack>
  );
}

function NextList({ lines }: { lines: string[] }) {
  return (
    <Stack gap={6}>
      <H2>Next</H2>
      <Text>{lines[0] ?? ""}</Text>
      {lines[1] ? <Text>{lines[1]}</Text> : null}
      {lines[2] ? <Text>{lines[2]}</Text> : null}
      {lines[3] ? <Text>{lines[3]}</Text> : null}
    </Stack>
  );
}

export default function PrReviewTemplate() {
  const d = review;
  const w = d.walk;

  return (
    <Stack gap={20} style={{ padding: 20, maxWidth: 960 }}>
      <Stack gap={8}>
        <Text
          size="small"
          tone="tertiary"
          style={{ letterSpacing: 0.08, textTransform: "uppercase" }}
        >
          PR review
        </Text>
        <H1>
          {d.repo}#{d.prNumber}: {d.title}
        </H1>
        <Row gap={8} align="center" wrap>
          <Pill tone={verdictTone(d.verdict)}>{d.verdict}</Pill>
          <Text size="small" tone="secondary">
            CI: {d.ci}
          </Text>
        </Row>
        <Text size="small" tone="secondary">
          Spec / SoT: {d.sot}
        </Text>
      </Stack>

      <Grid columns={3} gap={12}>
        <Stat
          value={String(d.blocks.length)}
          label="Block"
          tone={d.blocks.length ? "danger" : "success"}
        />
        <Stat
          value={String(d.shouldFix.length)}
          label="Should-fix"
          tone={d.shouldFix.length ? "warning" : undefined}
        />
        <Stat value={String(d.nits.length)} label="Nit" />
      </Grid>

      <Divider />

      <Stack gap={6}>
        <H2>Summary</H2>
        <Text>{d.summary}</Text>
      </Stack>

      <Card>
        <CardHeader>Human review guide</CardHeader>
        <CardBody>
          <Stack gap={14}>
            <StructureList lines={d.structureLines} />

            <Stack gap={10}>
              <H3>Suggested read order</H3>
              {w[0] ? <WalkRow step={w[0]} /> : null}
              {w[1] ? <WalkRow step={w[1]} /> : null}
              {w[2] ? <WalkRow step={w[2]} /> : null}
              {w[3] ? <WalkRow step={w[3]} /> : null}
              {w[4] ? <WalkRow step={w[4]} /> : null}
              {w[5] ? <WalkRow step={w[5]} /> : null}
              {w[6] ? <WalkRow step={w[6]} /> : null}
              {w[7] ? <WalkRow step={w[7]} /> : null}
            </Stack>

            <Callout tone="info" title="Why this order">
              {d.walkWhy}
            </Callout>
          </Stack>
        </CardBody>
      </Card>

      <Stack gap={10}>
        <H2>Findings</H2>
        <FindingsTable
          title="Must fix before merge"
          severity="Block"
          rows={d.blocks}
        />
        <FindingsTable
          title="Should fix"
          severity="Should-fix"
          rows={d.shouldFix}
        />
        <FindingsTable title="Nits" severity="Nit" rows={d.nits} />
      </Stack>

      <Text size="small" tone="tertiary">
        Axes clear: {d.axesClear}
      </Text>

      <Divider />

      <NextList lines={d.nextLines} />

      <Spacer height={8} />
      <Text size="small" tone="quaternary">
        Template sample with fictional data. Copy, rename to
        pr-N-review.canvas.tsx, replace the review object. Not a real review.
      </Text>
    </Stack>
  );
}

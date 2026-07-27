# Before / after examples

## Throat-clearing + binary contrast

**Before:**
> Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in.

**After:**
> Building products is hard. Technology is manageable. People aren't.

## Chatbot + significance inflation

**Before:**
> Certainly! Acme Analytics, a vibrant startup nestled in the heart of Boulder's thriving tech ecosystem, has secured $40M in Series B funding, marking a watershed moment for the observability landscape. Experts believe Acme is poised to disrupt the market. In conclusion, the future looks bright!

**After:**
> Acme Analytics raised a $40M Series B. The Boulder startup builds an observability platform with sub-second queries and integrations into existing stacks.

## Diff-anchored comment

**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.

**After:**
> Uses a hash map for O(1) lookups instead of naive O(n²) iteration.

## ADHD / density (chat)

**Before:**
> Great question! Let me think about this. Your auth flow has a few moving pieces: the middleware, the token verification, and the cookie handling. Looking at `src/auth.ts`, the `verifyToken` function (around lines 42-58) seems to be using an older API. One approach would be to update the package and rewrite that function. After making the change, you'd want to run the auth tests. By the way, you might also want to look at your dependency versions overall. Hope this helps!

**After:**
> Run `npm install jsonwebtoken@latest`, then edit `src/auth.ts:42`.
>
> 1. Open `src/auth.ts`
> 2. Replace `verifyToken` (lines 42–58) with the snippet below
> 3. Run `npm test -- auth.spec.ts`
>
> Next: paste the first failing line if a test fails.
>
> Separately: there's also a stale dependency. Want that next?

## PR Briefing (conclusion first)

**Before:**
> This PR carefully introduces several improvements across the checkout landscape, showcasing our commitment to a seamless payment experience while fostering reliability.

**After:**
> Adds PIX checkout so BR users can pay without a card.

## Fingerprints + CoT leak

**Before:**
> You're asking about retries. Let me think step by step. First, consider idempotency [INSERT DETAIL]. See https://example.com/docs?utm_source=chatgpt.com

**After:**
> Retries need an idempotency key on the webhook handler. Docs: https://example.com/docs

## Bare-NP bullets + meaning-telling

**Before:**
> This represents a broader shift toward excellence:
> - Stable processing efficiency
> - Reliable connection handling
> - Optimized query performance
> - Low error rates
> - Effective resource utilization

**After:**
> Webhook handler acknowledges after persist. p95 handler time stayed under 40ms in staging; failed deliveries stayed under 1% over a 12-hour run.

## False concession + Imagine opener

**Before:**
> Imagine a world where deploys never fail. While our pipeline is impressive, reliability remains a challenge. Interestingly, this could potentially become a pivotal narrative.

**After:**
> Deploy failures still come from flaky migrations. Next: gate `migrate` on the expand/contract checklist before prod.

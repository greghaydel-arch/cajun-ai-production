# Cajun AI — three-batch local completion, October 22, 2026

**REVIEW_PENDING_CHATGPT. Coming-soon/waitlist candidate: CONDITIONAL PASS for independent source review. Full commercial launch: BLOCKED. No release authorized.**

## Baseline and preservation

Expected earlier head: `d73ee7030dff7c1fc5e63cbdc4a949b01a211bff`. Actual clean starting head: `01dba3c44722814fc1a2ba3ee8f766502547df2d`, branch `marketing/20261016-release-truth`. Subsequent asset/accessibility work was present and preserved. One writable executor; no additional agents. The original hardening ZIP's 29 manifest entries were integrity-checked. This batch adds three sequential local commits per repository; exact final SHAs and complete commit/file inventories are in the review ZIP manifest and final handoff.

No TradeBoard application files, real customer records, production accounts, Cloudflare settings, DNS, Access, billing, GitHub branches/PRs, Actions, videos or DOT jobs were modified. Existing draft PRs were not changed; their live status was not freshly queried. No paid resource, cloud build or paid API was requested. Prior reports and original artwork remain intact.

## Completed batches and verified corrections

| Batch | Correction / evidence |
| --- | --- |
| A — artifact boundaries | Cajun's build previously relied on manifest exclusion alone. It now rejects explicit private/draft/full-preview categories and noncanonical/case-variant paths, including Windows aliases of legal.html. Real temporary builds test fail-closed behavior without deleting source evidence. TradeBoard continues explicit asset emission and separate review mode. |
| A — browser boundaries | Both artifacts propose no embedded objects, self-only base URLs, no framing of the marketing site, denied camera/microphone/geolocation, no-referrer and nosniff. Cajun allows no frames; TradeBoard permits only the existing Zoho form origin. Chromium confirmed framing denial using the actual local headers. This is partial CSP hardening, not a claim of comprehensive XSS prevention. No live security policy changed. |
| B — measured loading | Reused original artwork to create smaller display logos and Cajun mobile backgrounds. Original hashes match their baseline. Larger social/desktop assets stay available; this intentionally increases total artifact bytes while reducing bytes requested by typical pages. See measurements below. |
| B — navigation and conversion | Reproduced Cajun drawer remaining open after mobile-to-desktop resize in the original baseline; fixed resize/focus exit, retained Enter/Escape behavior. TradeBoard home now exposes the product journey and Product has an early waitlist CTA. Direct Zoho link persists before, during and after the optional embed; Cajun remains direct-only. |
| C — factual content | Replaced unsupported firsthand tests, ratings, ranking/pricing claims and speculative 2026 assertions in ten articles plus the trend explainer. Claude 3.5 is identified as historical 2024 context; current availability is not promised. Corrected the trailing-stop example: $59 is above a $58.90 trigger, and a stop is not a guaranteed fill. Removed universal profit-factor thresholds and performance-improvement promises. |
| C — usable library / SEO | Homepage article cards now link to real articles; library and About layouts collapse at mobile widths; corrected active-filter contrast. Empty categories redirect to the library. Existing article URLs are preserved. TradeBoard has five unique route descriptions; structured identity data contains no offers/ratings. Legal #tos compatibility anchor retained. Candidate sitemaps are docs-only; all public HTML and headers retain noindex. |

The commercial strategy is unchanged: planned permanent useful Free, planned Pro/Pro+, and first 100 successfully paid Founding Members at $199/year. Waitlist entries reserve nothing; no checkout, payment, account registration or entitlement guarantee is activated. Product scope remains one validated Webull USD equity-fill CSV, historical review and a private text journal. No broker sync, AI, native mobile, advanced reports or execution was enabled or represented as currently available.

## Local validation and limits

| Result | Check / evidence |
| --- | --- |
| PASS | Cajun 10 public-output regression tests, including real allowlisted builds, sentinel/private files, stale output, path aliases, header hold, editorial corrections and retired-category contracts. Final build: 32 files. |
| PASS | TradeBoard TypeScript project check, production Vite build (44 modules), exact 16-file output tests, unique descriptions, canonical routes, fixed WebSite identity, no review/draft markers and a single Zoho destination. JS 204.66 kB / 65.21 kB gzip; CSS 41.95 kB / 8.25 kB gzip. |
| PASS | 93 final local HTML/syntax/asset/link/anchor/HTTP checks, plus browser negative routes and category redirects. Custom server reads actual _headers/_redirects, but approximates Pages behavior. All unknown/private routes tested returned 404; no catch-all SPA fallback. |
| PASS | 134 final Chromium checks across all public page routes at 320/390/768/1366 widths, images, overflow, one h1, noindex, keyboard, mobile menu, article filtering, complete home-product-plans/waitlist journeys and no-script direct signup. Zero page JS errors and zero axe WCAG A/AA-tag violations in the tested set. Additional focused final library/waitlist checks passed after a scoped link-color change. Not full WCAG/screen-reader or cross-browser certification. |
| PASS | Real direct Zoho page GET rendered HTTP 200, the email textbox and Submit button on mobile. No values entered or submission attempted; all non-GET/HEAD requests were prohibited. Observed resource hosts: forms.zohopublic.com and static.zohocdn.com. A first locator expected type=email, but the form's accessible textbox required a label-based locator; the corrected check passed. |
| PASS | Local optional embed lifecycle: absent before request, present only after activation, removable, direct fallback always available. Cajun never requires an iframe. No local signup-success message exists. |
| NOT VERIFIED | Actual embedded Zoho rendering in this final batch, delivery/consent/retention, form cookies and downstream processing. Local journey tests intentionally blocked external resources, including Google Fonts and Zoho. Direct rendering is not proof of embedded rendering or submission delivery. |
| PASS | Bounded Gitleaks scans of final changed-file snapshots, actual public artifacts and the review ZIP payload; no findings. No environment files, private account screenshots, customer data or dependencies included. Legacy full history was not rescanned. |
| NOT VERIFIED | Current hosted SHA/settings, production domains/SSL, historical preview protection, www/apex/pages.dev redirects, edge-injected analytics, hosting request logs, cold provider builds, live latency/Core Web Vitals, all third-party/social links, full accessibility and the actual application release. No cloud validation was triggered. |

Recorded harness issues were corrected without changing product behavior to satisfy tests: a hidden-role locator after resize, a navigation timing assertion before React mounted, and a frame test whose parent CSP blocked the request before the child policy could be observed. The real library contrast defect was fixed. Failed/intermediate evidence is labeled in the review ZIP; final checks are separate.

## Controlled performance comparison

Fresh local browser contexts, same Chrome and viewport, external fonts blocked, no synthetic customer data or external profiling service. These numbers are decoded first-party resource bytes (excluding the document), not WAN timings or Core Web Vitals.

| Journey | Baseline | Final | Reduction |
| --- | ---: | ---: | ---: |
| Cajun home, 390px | 638,941 | 215,010 | 66.3% |
| Cajun home, 1366px | 638,941 | 541,814 | 15.2% |
| TradeBoard home, 390px / 1366px | 445,759 | 278,417 | 37.5% |

Cajun mobile image requests fell from 609,335 to 182,800 bytes; TradeBoard from 200,412 to 31,802. The mobile background is slightly softer at reduced resolution, with the same composition/color and readable foreground; controlled viewport screenshots were visually reviewed. Existing original images were not overwritten. Total artifacts grew from 898,547 to 1,030,868 bytes for Cajun and 717,745 to 725,164 for TradeBoard because multiple size variants and metadata are retained. Do not equate artifact size with per-page delivery.

## Exact hosting proposal — NOT APPLIED

| Project | Required future configuration / verification |
| --- | --- |
| cajun-ai-production | Repository root `/`; build command `python3 scripts/build-site.py`; build output `dist`. Standard-library Python >=3.9 required; local execution used Python 3.14. Verify provider runtime independently. Historical evidence recorded no build command/root output; if that remains true, changing both is mandatory before this candidate can be published. Serving root bypasses every allowlist exclusion. |
| tradeboard-website | Repository root `/`; Node 22.22.2 and locked dependency installation; production command `npm run build`; output `dist`, never `review-dist` or `--mode review`. The old recorded Bun install/build path needs owner-approved reconciliation. Local testing reused installed dependencies, so a clean provider install is not certified. Avoid duplicate automatic/manual install phases when approving the exact pipeline. |
| Both | Preserve production branch main, automatic production deployments enabled, preview branch deployments None, domains/SSL, existing Access and all historical deployments. These are owner-accepted historical settings, not freshly read back in this batch. No Functions/Workers/server/API/paid add-on is required by these static artifacts. Check actual headers, 404s, redirects, canonical host, noindex and draft exclusions only in a separately authorized host validation. |

No proposed settings change, push, merge or build is authorized by this report. A noindex hold is not private access protection. Existing publicly reachable historical previews must not be assumed protected based on this local artifact audit.

## Owner / counsel / provider decisions

1. **Coming-soon data collection:** approve controller/contact details, Zoho form fields/purpose/consent placement, processor/region facts, retention/deletion and withdrawal/unsubscribe procedures. A working form is not permission to collect. Public status notices remain nonbinding and draft legal pages remain source-only.
2. **Third-party exposure:** approve or replace Google Fonts delivery; it remains an external browser request. Approve/disclose actual Zoho and hosting processing and investigate edge-injected analytics/log retention. Optional analytics remain absent from built application code. Verify public company/founder biography with the owner before broader indexing.
3. **Coming-soon publication:** independent ChatGPT source review, then separately authorized GitHub handoff and hosting/output verification. Global noindex stays until a separately approved indexing patch. See the candidate sitemap and rollout plan.
4. **Full commercial launch:** application/provider/recovery certification, legal policies, Free limits and Pro/Pro+ entitlements/prices, Founding Member eligibility/renewal/refund/cancellation, payments and attended acceptance. None are resolved by marketing tests.
5. **Media:** verify one owner-controlled Cajun AI channel ID and approved actual-app screenshots/recordings with synthetic/redacted data. Tutorials and product demos remain planned. Existing illustrative concept is explicitly labeled; no new product UI, review score, subscriber count, testimonial or video was invented.

## Reproduce without cloud work

From Cajun: `python scripts/test-public-output.py`, `python scripts/build-site.py`; optional `node scripts/test-mobile-hero.cjs` with PLAYWRIGHT_MODULE and CHROME_PATH pointing to existing local tools. Nine hero/menu checks passed.

From TradeBoard: `node node_modules/typescript/bin/tsc -b`, `node node_modules/vite/bin/vite.js build`, `node scripts/test-public-output.mjs`. Node 22.22.2 was used. No dependency install or cloud Actions.

The ZIP contains the loopback server, artifact/browser/focused/performance and read-only Zoho test harnesses, exact logs/results, selected before/after screenshots, source snapshots, diffs and SHA-256 manifest. Tool paths reference this Windows workspace; update paths only when reproducing on another machine. Original historical evidence is preserved. This report's final source commit is identified by the package manifest rather than a self-referential SHA.

**Next:** independent ChatGPT source review of the exact two final local heads. Do not release on this agent's verdict.

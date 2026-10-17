# Overnight local completion — 2026-10-16

**REVIEW_PENDING_CHATGPT. Local technical work only; no independent certification or release approval.**

Starting reviewed commit: `d73ee7030dff7c1fc5e63cbdc4a949b01a211bff`. Branch: `marketing/20261016-release-truth`. The exact final commit containing this report is in the review ZIP manifest and final handoff.

Cajun: optimized logo/favicon and WebP backgrounds; originals excluded from the public allowlist. Corrected orange-button and contact-card contrast. Disabled contact form until its mail-draft handler attaches, preventing no-script personal-data GET fallback; added no-script navigation and contact link. Added canonical branded social metadata.

Public artifact before: **6,938,002 bytes**; after: **898,440 bytes** across 32 files (**87.05% reduction**). These are uncompressed artifact bytes, not measured WAN speed or Core Web Vitals. Original source-image hashes were checked unchanged. No asset-quality claim relies only on byte counts.

## Final local verification and evidence

- PASS: Cajun AI six public-boundary regressions and allowlisted build (32 files); TradeBoard TypeScript, production Vite build and exact 15-file public-output checks. Review Vite build remains separate in ignored review-dist and includes the original assets required by preserved review components.
- PASS: 95 filesystem/HTTP checks against final artifacts: HTML structure, asset links, anchors, canonicals, noindex, direct routes, excluded/internal/unknown routes returning 404, legal redirects and single direct Zoho destination. The loopback server approximates Pages aliases/redirects; this is not Cloudflare certification.
- PASS: 96 Chromium checks at 320, 375, 390, 768, 1024, 1366 and 1500 pixels, including 77 page/viewport combinations, image decoding, overflow, heading, UTF-8 text, keyboard skip link, mobile menu Enter/Escape, no-script access and disabled contact fields. TradeBoard embed can load only on explicit request and can be removed; direct fallback persists. No form was submitted. No page JavaScript errors.
- PASS: axe-core WCAG 2 A/AA and 2.1 AA tags on 11 representative pages at 390px: zero reported violations after correcting Cajun buttons/contact-link contrast. This is focused automated testing, not full WCAG conformance or screen-reader certification.
- Screenshots: four new baseline home captures plus 22 final full-resolution captures, mobile 390px and desktop 1366px. The prior 131px evidence is not reused. Third-party fonts were blocked, so these captures show the supported fallback fonts. Background/logo fidelity was visually inspected; source originals remain unchanged.
- NOT VERIFIED: live Cloudflare settings/headers/redirects, third-party form rendering or submission/delivery, actual Google Fonts delivery, real channel identity/videos, other browsers and hosted performance. All non-loopback browser requests were blocked, recorded as blocked, and never counted as successful. Public assets still reference Google Fonts and the same existing Zoho destination.
- No test servers remained listening on the task ports after teardown. No dependency installation, app-repository modification, GitHub write/Actions, deployment, provider mutation, charge, actual email or waitlist submission occurred.

Reproduce with existing tools: Cajun `python scripts/test-public-output.py` then `python scripts/build-site.py`; TradeBoard `node node_modules/typescript/bin/tsc -b`, `node node_modules/vite/bin/vite.js build`, `node scripts/test-public-output.mjs`. Optional preserved review check: `node node_modules/vite/bin/vite.js build --mode review`. Node 22.22.2 was used. The review ZIP includes browser.cjs, artifact-check.cjs, check-artifacts.cjs, serve-artifact.py and optimize-assets.py with commands in its README. Image derivation uses the already installed Pillow library; it is not a website runtime dependency. No new framework/service is introduced.

## Owner/counsel decision packet — no legal approval granted

| Actual boundary | Required decision / outstanding evidence |
|---|---|
| Website delivery through Cloudflare | Confirm controller/operator details, applicable hosting terms, request-log access/retention and any edge-injected analytics. No assertion that the provider collects nothing. |
| Remote Google Fonts on page load | Requests expose normal connection/browser metadata to Google. Decide whether to approve/disclose this vendor or authorize future font self-hosting after license/source review. No optional analytics scripts are included in these artifacts. |
| Zoho waitlist link; TradeBoard optional embed | One existing form destination. Loading contacts Zoho; submitting sends entered data to its operator. Confirm current fields, processors/region, cookies/anti-abuse behavior, purpose (launch updates), consent/notice placement, withdrawal/unsubscribe, retention period and deletion procedure before collecting data through this candidate. No invented retention or contractual guarantee. |
| Cajun contact helper | Name/email/message stay in the browser until the visitor opens and sends an email draft. The email app and receiving mailbox process sent content. Approve the contact notice, mailbox access/deletion procedure; discourage credentials and trading records. Without JavaScript the helper stays disabled and a direct mail link remains. |
| Cookies/storage | No new first-party tracking or consent platform was added. Third-party form cookies and hosting behavior require owner/provider verification. Do not interpret blocked-request tests as cookie certification. |
| Plans | Permanent useful Free, planned Pro/Pro+, proposed $199/year for first 100 successfully paid Founding Members remain. No guarantee, allocation/reservation, live Checkout or automatic entitlement; final prices/benefits/renewal/refund terms still need commercial/legal approval. |

## Exact proposed hosting checkpoint — NOT APPLIED

Both existing Pages projects: production branch **main**, preview deployments **None**, repository root `/`, output **dist**. Keep current Access/security/DNS settings unchanged and preserve noindex in HTML and `_headers`. No Functions, Workers, API, database binding or paid service is needed. Do not deploy review-dist or repository root. Keep built root 404.html; no catch-all SPA rewrite. Validate direct routes, old legal redirects, www/apex/pages.dev behavior and noindex on the actual host only after explicit publication/hosting authorization.

- Cajun AI build command: `python3 scripts/build-site.py` (standard-library Python >=3.9; proposed pinned provider version 3.12). Serving repository root is a release blocker because it bypasses the allowlist and includes draft/review material.
- TradeBoard build command proposal: `npm ci --ignore-scripts --no-audit --no-fund && npm run build`, Node **22.22.2**, output **dist**, never `--mode review`. Local validation used existing locked dependencies; clean provider installation is NOT VERIFIED. Replace the historically recorded Bun build only with separate owner approval; avoid duplicate automatic dependency installs during that configuration review.
- Keep Pages default caching rather than adding aggressive cache rules for mutable filenames. Hashed Vite assets and resized images need no new service. Cloudflare documents HTML normalization and root-404 behavior, but local tests do not prove provider configuration: https://developers.cloudflare.com/pages/configuration/serving-pages/ ; build settings: https://developers.cloudflare.com/pages/configuration/build-configuration/ ; headers: https://developers.cloudflare.com/pages/configuration/headers/ .

## Later real-media workflow

Use the existing single Cajun AI video hub. After approved application UI and separately authorized capture: launch the existing local synthetic application, record the import/history/journal/analytics workflow, inspect every frame for identifiers/secrets, create readable desktop/mobile captures with captions, obtain product/legal review, then add only verified owner-controlled channel/video IDs. No invented screenshots, testimonials, performance figures or new channel. Existing labeled illustrative concept remains labeled; no completed tutorial is claimed.

## Remaining release gates

Independent ChatGPT review; owner/counsel decisions above; separately approved GitHub publication and hosting/output verification (including cost approval if any cloud build/Actions could run). No current production authorization. Prior provider snapshots are historical, not fresh live facts. This local technical completion does not approve legal terms, data collection, production or deployment.

---
The earlier hardening report below is retained as historical evidence; this section supersedes its asset sizes and this batch's test status.

# Cajun AI — local release hardening, 2026-10-16

**Recommendation: CONDITIONAL PASS for independent source review. Production release remains blocked by the approvals below.**

Baseline: `2e067b158ef54d6e9a455ed272d4ba320135d26c` on `marketing/20261016-release-truth`.
Existing draft: https://github.com/greghaydel-arch/cajun-ai-production/pull/1

## Corrections delivered

- `scripts/build-site.py` now reads the explicit 32-file `scripts/public-files.json`
  allowlist. It does not recursively copy pages/assets. Draft `pages/legal.html`,
  `preview.html`, all three `*-full.html` pages, docs, source tools and arbitrary new
  assets are excluded. Existing review sources are retained. Missing/unsafe input
  fails before replacing prior output.
- Added `pages/legal-status.html`, `404.html`, `_headers` and narrow `_redirects`.
  Public legal links use status labels, not purported effective policies. Removed
  public session-storage redirects into full review pages. No client flag is
  relied on as a release security boundary.
- `pages/tradeboard.html` explains initial scope and adds prominent launch-update,
  pricing and cross-site paths. `pages/pricing.html` restores the planned Pro tier
  alongside Free, Founding Member and Pro+, with explicit no-reservation language.
- Cajun AI uses direct-only Zoho access after its optional iframe failed to render
  reliably in local browser checks. Form access needs neither an iframe nor JavaScript.
  `script.js` normalizes active navigation across HTML/extensionless paths. `styles.css` adds responsive cards and
  improves the new CTA/privacy-link contrast and anchor offset using existing colors.
- Public page edits outside those journeys only update legal destinations, waitlist
  navigation, canonical normalization and the prelaunch indexing hold. Existing
  editorial material and illustrative home concept remain; no new mock interface was made.

## Reproduce locally

```text
python scripts/test-public-output.py
python scripts/build-site.py
python -m http.server 4174 --bind 127.0.0.1 --directory dist
```

**PASS:** four boundary tests exercise real builds with unlisted/private/stale fixtures,
exact output inventory, missing input and traversal rejection. Final output: 32 files.
Full local HTTP/HTML/link evidence is in `artifact-results.json` in the review ZIP.
The loopback artifact test server also checks extensionless aliases and the explicit
legacy legal redirects; Python's basic server alone does not implement Cloudflare rules.

**Hosting blocker:** prior evidence says Cloudflare serves the repository root with
no build command. That configuration would bypass this isolation entirely. The
future approved configuration must use `python3 scripts/build-site.py`, output
`dist`; validate available Python and actual hosted behavior separately. No setting
was changed or freshly inspected in this local batch.

## Focused certification

| Check | Result | Evidence / limit |
|---|---|---|
| Artifact HTML, JavaScript syntax, internal links, anchors, images, route documents and metadata | PASS | 95 combined filesystem/HTTP checks in the accompanying review ZIP; no failed checks. Includes HTML structural/accessibility rules. |
| Internal source, private previews and legal drafts absent from public output | PASS | Exact artifact inventories, negative-content assertions and HTTP 404 checks. Legal compatibility links on Cajun AI redirect only to the status page. |
| Desktop and mobile journeys | PASS | Chrome at 1516×900 and 390×844: public home/product/plans/waitlist paths, no horizontal page overflow; new controls have accessible names and visible keyboard focus. Cajun mobile menu opens with Enter and closes with Escape. |
| Direct Zoho waitlist | PASS | Existing form renders its email input and Submit button. No values entered or registrations submitted. Both websites use the same destination. |
| Final direct and optional embedded paths | PASS | TradeBoard has no iframe before activation; its optional embed rendered the actual input and Submit button on desktop and mobile. Earlier attempts remained blank. Cajun AI now uses direct-only access after its optional embed failed to render reliably in this environment. Direct links remain available; no local success state is invented. Third-party availability is not guaranteed. |
| Privacy before embed activation | PASS | No Zoho frame/resource observed before activation. Optional analytics scripts absent from built artifacts. Google Fonts remains an external request and is disclosed. Duplicate Google Fonts CSS import removed from TradeBoard. This does not certify third-party form internals or hosting-injected scripts. |
| Console/runtime errors | PASS | No warnings/errors observed in final tested first-party pages. Browser automation encountered screenshot/input timeouts; viewport captures and keyboard checks were used. These are not presented as successful embed rendering. |
| Secret/sensitive-data review | PASS | Final staged source, generated artifacts and reports scanned locally with Gitleaks plus private-data/filename checks; review package is separately scanned. Prior full-history evidence is preserved; the entire legacy dependency history was not rescanned. |
| Cloudflare configuration / hosted behavior | NOT VERIFIED in this batch | No provider access or changes. Prior evidence records preview deployments None, production main with automatic deployments enabled. These are historical assumptions, not fresh verification. |
| Submission delivery, email processing, account registration and billing | NOT VERIFIED | Intentionally not exercised or activated. |
| Complete WCAG certification, other browsers and live application acceptance | NOT VERIFIED | Focused website checks only; not a full repeat audit or an application certification. |

## Product truth and privacy boundaries

Read-only application reference: commit `91cedab72c90e591d849c327f7bbcc776b44c005`,
`backend/src/config/firstRcReleaseManifest.js` and `backend/src/services/batch2ImportService.js`.
The supported initial format is `webull-csv-v1`: USD STK/EQUITY BUY/SELL FILLED rows,
with preview and confirmation. Initial historical FIFO review and private text journaling
do not establish support for all Webull exports, broker sync, live balances, AI, mobile
apps, advanced reports or execution. No application code or data was changed.

Both journeys preserve a planned permanent useful Free tier, planned Pro and Pro+
upgrades, and the first 100 successfully paid Founding Members at $199/year.
Waitlist entries never reserve slots. There is no checkout, account registration,
remaining-spots counter, new testimonial, invented product screenshot or video.
The Cajun AI tutorial hub remains the single channel destination; actual channel
ownership/ID and recordings are not verified and were not invented.

Public status wording is nonbinding and explicitly pending approval. Draft legal
documents remain source-only. The earlier legal discrepancy report in
`WEBSITE_RELEASE_VALIDATION_2026-10-16.md` remains applicable; this batch does not
approve processor contracts, retention/deletion commitments, security guarantees,
refunds or subscription terms. Zoho receives submitted information; its resources
can contact additional processors. Google Fonts is still loaded remotely. Cajun's
existing contact form opens a mail draft; it does not verify delivery.

## SEO recommendation — owner decision, not activated indexing

Keep this candidate's HTML robots meta and `_headers` noindex hold until legal,
hosting and independent source review gates pass. Do not use robots disallow as
privacy protection. After approval, index only useful reviewed marketing/editorial
pages; keep waitlist/status/404 and unfinished category pages noindex. Generate an
allowlisted sitemap only then. Verify search rendering before requesting indexing.
Canonical destinations are Cajun AI's apex domain with extensionless HTML paths,
and TradeBoard's apex domain with physical directory routes. Cross-site product
and tutorial links retain their respective canonical brands. A future owner-approved
host review must verify www/apex and pages.dev handling, direct deep links, real
404 responses, noindex headers and any analytics injected at the edge.

Cloudflare's [documented route and 404 behavior](https://developers.cloudflare.com/pages/configuration/serving-pages/)
is the design basis: `.html` paths normalize to extensionless URLs, and a root
`404.html` prevents implicit SPA fallback. Local HTTP evidence is not provider certification.

## Decisions still required

1. **Before collecting visitor data through this candidate:** owner/counsel approval
   of the Zoho waitlist notice, purposes, retention/deletion process and processor
   disclosures, including the Google Fonts decision. A form's generic abuse warning
   is not a substitute for the operator's approved notice.
2. **Before release:** independent ChatGPT source review, separate authorization
   for any push, and a separately approved hosting/output/route validation. Existing
   public preview protection and old deployments remain unchanged and outside this batch.
3. **Before paid launch:** confirm Free limits, Pro/Pro+ entitlements/prices, Founding
   Member eligibility, renewals, refunds and cancellation, and separately approve
   payment/application release gates. These are not activated by this website.

Approved real UI screenshots and the Cajun AI channel ID/recordings are later media
gates; clearly labeled pending media need not block a narrowly approved waitlist-only launch.

No pushes, PR updates, CI, Cloudflare mutations, deployment, payment/API activation,
video publication, subscription, DOT or monitoring occurred. Existing PRs were not
modified; their last verified state was OPEN/DRAFT. Prior validation evidence is preserved.

## Review handoff

The local checkpoint containing this report is the review target; the accompanying
ZIP manifest records its exact SHA and baseline. The ZIP contains full Git diffs,
this report, focused test evidence and before/after screenshots, excluding account
screenshots, credentials, raw private QA and dependency trees. Inspect the changes
and reproduce local checks before authorizing a separate GitHub handoff.

**REVIEW_PENDING_CHATGPT — no website release authorized.**

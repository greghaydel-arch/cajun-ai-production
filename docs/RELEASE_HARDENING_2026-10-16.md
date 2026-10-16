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

# Cajun AI website completion and release validation

**Date:** October 16, 2026 (America/Chicago)
**Status:** `REVIEW_PENDING_CHATGPT` — release not authorized; unresolved integration/legal/access gates remain.

## Executive summary and Git handoff

Preserved the existing Cajun AI design; corrected remaining product/pricing/import claims, centralized waitlist conversions, removed false signup/contact/newsletter behavior, completed the four-series/six-topic video hub, fixed legal anchors/keyboard controls, metadata, landmarks and mobile overflow. Legal text remains explicitly a review draft.

- Repository: `greghaydel-arch/cajun-ai-production`; existing draft [PR #1](https://github.com/greghaydel-arch/cajun-ai-production/pull/1).
- Branch: `marketing/20261016-release-truth`. Implementation through commit: `66f88a2cdc88cec53b42117480d263143ca1f6d4` (all task commits prefixed `[CF-Pages-Skip]`). This report is a subsequent documentation-only commit; its exact local head is available in normal Git history. New commits have not been pushed and the existing PR description has not been updated under the owner hold.
- Companion implementation: Cajun AI `66f88a2cdc88cec53b42117480d263143ca1f6d4`; TradeBoard marketing `7ee7bf6269a8fb0f96334bea1cc348f6bbed5def`. Both PRs remain open drafts and unmerged at their original remote heads; all new task commits are local only.
- No independent-review PASS or production-ready verdict is issued. Earlier preview deployments predate this work; no new deploy is authorized.

## Owner hold and verified hosting configuration

The owner's later instruction explicitly requires **no additional pushes/remote commits** until hosting controls are reviewed and approval is given. That instruction overrides the earlier planned use of a commit-message skip prefix. No task commit was pushed; no PR description or provider setting was changed. The existing draft PRs therefore do not yet contain the new implementation or this report. Local implementation and validation are preserved on the requested branches.

Read-only branch-control dialogs in **both projects** show:

- Production branch: `main`; “Enable automatic production branch deployments” checked.
- Preview branch: **All non-Production branches** selected; `None` and `Custom branches` available, neither selected.
- Existing marketing branch previews are public: unauthenticated GET returned HTTP 200 and the website title for both branch aliases, with no Cloudflare Access login redirect. TradeBoard's hash preview also returned 200. Cajun AI's hash URL had a transport failure in that probe, so that one hash URL is NOT VERIFIED; its branch alias establishes public access.
- Domain associations: Cajun AI `cajun-ai.com` and `www.cajun-ai.com`; TradeBoard marketing `trade-board.net`. Custom-domain tabs show all three bindings Active with SSL enabled. These map to the respective Pages projects above. Do not infer that the app's staging origin is the marketing domain.

Recommended bounded owner-approved change: in **each** Pages project's Settings → Build → Branch control, choose **Custom branches**, retain the intended preview include pattern (`*` if retaining all other existing previews), and exclude exactly `marketing/20261016-release-truth`. Alternatively choose `None` only if the owner wants all automatic previews stopped. Leave production `main`, production automatic-deploy behavior, domains, DNS, build settings and credentials unchanged. This is a recommendation, not permission or an executed change. Re-open both dialogs and verify the saved exclusions before requesting permission to resume review-branch pushes.

Stopping new preview builds does **not** make existing preview URLs private or remove their content. If they contain private review material, owner/security approval is separately needed to configure Cloudflare Access for preview hosts (including existing aliases/hash URLs); production/custom-domain protection is a separate scope. No existing deployment was removed and no access policy was changed. Public GitHub source also remains public.

Required approval before continuing remote work: owner approval for the exact per-project branch exclusions (or the broader `None` choice), followed by verification and explicit resumption of pushes. ChatGPT independent review, legal approval and production release approval remain separate. Do not use `[CF-Pages-Skip]` to bypass the owner's current no-push instruction.

## Tests performed

Environment: Windows PowerShell, Node 24.17.0, npm 11.13.0; isolated checkout; Python static server bound to `127.0.0.1:4174`; installed QA-only HTML Validate 11.16.2 outside the repository; real Chrome browser. Desktop viewport 1440×900; mobile 390×844 (content width 375px with scrollbar). No app/customer database used.

| Test | Result | Evidence / limit |
| --- | --- | --- |
| HTML structural syntax | PASS | All 27 source HTML pages; selected close-order, permitted-content/parent, duplicate-ID/attribute, quotes, doctype and basic image/form rules. Existing body styles moved into heads. This is not full HTML/WCAG certification. |
| JavaScript syntax | PASS | `node --check script.js`; every inline/external script compiled with Node `vm.Script`, event handlers parsed. |
| Internal links/assets/anchors | PASS | All local HTML link/file/fragment targets checked, including actual `#tos`/`#privacy` IDs and `#tradeboard`. No empty `#` CTA retained. |
| Local HTTP pages/assets | PASS | 32 unique pages/local stylesheet/script/image/background resources: HTTP 200, nonempty bodies, asset MIME checked against accidental HTML fallbacks. |
| Desktop/mobile routes | PASS | All 27 HTML documents covered in browser route checks; full pricing/product previews additionally inspected with local-only cosmetic flags. No final horizontal page overflow or broken/pending images on repaired routes. |
| Responsive regression | PASS | Repaired 489px-wide comparison table in 375px content viewport using a keyboard-focusable scrolling region; repaired missing landmarks in 3 stubs/contact. |
| Basic accessibility/keyboard | PASS | Heading/main/labels, image alternatives, skip targets; mobile menu open/close and Escape; legal tab ArrowLeft/End and selected state. All tested interactive labels remain visible/accessible. |
| Full screen-reader, contrast audit, Firefox/Safari | NOT VERIFIED | Chrome basic checks are not WCAG conformance or cross-browser certification. |
| Legal-page navigation | PASS | Terms deep link activates Terms; arrow/Home/End controls and hash-change handling implemented. Draft notice is visible; policy approval remains outstanding. |
| Video hub navigation | PASS | Four series, six topics, internal links and `#tradeboard` checked locally; no guessed YouTube channel/embed. |
| Cross-site production tutorial anchor | FAIL | Existing production Cajun AI page has no `#tradeboard`; corrected local source does. Requires controlled release, not a link guessed to another channel. |
| Waitlist direct destination/fallback | PASS | Correct public Zoho form title/field/button rendered; source URLs identical across sites; no customer submission. |
| Iframe rendering consistency/time-to-ready | NOT VERIFIED | Both sites rendered the form, but repeat blank frames and later population were observed; reliable timing was not established. |
| Submission/receipt/notification | NOT VERIFIED | Explicitly no fake signup or external account modification. |
| Contact required-field rejection | PASS | Empty form rejected by native validation; no mailto navigation, transmission or success claim. Valid-message delivery was not tested. |
| Newsletter | PASS | Removed nonfunctional subscription control; honest unavailable notice replaces it. |
| Console/runtime checks | PASS | No warning/error entries surfaced in Chrome's captured logs for tested local site routes. Embedded-provider timing/consistency remains separately unverified. |
| SEO metadata | PASS | All 27 pages have title/description/viewport; public pages have canonical URLs, full previews/legal drafts noindex. Search-engine indexing/ranking not tested. |
| External link validation | PASS / FAIL / NOT VERIFIED | Detailed common section records the actual 71-destination results and focused repairs. |
| Preview authentication | FAIL | Cosmetic session flag is not an authentication boundary; no server authentication installed. |
| Host-to-repo mapping | PASS | Existing Cloudflare dashboard/logs read without changes. |
| New-head hosted build/deploy | NOT VERIFIED | Deliberately omitted via documented commit prefix; no deployment authorization. |
| Git whitespace | PASS | `git diff --cached --check` passed. Windows normalization warnings were not source/test failures. |

Static QA read each HTML with JSDOM and HTML Validate, compiled scripts without executing submissions, resolved each relative target/fragment, and checked missing title/description/viewport. External checks used GET with 15-second timeout, redirects and no form data; 403/402/transport failures stayed NOT VERIFIED. Browser checks used real rendered DOM/screenshots, viewport dimensions, image decode/overflow, actual menu/tab interactions and captured console logs. No green status was inferred from an unrun check.

## Scope and source of truth

Owner-authorized website completion only. Existing visual systems and review branches retained. No TradeBoard application source was edited, and no production/database/billing/DNS/credential/channel setting was changed. No signup, mail delivery, video upload, playlist creation, deployment or DOT job was initiated. This is implementation-agent validation, **not independent ChatGPT approval or release authorization**.

Read both existing PRs and their changes, `docs/VIDEO_CHANNEL_HANDOFF.md`, the original Windows continuation/readiness documents, and application release evidence. GitHub read-only verification confirms current application `main` is `91cedab72c90e591d849c327f7bbcc776b44c005`. The release-document blob also matches the local canonical reference. The working application checkout is older and was not used as current implementation truth.

Application evidence at that immutable commit:

- `backend/src/config/firstRcReleaseManifest.js`: first-release exclusions include broker synchronization, live positions/portfolio, billing, AI/credits, replay, psychology, screenshots, backtesting, tax and advanced analytics/reports.
- `backend/src/services/batch2ImportService.js`: `webull-csv-v1`, one schema; BUY/SELL, FILLED records, STK/EQUITY, USD; preview/confirmation and deduplication. This does **not** establish support for every Webull export, other broker formats, options, currencies, OAuth or automatic sync. App runtime acceptance was not rerun in this website task.
- `backend/src/services/firstRcIdentityProvider.js`, `batch1IdentityService.js`, `backend/src/config/runtimeConfig.js`, `secureSessionStore.js`: provider-backed email identity and server-owned sessions; not the websites' cosmetic preview gates.
- `backend/src/services/batch4bJournalService.js`, `batch5aExportService.js`, `batch5bAccountDeletionService.js` and `docs/release/PRODUCTION-READINESS.md`: private journal, exports/deletion, retention and provider limitations.

## Factual legal/privacy discrepancy report — owner and counsel review required

These are source observations and editorial corrections, not legal advice or approved policies. Website drafts must not be released as effective Terms/Privacy. Reconcile the separately held September 28 legal draft; it was not available here. Business registration, regulatory status, age limits, governing law, liability, notice/assent rules, contact ownership and rights language require owner/counsel confirmation.

| Topic | Discrepancy and supported implementation facts | Required decision/evidence |
| --- | --- | --- |
| Authentication/session | Old local-password and brokerage-OAuth descriptions do not describe the invited flow. Current source selects Auth0 email identity with OIDC/PKCE and server PostgreSQL sessions. Source cookie policy is HttpOnly, SameSite=Lax and Secure in managed environments; idle/absolute session limits are implemented. | Actual enabled provider/tenant, cookie behavior and attended login acceptance remain environment-specific and unverified here. An unmerged AWS alternative is not a deployed fact. |
| Collection/storage | Imported execution fields, source-row facts, account/profile/identity/acceptance records, FIFO generations, journal text/tags/drafts and operational/privacy records exist. A bare “trade history only” policy is incomplete. | Approve categories, purpose, access, regions, rights and enabled-vendor inventory; avoid blanket anonymity or no-sharing promises. |
| Import processing | Parser handles raw CSV bytes in memory; normalized execution/source facts and batch/preview metadata persist in PostgreSQL. No broker login is required by this import path. | Do not promise that nothing from an upload is stored or that every logging/crash path creates no copy. Provider/log verification is separate. |
| Third parties | Marketing uses Cloudflare Pages, Google Fonts and Zoho Forms. TradeBoard marketing injects Runable/OneDollarStats analytics (`/runable.js`, events destination `r.lilstts.com`). App source selects Auth0/Zoho transactional delivery and references DigitalOcean PostgreSQL/object storage. | Verify actual vendors, contracts/DPAs, locations, identifiers, consent basis, cookies, access and deletion. Zoho Forms waitlist retention is distinct from Zoho transactional-email retention. |
| AI processing | AI endpoints are disabled in the first invited release. Old GPT-4o quota/inclusion promises were inaccurate. | Before future enablement, approve actual provider, transmitted fields, retention/training terms, user choices and educational-only behavior. No model-behavior guarantee is established. |
| Security | Authorization/session/role controls in source are not a universal encryption or operational-security certification. No field-encryption or instant independent psychology-erasure promise is established. Website preview flags are editable client state. | Verify hosting controls, real tenant/bucket encryption, logs, tests and access protection. Never place private material behind these browser flags. |
| Retention/deletion | Account deletion is asynchronous with retries/receipts and restore suppression. Journal drafts have expiry/cleanup logic. Provider copies, backups, object versions and suppression evidence have separate lifecycles; instant universal erasure is unproven. | Approve a category-specific schedule and exceptions. Release evidence records a category-specific Zoho transactional-log amendment of 60 days; it is not a waitlist, all-record, backup or Auth0 deletion promise. Provider settings and restoration proof remain separate gates. |
| Billing/refunds/cancellation | First-release billing routes are disabled. Marketing's local forms cannot create a paid subscription. Lifetime rates, plan quotas, unrestricted storage, exact cancellation rights and refund guarantees were unapproved. | Preserve planned permanent Free and first-100 Founding Member strategy at $199/year. Final eligibility, renewal, refunds, cancellation and entitlements must be approved and shown before payment. Waitlist entries do not reserve places. |
| Education/advice boundary | Historical analytics/journaling/education only. No execution, personalized buy/sell/hold advice, live signals or predictive entries/exits/stops. | Retain this boundary in future claims, actual recordings and any AI review. Source presence does not establish general release availability. |

## Video and product-media handoff

One Cajun AI channel; no separate TradeBoard channel. Four planned series: How Technology Works; AI Tools, News & Reviews; Software How-To Guides; TradeBoard Tutorials. The legacy handle was not reintroduced. **Channel ownership/URL/stable ID, playlist IDs and approved video IDs: NOT VERIFIED.** No account access was attempted. The historical handoff's monetization figures were not revalidated or repeated as marketing promises.

The hub retains `#tradeboard` and lists all six requested topics: What is TradeBoard?; Getting started; Importing trade history; Understanding the analytics dashboard; Using the trading journal; Reviewing historical trading performance. No card claims a completed video.

The TradeBoard `ProductShowcase` uses static typed capture/tutorial lists and existing card styling. Five screenshot slots cover dashboard, analytics, journal, historical performance and validated import; a sixth slot reserves the short primary demo. All asset/video fields are empty. Existing concept images remain labeled illustrative. Add only captures from approved real application UI, recorded against a stated release SHA using synthetic/redacted data. Confirm visible workflow/claims, readable zooms and annotations, captions, professional narration, and owner approval. Then add verified video IDs/approved image paths to the existing component and hub; no video CMS is needed. No application UI changes were made.

## Waitlist and conversion

Both sites use the same existing Zoho URL whose public title is **TradeBoard Waitlist**:

`https://forms.zohopublic.com/greghaydelgm1/form/TradeBoardWaitlist/formperma/ZesK-fk6NxQJBtB0a818KwRQSZhoyC8ThdQ-Co-J8Wc`

Direct destination GET/render: **PASS** (labeled email field and Submit button observed; no submission). Form identity matches pre-existing source, but Zoho account ownership, receiver delivery, retention and success behavior were not verified through the external account. Direct fallback links remain available. Primary iframes load eagerly and have 520px height. Labels and copy distinguish a waitlist entry from account creation, payment and a founding-place reservation.

Embedded form rendering was observed successfully in both sites during browser checks. Repeat visits also showed blank frames with no surfaced console error; later observations populated the fields. **Rendering consistency/time-to-ready: NOT VERIFIED**; do not turn an earlier successful render into an unconditional integration PASS. A plain static iframe isolation check and the final TradeBoard root both eventually rendered the actual email field. Eager loading is enabled and the primary React iframe now sits outside an animated container, but no stable rendering-time bound was measured. The same provider URL works directly, and the fallback is essential. Resolve repeat rendering/performance acceptance before release; no external form account was modified, and no fake registration was sent.

## External links and live cross-site dependency

GET checks initially covered 71 unique external destinations: 54 PASS, 3 FAIL, 14 NOT VERIFIED. Two 404 article references were replaced with verified official pages and retested HTTP 200: [Anthropic system cards](https://www.anthropic.com/system-cards) and [AMA augmented intelligence](https://www.ama-assn.org/practice-management/digital-health/augmented-intelligence-medicine). The remaining FAIL is `https://cajun-ai.com/pages/youtube.html#tradeboard`: HTTP 200, but the **current production page lacks that anchor**. Corrected local source has the anchor and tutorials. Coordinate a separately authorized Cajun AI release before claiming TradeBoard's canonical cross-site deep link works publicly. Do not substitute an unverified channel or a preview host.

NOT VERIFIED destinations returned anti-bot/payment responses or a fetch failure; these are not proven broken links: `chat.lmsys.org` (fetch failure); `jamanetwork.com`, `midjourney.com`, `openai.com`, `openai.com/index/gpt-4o-system-card/`, `perplexity.ai`, `www.cmegroup.com/education`, `www.mckinsey.com`, the linked McKinsey generative-AI article (403); five linked Investopedia articles (402). They require a normal authorized-browser recheck. Other editorial article assertions were not certified as current product facts by a successful URL response.

## Hosting and no-deployment control

Read-only inspection of the existing Cloudflare dashboard established both repository mappings, production branch `main`, automatic deployments enabled, and **public preview deployments of the existing review branches before this task**. The old handoff's blanket “not deployed” wording was inaccurate for previews. Production heads were unchanged at the observed baselines: Cajun AI `66e49c49b851fcfa9fa5a510ced483714eb3822d`; TradeBoard website `3d5d94481326cb5625e64736130675ee578bb519`.

| Project | Domain/source/build | Existing review preview before this task |
| --- | --- | --- |
| Cajun AI | `cajun-ai.com`, `www.cajun-ai.com`; `greghaydel-arch/cajun-ai-production`; root static output, no build command/functions | `d51eb552-a473-4eb9-8c62-fe6ecc6a6e27`, source `2e295e128c3279d6c2e1687de797a7ff4b728da4` |
| TradeBoard marketing | `trade-board.net`; `greghaydel-arch/tradeboard-website`; root, `bun install && bun run build`, output `dist`, no Pages Functions | `e03944ca-435d-42e8-859f-153938d8bb75`, source `1a8b93f3dd9bec74f6dab92035eb7c65f1854ff0` |

Dashboard settings displayed no deploy hooks. No repository GitHub Actions workflows were found; Cloudflare checks publish assets and therefore cannot be used as a no-deployment test gate here. **Hosted build/canonical Cloudflare execution for the new commits: NOT VERIFIED / intentionally not run.** Local build success is not release permission.

Every task commit starts with `[CF-Pages-Skip]`, Cloudflare's documented deployment-omission prefix; it targets Pages and does not skip local validation. See [official GitHub integration documentation](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/#skipping-a-build-via-a-commit-message). Preserve this prefix for review-only follow-up commits. Hosting settings were not changed. The owner has since prohibited pushes; no task commit was transmitted, and provider deployment baselines remain the previously observed heads. Future post-push checks and PR updates are deferred until explicit owner resumption.

Both repositories are currently **public** according to GitHub metadata; existing PRs cannot provide private review merely by being drafts. No visibility change was made. Do not add private screenshots, customer records, real credentials or confidential review material. Both preview gates ship their comparison logic/browser flags; source is retrievable without authentication. **Private preview protection: FAIL.** Server/hosting authentication requires a separately authorized owner/security decision. Root static Cajun AI publishing can also expose repository documentation; exclude internal review documents from the future public artifact or protect that environment before release.

## Remaining gates and exact next steps

1. ChatGPT independently reviews the final combined diffs and this report; retain `REVIEW_PENDING_CHATGPT` until that review is complete. This task does not sign off its own work.
2. Resolve repeat iframe blank rendering; then, with an owner-designated real submission and appropriate authorization, verify external waitlist receipt/confirmation. Keep direct fallback links.
3. Owner verifies the selected Cajun AI stable channel ID/ownership in the correct YouTube Studio channel. Add links/embeds only after actual video approval; create no separate TradeBoard channel.
4. Approve final UI and capture the real application showcase/tutorials with synthetic/redacted records. No currently missing asset is represented as complete.
5. Reconcile the September 28 draft, processor/cookie/analytics inventory, category-specific retention, payment terms and preview access with owner/counsel/security review. Public signup and billing remain closed.
6. Recheck blocked external links, broader browser/assistive-technology coverage, and hosted route/build behavior under separately authorized controlled-release testing. For a future release, Cajun AI's canonical hub must exist before TradeBoard points users to its live section. Obtain explicit merge/deployment approval separately; none follows from local PASS results.

## Files changed in the implementation commits

- `index.html`
- `pages/about.html`
- `pages/ai-news.html`
- `pages/ai-tools.html`
- `pages/ai-trends-2026.html`
- `pages/articles/ai-in-energy-healthcare-business.html`
- `pages/articles/analyze-trading-performance.html`
- `pages/articles/automate-workflow-with-ai.html`
- `pages/articles/best-ai-tools-2026.html`
- `pages/articles/chatgpt-vs-claude-vs-gemini.html`
- `pages/articles/claude-35-sonnet-review.html`
- `pages/articles/perplexity-ai-review.html`
- `pages/articles/trading-journal-setup.html`
- `pages/articles/trailing-stops-explained.html`
- `pages/articles/what-is-generative-ai.html`
- `pages/blog.html`
- `pages/contact.html`
- `pages/legal.html`
- `pages/login-full.html`
- `pages/login.html`
- `pages/pricing-full.html`
- `pages/pricing.html`
- `pages/tech-reviews.html`
- `pages/tradeboard-full.html`
- `pages/tradeboard.html`
- `pages/youtube.html`
- `preview.html`
- `script.js`
- `styles.css`

This handoff also adds this report and an additive correction in `docs/VIDEO_CHANNEL_HANDOFF.md`.


## Authorized preview protection update — October 16, 2026, 11:40 CDT

This section supersedes the earlier hosting-settings hold and the earlier preview-protection FAIL **only for the provider controls and URLs tested below**. All website source, legal, content, form, release, and GitHub holds remain. Status: `REVIEW_PENDING_CHATGPT`; this is implementation evidence, not independent approval.

The owner expressly authorized preview-only Cloudflare Access and Custom preview branch controls for these two projects. No GitHub push, PR update, merge, build, deployment, DNS change, DOT activity, new credentials, or paid enrollment was performed.

| Saved setting | Cajun AI | TradeBoard marketing | Result |
| --- | --- | --- | --- |
| Preview branches | Custom; include `*`; exclude exact `marketing/20261016-release-truth` | Same | PASS: saved, reopened and read back |
| Production branch and automatic deployments | `main`; enabled, unchanged | `main`; enabled, unchanged | PASS |
| Access destination | `*.cajun-ai-production.pages.dev` | `*.tradeboard-website.pages.dev` | PASS: no production root/custom hostname in either application |
| Access policy | Allow Members - Cloudflare Pages; one exact signed-in owner email include rule | Same exact owner identity; one rule | PASS: inspected generated policy details; no Everyone/bypass rule present |
| Access application ID | `4539ef8b-421d-4c4c-9575-48a043533e71` | `81a10d1e-3842-4eeb-9403-4452e7323156` | PASS |
| Policy ID | `4a8dafdb-1611-4875-ac04-0c32db8b4114` | `408c2b2c-6eca-458f-be58-80940a6454ab` | PASS |
| Actual authenticated owner access to both aliases and hashes | Email-code login required; not completed | Not completed | NOT VERIFIED: owner must sign in directly through Cloudflare |
| Excluded branch cannot trigger a build | Configuration verified; no test push | Same | NOT VERIFIED by push, intentionally: no push/build authorized |

TradeBoard's first policy-creation attempt displayed “Access policy could not be created.” One retry succeeded; the resulting application and single email policy were read back. No broad/manual fallback policy was added. Cloudflare's shared team domain is `cajun-ai-production-pages.cloudflareaccess.com`, including for the TradeBoard application; the protected destination and policy are distinct.

### Cookie-free HTTP verification

The following separate HTTPS requests used no browser cookies, did not follow redirects, and did not submit forms. A 302 to Cloudflare Access is PASS for denial of unauthenticated website content, not proof that a signed-in owner can enter. Query strings containing transient authentication metadata were omitted from evidence. Probe time: 2026-10-16T16:40:42.299Z.

| URL | HTTP status | Redirect destination / result | Verdict |
| --- | --- | --- | --- |
| https://marketing-20261016-release-t.cajun-ai-production.pages.dev/ | 302 | https://cajun-ai-production-pages.cloudflareaccess.com/cdn-cgi/access/login/marketing-20261016-release-t.cajun-ai-production.pages.dev | PASS |
| https://d51eb552.cajun-ai-production.pages.dev/ | 302 | https://cajun-ai-production-pages.cloudflareaccess.com/cdn-cgi/access/login/d51eb552.cajun-ai-production.pages.dev | PASS |
| https://marketing-20261016-release-t.tradeboard-website.pages.dev/ | 302 | https://cajun-ai-production-pages.cloudflareaccess.com/cdn-cgi/access/login/marketing-20261016-release-t.tradeboard-website.pages.dev | PASS |
| https://e03944ca.tradeboard-website.pages.dev/ | 302 | https://cajun-ai-production-pages.cloudflareaccess.com/cdn-cgi/access/login/e03944ca.tradeboard-website.pages.dev | PASS |
| https://cajun-ai-production.pages.dev/ | 200 | No redirect; public website title observed | PASS |
| https://tradeboard-website.pages.dev/ | 200 | No redirect; public website title observed | PASS |
| https://cajun-ai.com/ | 200 | No redirect; public website title observed | PASS |
| https://www.cajun-ai.com/ | 200 | No redirect; public website title observed | PASS |
| https://trade-board.net/ | 200 | No redirect; public website title observed | PASS |

The initial sandboxed network attempt failed for all URLs; it was not counted as PASS. The subsequent permitted read-only network check produced the results above. Current review aliases and immutable hashes are directly verified; wildcard configuration covers other preview hostnames, but every historical deployment URL was not individually requested.

Deployment history still showed the existing latest preview heads (`2e295e1` Cajun; `1a8b93f` TradeBoard) and production heads (`66e49c49b851fcfa9fa5a510ced483714eb3822d` Cajun; `3d5d94481326cb5625e64736130675ee578bb519` TradeBoard). No new deployment was started by this work.

### Plan, legal, and owner-login boundary

`BLOCKED_BY_OWNER_COST_APPROVAL`: Cloudflare One Settings reports “No plan has been chosen yet. Choose a plan to avoid disruptions to your account.” The Free option is displayed as $0/seat/month with a 50-seat limit. Its final checkout requires two unchecked consents: agreement to Terms/Privacy, and authorization to charge the existing card for usage exceeding free limits each month until cancellation. Neither consent was checked; Activate was not clicked. No subscription or payment change was made.

Required decision details:

1. Proposed operation: activate Cloudflare Zero Trust Free for the existing account to resolve its unselected-plan warning. This is an account-level enrollment, beyond merely saving the two preview applications.
2. Displayed base charge: $0/month, up to 50 seats. Excess-usage rates, applicability, and a hard spending cap were not verified; $0 total cannot be guaranteed from this checkout. No GitHub Actions allowance or build minutes were used.
3. Free/local alternative: continue local-only review and retain the saved branch exclusions. Access currently denies anonymous requests without completing enrollment, but its continuity is not certified. Local-only review avoids additional publishing; it does not itself secure existing previews.
4. Postponement: both Access policies enforce the tested anonymous boundary now, but the provider warns of possible disruptions. Authenticated owner access and long-term availability remain uncertified.
5. Recommendation: do not accept uncapped charge authorization. Owner/ChatGPT should confirm whether Pages-only Access can remain supported without plan enrollment or establish a zero-cost cap/approved enrollment path. Any legal acceptance or potential charge commitment requires a separate owner decision.

The secure owner email-code login page was left open for owner completion; no code was requested in chat, read from email, or entered by the agent. Owner dashboard access and the policy's matching email are not substitutes for an actual successful preview login. Next: owner signs in directly, then validate website rendering on all four preview URLs and repeat anonymous denial checks. ChatGPT must independently review the saved controls and evidence before considering this boundary complete.

Official references: [Pages preview Access scope](https://developers.cloudflare.com/pages/configuration/preview-deployments/), [branch controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/), and [Zero Trust plans](https://www.cloudflare.com/plans/zero-trust-services/). The account checkout, rather than the advertised base price alone, determines the outstanding approval boundary.

Local evidence (outside these public repositories): `C:/webull-dashboard/.website-review/qa/cloudflare-preview-probes-2026-10-16.json`, `cloudflare-preview-check.cjs`, and screenshots `cajun-preview-branches-saved.jpg`, `tradeboard-preview-branches-saved.jpg`, `cajun-preview-owner-policy.jpg`, `tradeboard-preview-owner-policy.jpg`, `cajun-access-login-required.jpg`, `cloudflare-free-plan-approval-boundary.jpg` in the QA screenshots directory. Account screenshots are not committed to public source.

All earlier local website implementation commits and complete validation reports are preserved. Pushes and PR-description updates remain deferred; branch exclusion and a commit skip prefix do not constitute owner authorization to publish. No website release is authorized.


## Read-only Cloudflare billing review — October 16, 2026, 16:51 UTC

Owner requested billing verification before any further preview login/enrollment. No provider settings, billing details, subscription, plan, consent, or resource were changed in this review. Development remains local; pushes, PR writes, builds on Cloudflare, releases, and DOT remain prohibited.

### Verified account facts

| Check | Observed result | Verdict |
| --- | --- | --- |
| Account Billing > Subscriptions > Subscribed (unfiltered) | Only `Workers Free`, Active; no paid Pages, Workers, Access, or other paid add-on subscription listed | PASS |
| Compute > Workers plans | Free, `$0`, `Current plan`; Paid is an upgrade option, not current | PASS |
| Domain overview | `cajun-ai.com` and `trade-board.net` Active, Plan `Free` | PASS |
| Zero Trust > Settings > Cloudflare One plan | No plan has been chosen; provider still warns to choose one to avoid disruptions | PASS for observation; Access continuity NOT VERIFIED |
| Zero Trust > Team & Resources > Users | Empty-state user inventory: users appear after first successful Access login/device enrollment; no registered users listed | PASS: 0 listed users; no paid seat subscription or billable seats shown |
| Paid service activation by the two preview policies | No paid subscription appears after policy creation; Zero Trust still has no selected plan; prior checkout was never activated | PASS: no paid-service activation found |
| Workers & Pages inventory, Show all | Three Pages projects (including the two websites); no standalone Worker script listed | PASS |
| Account Workers usage, October 1–16 | Requests 0; CPU time 0 ms; observability events 0; Workers build minutes 0; today's requests 0/100,000 | PASS for displayed period; these are not Pages deployment counts |
| Both current production deployments | Existing build logs explicitly report no `/functions` directory and skip Functions; no Wrangler configuration found | PASS |
| Both website Settings > Bindings | Empty resource-binding configuration | PASS |
| Billing > Billable usage, Current Month | Spectrum panel says No data; page says daily refresh and estimates only | NOT VERIFIED as a final invoice or universal $0 metered-usage certificate |
| Billing > Invoices | Only two historical paid June invoices displayed; no new October invoice listed at review time | PASS for list observation; invoice-generation lag can exist |

Verified recurring **monthly hosting and preview-security subscription cost for these websites: $0/month**. This is the observed active configuration, not an estimate of a future invoice or a guarantee of uninterrupted Access service without selecting a plan. Policies are applications, not two paid users; the user inventory is empty.

### Existing annual domain renewals (separate from hosting)

The account does have recurring annual registration costs and existing payment methods; it is not an account with no possible future charges. No payment details are reproduced here.

| Domain | Registrar's current displayed renewal price | Existing auto-renew schedule | Registration expiry |
| --- | --- | --- | --- |
| `cajun-ai.com` | $10.46/year | Enabled; May 3, 2027, one year | June 2, 2027 |
| `trade-board.net` | $11.86/year | Enabled; May 31, 2027, one year | June 30, 2027 |

The registrar displays a notice that standard `.com` pricing rises from $10.46 to $11.17 effective November 1, 2026. Current displayed combined annual price is $22.32. **Estimate only:** $23.03/year after that announced increase if `.net` remains $11.86 and no other adjustments/taxes apply. These are annual renewals, not monthly hosting charges, and no renewal or payment action was performed.

### Usage-based exposure and remaining boundary

- Current static Pages asset delivery: official [Pages pricing](https://developers.cloudflare.com/pages/functions/pricing/) states static requests are free and unlimited. With current no-Functions artifacts, there is no identified request/CPU overage charge for serving these two static websites.
- Functions, if added later, share Workers quotas. A future [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/) upgrade or paid storage/AI/other add-on can introduce usage charges; none is authorized or currently listed as a paid subscription. A plan's comparison table is not proof that those products are enabled.
- Zero Trust's unsubmitted Free-plan checkout previously required legal acceptance and authorization for monthly charges exceeding free limits. That consent remains unaccepted by this agent. No claim is made that future enrollment has a verified hard $0 cap; enrollment remains `BLOCKED_BY_OWNER_COST_APPROVAL` and is outside this read-only request.
- No current paid Access subscription and no users are observed. Authenticated preview access is still NOT VERIFIED; creating the policies did not itself complete owner login.
- Usage dashboards are delayed/limited and cannot certify all future invoices. This review found no active paid website add-on, but did not open every unrelated product's resource inventory. External processors such as Zoho and Runable are outside this Cloudflare billing review.

Recommendation: retain the current Free hosting configuration, do not enroll/upgrade/accept charge consent, and continue local-only development. Resolve the Access plan warning and owner login separately with owner/ChatGPT review. Preserve `REVIEW_PENDING_CHATGPT`; this financial inspection does not authorize a release or a GitHub push.


## No-credit-card directive and preview retirement inspection

Zero Trust onboarding is stopped; no payment method, legal/overage consent, subscription, settings save, deployment deletion, GitHub write, or deployment was performed. Current anonymous denial is reverified for all 38 hosted preview URLs and both aliases; production remains public on all five tested roots/custom domains. Both projects still use Custom preview branch controls; None is recommended but not applied. Current Access continuity without enrollment and authenticated owner access remain NOT VERIFIED.

The complete per-project inventory, exact None-setting proposal, production preservation list, and approved-deletion boundaries are in [Cloudflare preview retirement report](CLOUDFLARE_PREVIEW_RETIREMENT_2026-10-16.md). This supersedes earlier suggestions to resume enrollment. Local development remains the preferred $0-additional-cost workflow. `REVIEW_PENDING_CHATGPT`.

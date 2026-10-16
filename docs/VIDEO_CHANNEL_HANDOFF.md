# Cajun AI + TradeBoard: One YouTube Channel — Website / Codex Handoff

Status: **review-stage decision; production release not authorized** (2026-10-16).

Validation correction (October 16): read-only Cloudflare inspection found that the existing review branches already had public preview deployments before Codex began this completion task. “Not deployed” did not accurately describe those previews. Production remains on `main`. Task commits use the documented `[CF-Pages-Skip]` prefix to avoid further deployment without changing hosting settings. Cosmetic preview flags do not authenticate visitors. See [WEBSITE_RELEASE_VALIDATION_2026-10-16.md](WEBSITE_RELEASE_VALIDATION_2026-10-16.md) for actual PASS/FAIL/NOT VERIFIED results, remaining iframe/legal/access gates and `REVIEW_PENDING_CHATGPT`. Channel identity and historical monetization figures were not revalidated by this website task.

## Approved channel strategy

- Use exactly **one Cajun AI YouTube channel** for original AI news, technology explainers, software tutorials, and TradeBoard app walkthroughs. **Do not create a separate TradeBoard channel.**
- Brand TradeBoard tutorials as **TradeBoard by Cajun AI**, organized within a dedicated series / playlist on the single Cajun AI channel.
- A shared Google login can own multiple channels, but YouTube subscribers, qualifying watch hours, and eligibility **belong to each individual channel**, not to the login; do not split traffic for the assumption that it combines.
- Preserve user/owner approval for each publication. YouTube upload OAuth / automation has not been authorized; no videos should be uploaded or published as part of this website task.

## Critical channel URL integrity

- The earlier public Cajun AI website used `https://www.youtube.com/@cajunnationtech` and described **Cajun Nation Tech**. This is a **legacy website link**, not evidence of the chosen **Cajun AI** channel's current URL or ownership.
- The new Cajun AI public-facing website draft points video CTA/footer links to its own `/pages/youtube.html` hub (all internal links). It does not redirect to the legacy handle or invent a replacement URL.
- The TradeBoard website draft points Tutorials / App tutorials to `https://cajun-ai.com/pages/youtube.html#tradeboard`.
- **Owner action before any public channel button, embed or OAuth consent:** retrieve the actual selected Cajun AI channel URL or stable channel ID directly from the correct YouTube Studio channel, verify its current display identity and ownership, and ensure uploads are targeted to that same channel ID. Do not rely only on an arbitrary @handle.
- Once verified, add the outbound channel link in one canonical Cajun AI hub and test it. Keep marketing sub-sites linking to the hub, not duplicating the handle throughout many footers.
- If the verified channel is the legacy account renamed to Cajun AI, confirm the current channel ID and redirect before updating links. Do not migrate/re-upload videos just to consolidate branding: YouTube cannot combine channel history automatically.

## Video series / proposed playlist names (no playlists created yet)

1. **How Technology Works** — real demos, useful explanations, subject-specific visuals.
2. **AI Tools, News & Reviews** — independent comparisons and sourced updates.
3. **Software How-To Guides** — hands-on technical walkthroughs.
4. **TradeBoard Tutorials** — getting started, validated historical CSV import, analytics views, journal, retrospective review.

These are planning labels. No playlist ID, YouTube videos, upload rights, or monetization status has been verified.

## Product, UX and monetization safeguards

- TradeBoard is historical analytics / education; **not** trading execution, broker order automation, signals, or individualized investment advice.
- Record TradeBoard tutorials from **approved, final, working product UI**, not speculative mockups or generic card slides. Use synthetic/redacted demo data, no real customer credentials, balances, broker account numbers, or private records.
- Preserve accessible captions, realistic narration pacing, original visual examples, useful substantive commentary, and accurate scope. Avoid highly repetitive, templated AI-generated videos; YouTube reviews channels for original/authentic content.
- Keep public video pages honest about what is **planned**, **unreleased**, or **actually published**.
- YouTube monetization eligibility does not equal a guarantee of monetization or a specific earnings amount; review actual YouTube Studio Earn status when connected.
- **Monetization rule watch:** as of October 16, 2026, YouTube lists 1,000 subscribers plus 4,000 qualifying public long-form watch hours / 10M qualifying Shorts views for ads/Premium entry. Its official help page announces that starting **February 1, 2027**, *new applicants* instead need 1,000 subscribers plus **8,000** qualified long-form watch hours or **20M** qualified Shorts views, with the same 365-/90-day windows. Earlier access at 500 subscribers and 3,000 hours / 3M Shorts views is described as unchanged. See https://support.google.com/youtube/answer/12843009 ; recheck before publishing eligibility figures, and don't promise thresholds in marketing copy.
- Only eligible **public** video watch hours count toward the long-form watch-hour path. Unlisted/private videos, Shorts Feed watch hours and paid-ad campaign hours do not count toward that long-form threshold (https://support.google.com/youtube/answer/72851).
- No new software stack, video CMS, duplicate uploader, or independent channel is required for the initial website release.

## Handoff gates for the new Codex TradeBoard chat

- Work on the existing review branches only: `greghaydel-arch/cajun-ai-production:marketing/20261016-release-truth` and `greghaydel-arch/tradeboard-website:marketing/20261016-release-truth`. PR #1 in each repository is a draft.
- Read PR diffs and the current TradeBoard application release evidence as source of truth. Validate build, syntax, accessibility, responsive layout and all relative video hub links in isolated checkouts, **not shared writable trees**.
- Cajun AI's legal policy draft and TradeBoard marketing legal draft contain editorial redlines only. Reconcile against actual data flows, contractual terms and legal review; neither is counsel-approved.
- Do not assume YouTube ownership, OAuth grant, YPP eligibility, video count, payment status, production app availability, billing availability, or broker capabilities.
- **Do not merge, deploy, alter channel configuration, create playlists, upload/publish, or restart DOT** without explicit user approval and appropriate independent review.

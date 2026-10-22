# Indexing rollout proposal — October 22, 2026

**LOCAL CANDIDATE ONLY. REVIEW_PENDING_CHATGPT. Keep global noindex.**

`SITEMAP_CANDIDATE.xml` is a proposed allowlist for owner-approved pages, not an assertion that indexing is approved. It lives in docs and is excluded from the public artifact. No sitemap was submitted, no robots directive relaxed, and no Search Console or hosting setting changed.

| Site | Proposed initial indexable set after approval | Continue holding |
| --- | --- | --- |
| Cajun AI | Home, About, TradeBoard information, planned Pricing, article library and the ten corrected educational articles (15 URLs) | Contact/data-collection status, login/access status, legal status, planned-video hub, trend explainer until additional editorial approval, old category aliases, all private/full previews, draft legal pages, internal docs and 404 |
| TradeBoard marketing | Home, Product, planned Pricing (3 URLs) | Waitlist, legal status, 404, all review screens and drafts |

Canonical forms: Cajun apex `https://cajun-ai.com/` and extensionless `/pages/...`; TradeBoard apex `https://trade-board.net/` and trailing-slash physical directories. Retain existing article slugs when titles change. Old Cajun category URLs redirect to the library; old legal URLs redirect only to nonbinding status. Canonical markup does not establish live www/apex/pages.dev redirect behavior.

Sequence, each live step requiring separate authorization:

1. Independent source/editorial review, owner/counsel waitlist/vendor approval and hosting-output verification. Confirm current domains, canonical host redirects, real 200/404 status, required headers and excluded-path denials. Do not publish a repository root or review-dist.
2. Approve the specific pages in the candidate XML. Resolve any founder/company wording with the owner. Check facts and linked sources again before a later publication date. Remove a page from the proposal if it lacks useful, verified content.
3. Prepare a separate patch that removes both meta and header noindex only for approved pages, retaining holds elsewhere. Do not simply remove the global header and assume individual pages are protected. Add the approved XML to the build allowlist only in that separately reviewed change.
4. Verify hosted rendered content and canonicals, including TradeBoard's JavaScript rendering and useful no-script fallback, before requesting indexing. Submit only through the owner-authorized property. A sitemap is discovery guidance, not a guarantee of inclusion or ranking.

No `robots.txt` disallow was introduced as a privacy measure: a crawler needs to fetch a page to observe noindex. Neither noindex nor a sitemap is access control. Keep private source absent from release output; existing historical preview access controls need independent provider verification.

Structured data is deliberately limited to Cajun AI Organization and TradeBoard WebSite identities. No Product/Offer, rating, testimonial, FAQ rich-result, VideoObject, invented publication history or unverified social `sameAs` data is asserted. Consider Article/Breadcrumb metadata only after editorial ownership and dates are approved; do not add review scores without real evidence.

Official guidance consulted October 22, 2026:
- [Google: noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Google: sitemap overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Cloudflare: serving Pages](https://developers.cloudflare.com/pages/configuration/serving-pages/)
- [Cloudflare: response headers](https://developers.cloudflare.com/pages/configuration/headers/)

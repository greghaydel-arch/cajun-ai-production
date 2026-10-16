# Current review build (October 16, 2026)

All development and validation remain local; a passing build does not authorize publication.
Run `python scripts/build-site.py` to prepare `dist/`, then
`python -m http.server 4174 --bind 127.0.0.1 --directory dist` to inspect it.
The explicit `scripts/public-files.json` allowlist excludes draft `pages/legal.html`,
all `*-full.html` pages, `preview.html`, internal documents, development tools and
unlisted assets. Run `python scripts/test-public-output.py` for boundary tests.
Public legal links lead only to nonbinding `pages/legal-status.html`.

**Release blocker:** Cloudflare currently serves the repository root. A future
owner-approved hosting change must set build command `python3 scripts/build-site.py`
and output directory `dist` before any release of this branch. Verify Python
availability and hosted direct routes in that separately approved operation.
No hosting setting has been changed by this local preparation. Owner/counsel must
approve the actual waitlist notice and data handling before visitor collection
through this candidate. Earlier installation instructions do not authorize a push
or deployment. Never publish the repository root or infer protection from a browser flag.

Internal review source remains intact. For local review only, serve the repository
on loopback, unlock `preview.html`, then open `pages/tradeboard-full.html` or
`pages/pricing-full.html` directly. Public pages no longer redirect based on that flag.
Do not expose that source server to a network or publish it.

See [the focused hardening report](docs/RELEASE_HARDENING_2026-10-16.md) for
validation, SEO recommendations and remaining release gates.

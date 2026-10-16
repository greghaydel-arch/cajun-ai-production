# Current review build (October 16, 2026)

All development and validation remain local; a passing build does not authorize publication.
Run `python scripts/build-site.py` to prepare `dist/`, then
`python -m http.server 4174 --bind 127.0.0.1 --directory dist` to inspect it.
The allowlist includes only the existing website HTML, CSS, JavaScript and assets.
It excludes `docs/`, repository metadata, scripts and installation notes.

**Release blocker:** Cloudflare currently serves the repository root. A future
owner-approved hosting change must set build command `python3 scripts/build-site.py`
and output directory `dist` before any release of this branch. Verify Python
availability and hosted direct routes in that separately approved operation.
No hosting setting has been changed by this local preparation. The legal page in
the output is still a visibly labeled editorial draft; it cannot replace an
effective policy without owner/counsel approval. Earlier installation instructions
do not authorize a push or deployment.

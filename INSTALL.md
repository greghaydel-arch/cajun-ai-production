# WCAG 2.1 AA Accessibility Fixes — Cajun AI Website
## Date: July 1, 2026

## Files Changed (12 total)
All files are DROP-IN REPLACEMENTS. Copy each file to the exact path shown below,
then commit and push via GitHub Desktop → Cloudflare auto-deploys.

---

### ROOT FILES (C:\Users\gregh\Projects\cajun-ai-website\)

| File | Action | Windows Path |
|------|--------|--------------|
| index.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\index.html |
| styles.css | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\styles.css |
| script.js | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\script.js |
| preview.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\preview.html |

### PAGES FOLDER (C:\Users\gregh\Projects\cajun-ai-website\pages\)

| File | Action | Windows Path |
|------|--------|--------------|
| about.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\about.html |
| blog.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\blog.html |
| contact.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\contact.html |
| youtube.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\youtube.html |
| legal.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\legal.html |
| tradeboard.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\tradeboard.html |
| pricing.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\pricing.html |
| login.html | REPLACE | C:\Users\gregh\Projects\cajun-ai-website\pages\login.html |

---

## What Was Fixed (WCAG 2.1 AA)

### Global (all pages)
- **Skip-to-content link**: Keyboard users can jump directly to main content
- **Nav landmark**: `<header aria-label="Main navigation">` on all pages
- **Hamburger menu**: `aria-expanded` now toggles correctly on open/close
- **Mobile nav**: `id="mobile-nav" aria-label="Mobile navigation"` on all pages
- **Main landmark**: `<main id="main-content" tabindex="-1">` wraps all page content
- **Focus rings**: `:focus-visible` global styles — keyboard users always see where focus is
- **Reduced motion**: IntersectionObserver scroll animations disabled when OS prefers reduced motion; CSS animations suppressed via `@media (prefers-reduced-motion: reduce)`
- **Footer social links**: All 4 platforms get `aria-label="Cajun AI on [Platform] (opens in new tab)"` + `rel="noopener noreferrer"`

### index.html
- Trust bar marquee: `aria-hidden="true"` (decorative)
- Mock dashboard: `aria-hidden="true"` (decorative illustration)
- Feature icons (📊🤖▶️🚀) + showcase icons (📈⚡📱🔒): `aria-hidden="true"`
- Hero scroll indicator: `aria-hidden="true"`
- Hero logo image: `alt=""` (decorative; h1 already provides text)
- YouTube CTA link: `aria-label="...  (opens in new tab)"`

### pages/blog.html
- Filter buttons: `aria-pressed="true/false"` — screen readers announce active filter
- `filterCat()` JS: updates `aria-pressed` on button click
- Newsletter email input: explicit `<label>` linked via `for`/`id`
- Article link cards: `aria-label` with full title + category + date + read time
- Filter region: `role="region" aria-label="Filter articles by category"`

### pages/legal.html
- Tab buttons: `role="tab"`, `aria-selected`, `aria-controls`
- Tab container: `role="tablist" aria-label="Legal documents"`
- Tab panels: `role="tabpanel"`, `aria-labelledby`, `tabindex="0"`
- `showTab()` JS: updates `aria-selected` on tab switch
- Removed invalid duplicate `id="tos"` on same element

### pages/contact.html
- **Complete rebuild**: was a bare skeleton — now has full nav, footer, contact form,
  social channel cards, and a `role="alert"` success message
- All 3 form fields: explicit `<label>` elements

### pages/tradeboard.html / pricing.html / login.html (Coming Soon)
- Email inputs: `<label class="sr-only">` + matching `id`
- `aria-live="polite"` + `role="alert"` on success messages
- `cs-badge-dot` pulsing dot: `aria-hidden="true"` (decorative animation)
- External links: `aria-label="... (opens in new tab)"`

### preview.html
- Added `<main id="main-content" tabindex="-1">` wrapper
- Password input already had a label — verified correct
- Error message: `role="alert"` + `aria-describedby` linking to error element

### styles.css (appended — no existing rules changed)
- `.skip-link` styles (hidden, revealed on focus)
- `.sr-only` utility class (visually hidden, readable by screen readers)
- `:focus-visible` global outline styles
- `@media (prefers-reduced-motion: reduce)` block

### script.js
- Hamburger: `aria-expanded` toggled on click and on mobile nav link click
- Scroll observer: wrapped in `!window.matchMedia('prefers-reduced-motion: reduce').matches` check

---

## Deploy Steps
1. Extract ZIP
2. Copy all 12 files to Windows paths shown above (REPLACE existing files)
3. Open GitHub Desktop → should show all 12 files changed
4. Commit: "feat: WCAG 2.1 AA accessibility audit and fixes (all pages)"
5. Push to origin → Cloudflare Pages auto-deploys (1-2 min)
6. Verify on cajun-ai.com: Tab through page, skip link should appear on first Tab press

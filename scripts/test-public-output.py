"""Local build-boundary regression tests; no network or deployment."""
import importlib.util
import json
from pathlib import Path
import tempfile
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_site', ROOT/'scripts/build-site.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class PublicOutputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.names = json.loads((ROOT/'scripts/public-files.json').read_text())
        for name in self.names + ['scripts/public-files.json']:
            target = self.root/name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/name, target)
        builder.ROOT = self.root
        builder.OUTPUT = self.root/'dist'

    def tearDown(self):
        self.temp.cleanup()

    def test_only_allowlisted_files_survive_real_build(self):
        for name in ['preview.html','pages/legal.html','pages/tradeboard-full.html','assets/internal-review.txt','docs/private-review.md','.env']:
            target=self.root/name
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text('INTERNAL_TEST_SENTINEL')
        (self.root/'dist').mkdir()
        (self.root/'dist/stale-review.html').write_text('INTERNAL_TEST_SENTINEL')
        builder.build()
        actual={p.relative_to(builder.OUTPUT).as_posix() for p in builder.OUTPUT.rglob('*') if p.is_file()}
        self.assertEqual(actual,set(self.names))
        self.assertFalse(any('INTERNAL_TEST_SENTINEL' in p.read_text(errors='ignore') for p in builder.OUTPUT.rglob('*') if p.is_file()))
        self.assertTrue((self.root/'pages/legal.html').exists(), 'Review sources must remain intact')

    def test_manifest_excludes_private_categories(self):
        for name in self.names:
            self.assertNotIn('-full.',name)
            self.assertNotIn(name,['preview.html','pages/legal.html'])
            self.assertFalse(name.startswith(('docs/','scripts/','.')))

    def test_missing_asset_fails_before_output_replacement(self):
        (self.root/'dist').mkdir()
        (self.root/'dist/previous.txt').write_text('previous build')
        (self.root/'index.html').unlink()
        with self.assertRaises(RuntimeError):builder.build()
        self.assertTrue((self.root/'dist/previous.txt').exists())

    def test_public_icons_are_sized_and_originals_excluded(self):
        import struct
        for name, size in [('assets/images/favicon-64.png',64),('assets/images/logo-512.png',512)]:
            data=(self.root/name).read_bytes()
            self.assertEqual(struct.unpack('>II',data[16:24]),(size,size))
        for name in ['assets/images/logo.png','assets/images/favicon.png','assets/images/hero-bg.jpg','assets/images/circuit-bg.jpg']:
            self.assertNotIn(name,self.names)

    def test_contact_no_script_cannot_submit_personal_data(self):
        text=(self.root/'pages/contact.html').read_text(encoding='utf8')
        self.assertIn('<fieldset id="contactFields" disabled',text)
        self.assertIn('<noscript>',text)
        self.assertIn('mailto:support@cajun-ai.com',text)
        self.assertLess(text.index("e.preventDefault()"),text.index("contactFields').disabled = false"))

    def test_traversal_is_rejected(self):
        (self.root/'scripts/public-files.json').write_text('["../outside.html"]')
        with self.assertRaises(RuntimeError):builder.build()
        for name in ['pages/LEGAL.html', 'pages\\legal.html', 'pages/./legal.html']:
            (self.root/'scripts/public-files.json').write_text(json.dumps([name]))
            with self.assertRaisesRegex(RuntimeError, 'Invalid public asset path'):
                builder.build()

    def test_accidentally_allowlisted_private_file_fails_closed(self):
        for name in ['preview.html', 'pages/legal.html', 'pages/login-full.html',
                     'docs/review.md', '.env', 'assets/images/review.txt']:
            with self.subTest(name=name):
                target = self.root/name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text('INTERNAL_TEST_SENTINEL')
                (self.root/'scripts/public-files.json').write_text(json.dumps(self.names+[name]))
                with self.assertRaisesRegex(RuntimeError, 'Nonpublic asset category'):
                    builder.build()

    def test_output_headers_keep_hold_and_browser_boundaries(self):
        headers = (self.root/'_headers').read_text()
        for value in ['X-Robots-Tag: noindex, nofollow', 'Referrer-Policy: no-referrer',
                      "frame-ancestors 'none'", "object-src 'none'", "base-uri 'self'", "frame-src 'none'"]:
            self.assertIn(value, headers)

    def test_editorial_corrections_and_indexing_hold(self):
        import re
        titles = set()
        for name in self.names:
            if not name.endswith('.html'): continue
            text = (self.root/name).read_text(encoding='utf8')
            self.assertRegex(text, r'noindex,\s*nofollow')
            if name.startswith('pages/articles/'):
                self.assertIn('October 22, 2026', text)
                self.assertNotIn('Our Ratings', text)
                self.assertNotIn('For most professional writing and knowledge work use cases:', text)
                titles.add(re.search(r'<title>(.*?)</title>', text)[1])
        self.assertEqual(len(titles), 10)
        stop = (self.root/'pages/articles/trailing-stops-explained.html').read_text(encoding='utf8')
        self.assertIn('A subsequent price of $59 is still above that trigger', stop)
        self.assertIn('do not guarantee an execution price', stop)
        self.assertNotIn('docs/SITEMAP_CANDIDATE.xml', self.names)

    def test_real_article_library_replaces_empty_categories(self):
        redirects = (self.root/'_redirects').read_text()
        for slug in ['ai-news', 'ai-tools', 'tech-reviews']:
            self.assertNotIn(f'pages/{slug}.html', self.names)
            self.assertIn(f'/pages/{slug} /pages/blog 302', redirects)
            self.assertIn(f'/pages/{slug}.html /pages/blog 302', redirects)

if __name__=='__main__':unittest.main()

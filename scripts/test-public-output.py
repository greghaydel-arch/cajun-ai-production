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

if __name__=='__main__':unittest.main()

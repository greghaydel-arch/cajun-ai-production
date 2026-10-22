"""Prepare only website assets for local validation and a future approved release.

Historical Cloudflare evidence recorded repository-root serving. Changing its build command to
python3 scripts/build-site.py and output directory to dist needs owner approval.
This script does not deploy or contact any provider.
"""
from pathlib import Path
import shutil
import json

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"


def build():
    # Delete only the generated output at this exact repository-local path.
    if OUTPUT.is_symlink() or OUTPUT.resolve() != ROOT / "dist":
        raise RuntimeError("Unsafe output path")
    names = json.loads((ROOT / "scripts/public-files.json").read_text())
    if len(names) != len(set(names)):
        raise RuntimeError("Duplicate public asset")
    sources = []
    for name in names:
        relative = Path(name)
        if (relative.is_absolute() or relative.drive or '..' in relative.parts or
                name != relative.as_posix() or name != name.lower()):
            raise RuntimeError("Invalid public asset path")
        # A manifest edit must not silently opt draft/review material into release.
        # These source categories remain local even when accidentally listed.
        if (name.startswith(('.', 'docs/', 'scripts/')) or
            name in ('preview.html', 'pages/legal.html') or '-full.' in name or
            not (name in ('index.html', '404.html', 'styles.css', 'script.js', '_headers', '_redirects') or
                 (name.startswith('pages/') and relative.suffix == '.html') or
                 (name.startswith('assets/images/') and relative.suffix in ('.png', '.webp', '.jpg', '.ico')))):
            raise RuntimeError(f"Nonpublic asset category: {name}")
        source = ROOT / relative
        if not source.is_file():
            raise RuntimeError(f"Missing public asset: {name}")
        sources.append(source)
    for source in sources:
        if source.is_symlink() or not source.resolve().is_relative_to(ROOT):
            raise RuntimeError("Public assets must be regular repository files")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for source in sources:
        destination = OUTPUT / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    print(f"Prepared {len(sources)} public files in {OUTPUT}")


if __name__ == "__main__":
    build()

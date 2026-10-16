"""Prepare only website assets for local validation and a future approved release.

Cloudflare currently serves the repository root. Changing its build command to
python3 scripts/build-site.py and output directory to dist needs owner approval.
This script does not deploy or contact any provider.
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
ROOT_FILES = ("index.html", "preview.html", "styles.css", "script.js")
PUBLIC_DIRS = ("pages", "assets")


def build():
    # Delete only the generated output at this exact repository-local path.
    if OUTPUT.is_symlink() or OUTPUT.resolve() != ROOT / "dist":
        raise RuntimeError("Unsafe output path")
    sources = [ROOT / name for name in ROOT_FILES]
    for directory in PUBLIC_DIRS:
        sources.extend(path for path in (ROOT / directory).rglob("*") if path.is_file())
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

"""Prepare small reference JPEGs before committing; keep input originals outside Git."""
from pathlib import Path
import argparse
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--component", default="Welle")
    parser.add_argument("--max-edge", type=int, default=1600)
    parser.add_argument("--quality", type=int, default=80)
    args = parser.parse_args()
    if not args.component or Path(args.component).name != args.component or args.component in (".", ".."):
        parser.error("--component must be one folder name")
    if args.max_edge < 256 or not 1 <= args.quality <= 95:
        parser.error("Use --max-edge >= 256 and --quality from 1 to 95")
    dest = ROOT / "evidence/raw" / args.component
    pairs = [(source, dest / (source.stem + ".jpg")) for source in args.files]
    if len({target.name for _, target in pairs}) != len(pairs):
        parser.error("Input filenames would collide")
    for source, target in pairs:
        if not source.is_file():
            parser.error(f"Missing input: {source}")
        if target.exists() or source.resolve() == target.resolve():
            parser.error(f"Refusing to overwrite an existing source: {target}")
    dest.mkdir(parents=True, exist_ok=True)
    for source, target in pairs:
        with Image.open(source) as raw:
            image = ImageOps.exif_transpose(raw).convert("RGB")
            image.thumbnail((args.max_edge, args.max_edge), Image.Resampling.LANCZOS)
            # Exclusive creation prevents replacing an existing source.
            with target.open("xb") as output:
                image.save(output, format="JPEG", quality=args.quality, optimize=True, progressive=True)
        with Image.open(target) as check:
            check.verify()
        print(f"{target.relative_to(ROOT)}: {source.stat().st_size} -> {target.stat().st_size} bytes")

if __name__ == "__main__":
    main()

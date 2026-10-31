#!/usr/bin/env python3
"""Copy the bot's fonts next to the Mini App and write fonts.json, so the page can preview them.

    python miniapp/make_fonts.py          # then upload index.html + fonts.json + fonts/ to your GitHub Pages repo
"""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "fonts"


def label(stem: str) -> str:
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", stem).replace("-", " ").replace("_", " ")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    items = []
    for src in sorted(list((ROOT / "fonts").glob("*.ttf")) + list((ROOT / "fonts").glob("*.otf"))):   # shared fonts only
        shutil.copy2(src, OUT / src.name)
        items.append({"name": src.stem, "label": label(src.stem), "file": src.name})
    (Path(__file__).resolve().parent / "fonts.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(items)} fonts -> {OUT} + fonts.json")


if __name__ == "__main__":
    main()

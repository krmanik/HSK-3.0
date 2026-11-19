#!/usr/bin/env python3
"""Split yct_words.json into one TSV file per YCT level."""

import json
from pathlib import Path

SRC = Path(__file__).parents[2] / "static" / "data" / "yct_words.json"
OUT_DIR = Path(__file__).parents[2] / "HSK-3.0-words-list" / "YCT"

data = json.loads(SRC.read_text(encoding="utf-8"))

for key, words in data.items():
    level_num = key.split("_")[1]
    out_path = OUT_DIR / f"yct_level_{level_num}.tsv"
    lines = [
        f"{w['word']}\t{w['pinyin_tone']}\t{w['meaning']}" for w in words
    ]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"YCT {level_num}: {len(words)} words → {out_path.name}")

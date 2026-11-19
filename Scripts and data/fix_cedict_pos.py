#!/usr/bin/env python3
"""
Correct the part-of-speech columns in static/data/cedict.db.zip.

The SUBTLEX corpus (SUBTLEX_CH_131210_CE.utf8, in this same folder) has multiple
rows per word for homographs. The original DB build picked the wrong
(low-frequency) row for ~327 common single-char words, tagging them `.n.` (Noun)
— e.g. 了 became Noun instead of Particle, 个 instead of Classifier.

This script repopulates `all_PoS` / `dominant_PoS` from each word's
highest-frequency SUBTLEX row (the canonical reading), then re-zips the DB.

Run from anywhere:  python3 "HSK-3.0-words-list/Scripts and data/fix_cedict_pos.py"
"""
import os
import sqlite3
import zipfile
import tempfile
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
# repo root = .../<repo>/HSK-3.0-words-list/Scripts and data/ -> up three levels
ROOT = os.path.dirname(os.path.dirname(HERE))
SUBTLEX = os.path.join(HERE, "SUBTLEX_CH_131210_CE.utf8")
ZIP = os.path.join(ROOT, "static", "data", "cedict.db.zip")

# SUBTLEX columns (tab-separated): 0=word 4=frequency 10=dominant_PoS 12=all_PoS
COL_WORD, COL_FREQ, COL_DOM, COL_ALL = 0, 4, 10, 12


def best_pos_per_word():
    """word -> (dominant_PoS, all_PoS) from the highest-frequency SUBTLEX row."""
    best = {}
    with open(SUBTLEX, encoding="utf-8") as f:
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) <= COL_ALL:
                continue
            w = c[COL_WORD]
            try:
                freq = float(c[COL_FREQ])
            except ValueError:
                continue
            if w not in best or freq > best[w][0]:
                best[w] = (freq, c[COL_DOM], c[COL_ALL])
    return {w: (dom, allp) for w, (_, dom, allp) in best.items()}


def main():
    best = best_pos_per_word()

    tmp = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(ZIP) as z:
            db_name = next(n for n in z.namelist() if n.endswith(".db") and "__MACOSX" not in n)
            z.extract(db_name, tmp)
        db_path = os.path.join(tmp, db_name)

        con = sqlite3.connect(db_path)
        changed = 0
        for simp, allp, dom in con.execute(
            "SELECT simplified, all_PoS, dominant_PoS FROM cedict"
        ).fetchall():
            b = best.get(simp)
            if not b:
                continue
            new_dom, new_all = b
            if (allp or "") != (new_all or "") or (dom or "") != (new_dom or ""):
                con.execute(
                    "UPDATE cedict SET all_PoS = ?, dominant_PoS = ? WHERE simplified = ?",
                    (new_all, new_dom, simp),
                )
                changed += 1
        con.commit()
        con.close()
        print(f"updated {changed} word(s)")

        # Re-zip with just the .db entry (drop the macOS resource fork).
        with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(db_path, "cedict.db")
        print(f"wrote {ZIP}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

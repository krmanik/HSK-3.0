import pandas as pd
import sys
from pathlib import Path


def xlsx_to_txt(xlsx_path: str) -> None:
    path = Path(xlsx_path)
    df = pd.read_excel(path, dtype=str)
    df.fillna("", inplace=True)
    out_path = path.parent.parent / (path.stem + ".txt")
    df.to_csv(out_path, sep="\t", index=False)
    print(f"{path.name} -> {out_path.name} ({len(df)} rows)")


if __name__ == "__main__":
    files = [
        "../BCT/xlsx/BCTA_cihui.xlsx",
        "../BCT/xlsx/BCTB_cihui.xlsx"
    ]
    for f in files:
        xlsx_to_txt(f)

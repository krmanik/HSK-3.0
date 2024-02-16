from dragonmapper import transcriptions, hanzi


def to_zhuyin(file, out_file):
    out = open(out_file, "w", encoding="utf-8")
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            split = line.split("\t")
            pinyin = (
                split[2]
                .replace(" ", "")
                .replace("…", "")
                .replace("ránér", "ránr")
                .replace("cóngér", "cóngr")
                .replace("gōngān", "gōng'ān")
                .replace("chǒngài", "chóng'ài")
                .replace("fèné", "fèn'é")
                .replace("xiōngè", "xiōng'è")
                .replace("zǒngé", "zǒng'é")
                .lower()
            )

            simplified = split[0]
            if len(pinyin) == 1 and pinyin == "ó":
                zhy = "ㄛˊ"
            else:
                zhy = transcriptions.to_zhuyin(pinyin)
            out.write(f"{simplified}\t{zhy}\n")


root = "../HSK list with meaning/"
out_root = "../HSK list with zhuyin/"

# change level to the level you want to convert
level = "1"

to_zhuyin(f"{root}HSK {level}.tsv", f"{out_root}HSK {level}.txt")

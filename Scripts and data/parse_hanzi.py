root = "../HSK Hanzi/"
level = "HSK 2.txt"

with open(f"{root}{level}", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = [char for char in line]
        for char in line:
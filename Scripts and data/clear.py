import os

root = "../HSK list with frequency/"

files = [
    f"{root}HSK 1.txt",
    f"{root}HSK 2.txt",
    f"{root}HSK 3.txt",
    f"{root}HSK 4.txt",
    f"{root}HSK 5.txt",
    f"{root}HSK 6.txt",
    f"{root}HSK 7-9.txt",
]

temp_files = []

for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            words = f.read()
    except Exception as e:
        print(f"Error reading file {file}: {e}")
        continue

    name = file.split(" ")[4]
    temp_file = f"{root}HSK_{name}"
    temp_files.append(temp_file)

    with open(temp_file, "a", encoding="utf-8") as temp_f:
        words_arr = words.split("\n")
        for word_line in words_arr:
            word = word_line.split("\t")[0] + "\n"
            temp_f.write(word)

print("Temp files created:", temp_files)

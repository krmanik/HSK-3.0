import os

def clear_freq_files():
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

def clear_hanzi():
    root = "../HSK Hanzi/"

    files = [
        f"{root}HSK 1.txt",
        f"{root}HSK 2.txt",
        f"{root}HSK 3.txt",
        f"{root}HSK 4.txt",
        f"{root}HSK 5.txt",
        f"{root}HSK 6.txt",
        f"{root}HSK 7-9.txt",
    ]

    temp_files = [
        f"{root}temp/HSK 1_temp.txt",
        f"{root}temp/HSK 2_temp.txt",
        f"{root}temp/HSK 3_temp.txt",
        f"{root}temp/HSK 4_temp.txt",
        f"{root}temp/HSK 5_temp.txt",
        f"{root}temp/HSK 6_temp.txt",
        f"{root}temp/HSK 7-9_temp.txt",
    ]

    for i in range(len(temp_files)):
        try:
            with open(temp_files[i], "r", encoding="utf-8") as f:
                lines = f.readlines()
                
                for line in lines:
                    for word in line:
                        print(word)
                        if word == "\n" or word == " " or word == "":
                            continue
                        else:
                            print(word)
                            with open(files[i], "a", encoding="utf-8") as fi:
                                word = word + "\n"
                                fi.write(word)
        except Exception as e:
            print(f"Error reading file {files[i]}: {e}")
            continue

def clear_handwritten():
    root = "../HSK Handwritten/"

    files = [
        f"{root}Elementary.txt",
        f"{root}Medium.txt",
        f"{root}Advanced.txt",
    ]

    temp_files = [
        f"{root}temp/Elementary_temp.txt",
        f"{root}temp/Medium_temp.txt",
        f"{root}temp/Advanced_temp.txt",
    ]

    for i in range(len(temp_files)):
        try:
            with open(temp_files[i], "r", encoding="utf-8") as f:
                lines = f.readlines()
                
                for line in lines:
                    for word in line:
                        print(word)
                        if word == "\n" or word == " " or word == "":
                            continue
                        else:
                            print(word)
                            with open(files[i], "a", encoding="utf-8") as fi:
                                word = word + "\n"
                                fi.write(word)
        except Exception as e:
            print(f"Error reading file {files[i]}: {e}")
            continue

# clear_freq_files()
# clear_hanzi()
# clear_handwritten()
def sort_file(first, second, level):

    with open(first, 'r', encoding="utf-8") as f1:
        words = [line.strip().split("	")[0] for line in f1]

    out = open("temp/HSK-freq-" + level + ".txt", "w", encoding="utf-8")

    with open(second, 'r', encoding="utf-8") as f2:
        for line in f2:
            l = line.strip().split("	")
            if len(l) == 2:
                word, value = line.strip().split("	")
                if word in words:
                    word = word + "	" + str(value) + "\n"
                    out.write(word)
                    print(word)


def sort_file2(first, second, level):

    with open(first, 'r', encoding="utf-8") as f1:
        words = [line.strip().split("	")[0] for line in f1]

    out = open("temp/SUBTLEX-HSK-freq-" + level + ".txt", "w", encoding="utf-8")

    with open(second, 'r', encoding="utf-8") as f2:
        new_words = []
        for line in f2:
            line = line.strip().split("	")
            word = line[0]
            value = line[4]
            if word in words:
                if word not in new_words:
                    new_words.append(word)
                    word = word + "	" + str(value) + "\n"
                    out.write(word)
                    print(word)


def not_found_in_freq_list(level, subtlex=""):
    out = open("temp/" + subtlex + "not-found-" + level + ".txt", "w", encoding="utf-8")
    with open("../../HSK list with zhuyin/zhuyin/HSK " + level + " with zhuyin.tsv", "r", encoding="utf-8") as orig:
        lines = orig.readlines()

        with open("temp/" + subtlex + "HSK-freq-" + level + ".txt", "r", encoding="utf-8") as f:
            test = f.readlines()

            lst = []

            for test_line in test:    
                lst.append(test_line.split("	")[0].strip())

            for orig_line in lines:
                if orig_line.split("	")[0].strip() not in lst:
                    o = orig_line.split("	")[0].strip() + "\n"
                    # print(orig_line.split("	")[0].strip())
                    out.write(o)


def extract_frequency():
    for level in LEVEL:
        HSK_TSV = "../../HSK list with zhuyin/zhuyin/HSK " + level + " with zhuyin.tsv"

        # sort_file(HSK_TSV, FREQ_FILE1, level)
        # not_found_in_freq_list(level)

        sort_file2(HSK_TSV, FREQ_FILE2, level)
        not_found_in_freq_list(level, "SUBTLEX-")


def extract_frequency_for_not_found(first, second, level):
    with open(first, 'r', encoding="utf-8") as f1:
        words = [line.strip().split("\n")[0] for line in f1]

    out = open("temp/new-found-HSK-freq-" + level + ".txt", "w", encoding="utf-8")

    with open(second, 'r', encoding="utf-8") as f2:
        for line in f2:
            l = line.strip().split("	")
            if len(l) == 2:
                word, value = line.strip().split("	")
                if word in words:
                    word = word + "	" + str(value) + "\n"
                    out.write(word)
                    print(word)


def new_not_found(level):
    NEW_FOUND_FILE = "temp/new-found-HSK-freq-" + level + ".txt"
    NOT_FOUND_FILE = "temp/SUBTLEX-not-found-" + level + ".txt"

    with open(NEW_FOUND_FILE, 'r', encoding="utf-8") as f1:
        words = [line.strip().split("	")[0] for line in f1]

    out = open("temp/new-not-found-HSK-freq-" + level + ".txt", "w", encoding="utf-8")

    with open(NOT_FOUND_FILE, 'r', encoding="utf-8") as f2:
        for line in f2:
            word = line.strip().split("\n")[0]
            if word not in words:
                word = word + "	0\n"
                out.write(word)
                print(word)


def merge_new_found_and_sort(level):
    FOUND_FILE = "temp/SUBTLEX-HSK-freq-" + level + ".txt"
    NEW_FOUND_FILE = "temp/new-found-HSK-freq-" + level + ".txt"

    with open(FOUND_FILE, 'r', encoding="utf-8") as file1:
        file1_contents = file1.read()

    with open(NEW_FOUND_FILE, 'r', encoding="utf-8") as file2:
        file2_contents = file2.read()

    merged_contents = file1_contents + file2_contents
    lines = merged_contents.strip().split('\n')
    tuples = [(line.split('\t')[0], int(line.split('\t')[1])) for line in lines]
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)
    sorted_lines = [f"{t[0]}\t{t[1]}\n" for t in sorted_tuples]

    with open('temp/SUBTLEX-Merged-' + level + '.txt', 'w', encoding="utf-8") as file3:
        file3.writelines(sorted_lines)


def merge_not_found_and_sort(level):
    FOUND_FILE = "temp/SUBTLEX-Merged-" + level + ".txt"
    NOT_FOUND_FILE = "temp/new-not-found-HSK-freq-" + level + ".txt"

    with open(FOUND_FILE, 'r', encoding="utf-8") as file1:
        file1_contents = file1.read()

    with open(NOT_FOUND_FILE, 'r', encoding="utf-8") as file2:
        file2_contents = file2.read()

    merged_contents = file1_contents + file2_contents

    with open('Final-Merged-' + level + '.txt', 'w', encoding="utf-8") as file3:
        file3.writelines(merged_contents)


def create_hsk_word_list(level):
    FREQ_FILE = "Final-Merged-" + level + ".txt"
    # HSK_FILE = "../../HSK list with zhuyin/zhuyin/HSK " + level + " with zhuyin.tsv"
    HSK_FILE = "../../HSK list with meaning/Anki xiehanzi__HSK " + level + ".txt"
    FINAL_FILE = "../../HSK list with frequency/HSK " + level + " with frequency.tsv"

    with open(HSK_FILE, "r", encoding="utf-8-sig") as file1:
        file1_contents = file1.readlines()

    with open(FREQ_FILE, "r", encoding="utf-8-sig") as file2:
        file2_contents = [line.strip().split("	")[0] for line in file2.readlines()]

    sorted_lines = sorted(file1_contents, key=lambda line: file2_contents.index(line.split("	")[0]))

    with open(FINAL_FILE, 'w', encoding="utf-8-sig") as file3:
        file3.writelines(sorted_lines)


LEVEL = ["1", "2", "3", "4", "5", "6", "7-9"]
FREQ_FILE1 = "../../blog_lit_news_tech_weibo_freq.release_sorted.txt"
FREQ_FILE2 = "../../SUBTLEX_CH_131210_CE.utf8"


# extract_frequency()


# for level in LEVEL:
#     FILE = "SUBTLEX-not-found-" + level + ".txt"
#     extract_frequency_for_not_found(FILE, FREQ_FILE1, level)


# for level in LEVEL:
#     new_not_found(level)


# for level in LEVEL:
#     new_not_found(level)


# for level in LEVEL:
#     merge_new_found_and_sort(level)


# for level in LEVEL:
#     merge_new_found_and_sort(level)


# for level in LEVEL:
#     merge_not_found_and_sort(level)


# for level in LEVEL:
#     create_hsk_word_list(level)

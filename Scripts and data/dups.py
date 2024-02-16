from collections import defaultdict

def find_dups(file):
    with open(file, "r", encoding="utf-8") as f:
        words = f.read()

    words_arr = words.split("\n")
    sorted_arr = sorted(words_arr)
    results = []

    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i + 1] == sorted_arr[i]:
            results.append(sorted_arr[i].strip())

    print(f"Duplicates in file '{file}'\n", results)
    print("Total: ", len(results))
    print("-------------------\n")

    # Save results to a file
    output_file = f"duplicates.txt"
    with open(output_file, "a", encoding="utf-8") as output_f:
        output_f.write(f"Duplicates in file '{file}'")
        output_f.write("\n--------------------------------------------\n")
        output_f.write("\n".join(results))
        output_f.write("\n-------------------\n")

    print(f"Results saved to '{output_file}'\n")


def find_and_save_common_words(file_paths, output_file):
    word_occurrences = defaultdict(list)

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = set(file.read().split())
            for word in words:
                word_occurrences[word].append(file_path)

    common_words = {word: files for word, files in word_occurrences.items() if len(files) > 1}

    with open(output_file, 'w', encoding='utf-8') as file:
        for word, files in common_words.items():
            files = ', '.join(files).replace(root, '').replace('.txt', '')
            file.write(f"{word} [{files}]\n")


root = "../HSK List/"

files = [
    f"{root}HSK 1.txt",
    f"{root}HSK 2.txt",
    f"{root}HSK 3.txt",
    f"{root}HSK 4.txt",
    f"{root}HSK 5.txt",
    f"{root}HSK 6.txt",
    f"{root}HSK 7-9.txt",
]

for file in files:
    find_dups(file)

output_file = f"duplicates_across_files.txt"

find_and_save_common_words(files, output_file)
print(f'Common words across files saved to {output_file}')

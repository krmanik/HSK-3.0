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

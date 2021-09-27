# Before running this run index.js

# Take Traditional, Simplified and Pinyin from Pleco export and meaning from existing data
def add_meaning(filename):
    out = open("new/"+ filename +".tsv", "w", encoding="utf-8")
    with open("pinyin/" + filename + "-pinyin.txt", "r", encoding="utf-8") as f1:
        with open("old/" + filename + ".tsv", "r", encoding="utf-8") as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            for l1 in lines1:
                for l2 in lines2:
                    split1 = l1.strip().split("\t")
                    split2 = l2.strip().split("\t")

                    if split1[0] == split2[0] or split1[1] == split2[1]:
                        new_data = split1[0] + "\t" + split1[1] + "\t" + split1[2] + "\t" + split2[3] + "\n"
                        print(new_data)
                        out.write(new_data)

# change 1 to 7-9
add_meaning("HSK7-9")

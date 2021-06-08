import json
import pinyin
import pinyin_jyutping_sentence
from hanziconv import HanziConv
from googletrans import Translator
from cedict.pinyin import pinyinize

# cedict meaning in json format
with open("all_cedict.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# create word meaning list
def get_meaning():
    # for not repeat of chars, in list only one word/character to prevent duplicate in list
    inserted = []

    # change HSK ? -> 1,2,3,4,5,6,7-9
    # e.g. HSK 1 with clear meaning.txt, HSK 2 with clear meaning.txt, HSK 7-9 with clear meaning.txt...
    # write to HSK 7-9 with clear meaning.txt
    out = open("HSK 7-9 with clear meaning.txt", "w", encoding="utf-8") 

    # read list characters/words one per line
    with open("HSK 7-9.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            char = line.strip()
            # read 10k words from wiktionary
            with open("10k Mandarin.txt", "r", encoding="utf-8") as f2:
                lines2 = f2.readlines()
                found = False
                for l2 in lines2:
                    sp = l2.split(",")[1].strip()
                    if sp  == char:
                        if char not in inserted:
                            inserted.append(char)
                            print(l2)
                            out.write(l2)
                            found = True

                # not found in wiktionary 10k
                # get meaning from all_cedict.json
                if not found:
                    found = False
                    try:
                        ch_pin = ""
                        ch_mean = ""
                        for p in data[char]["pinyin"]:
                            ch_pin += pinyinize(p) + ", "
                        ch_pin = ch_pin.strip().rstrip(",")

                        for x in [1,2,3,4,5]:
                            if str(x) in ch_pin:
                                # convert to numeric pinyin to pinyin tone
                                ch_pin = pinyin_jyutping_sentence.pinyin(char)
                                break

                        for d in data[char]["definitions"]:
                            ch_mean += data[char]["definitions"][d]
                        
                        ch_mean = ch_mean.replace(";", ",")
                        ch_mean = ch_mean.strip().rstrip(",")
                        
                        ch_data = data[char]["traditional"] + "," + data[char]["simplified"] + "," + ch_pin + ',"' + ch_mean + '"\n'
                        
                        if char not in inserted:
                            inserted.append(char)
                            print(ch_data)
                            out.write(ch_data)

                    except:
                        # exception occurs the characters not in json as well as 10k Mandarin
                        # get meaning using google translate
                        print(char+" not found in 10k and cedict, fetching online")
                        translator = Translator()
                        t = translator.translate(char, src='zh-cn', dest="en")
                        ch_mean = t.text

                        ch_pin = pinyin_jyutping_sentence.pinyin(char)
                        ch_trad = HanziConv.toTraditional(char)

                        ch_data = ch_trad + "," + char + "," + ch_pin + ',"' + ch_mean + '"\n'

                        if char not in inserted:
                            inserted.append(char)
                            print(ch_data)
                            out.write(ch_data)

# find duplicates in list
# change path e.g. HSK 1.txt, HSK 2.txt, HSK 7-9.txt...
def find_dup():
    with open("HSK 7-9.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            if line.strip() not in data:
                data.append(line.strip())
            else:
                print(line)
                
# add sound field in Anki format:- [sound:cmn-爱.mp3] to list
# change path e.g. tsv/HSK 1.txt, tsv/HSK 2.txt, tsv/HSK 7-9.txt...
def get_sound():
    out = open("tsv/HSK 7-9 with sound.tsv", "w", encoding="utf-8")
    with open("tsv/HSK 7-9.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            sp = line.split("\t")
            #print(sp)
            char = sp[1]
            sound = "[sound:cmn-"+ char +".mp3]"
            ln = line.strip() + "\t" + sound + "\n"
            print(ln)
            out.write(ln)

# count fields in every row, it help in fixing errors when before importing in Anki
def count_field():
    with open("tsv/HSK 7-9.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            sp = line.split("\t")
            if len(sp) != 4:
                print(sp)
            

# uncomment below and run
# get_meaning()


# some other helper functions
# find_dup()

# get_sound()
# count_field()

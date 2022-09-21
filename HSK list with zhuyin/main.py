from dragonmapper import transcriptions
from bs4 import BeautifulSoup

def meaning_generate():
    out = open("hsk/HSK 6.tsv", "w", encoding="utf-8")
    with open("HSK 6.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            split = line.split("\t")
            pinyin = split[2].split(',')
            simplified = split[0]
            meaning = split[4].split("<div class='meaning'>")
            meaning = list(filter(None, meaning))
            
            char_tone_list = []
            j=0
            for pin in pinyin:
                char_tone = ''
                tone = pin.split('<span class="t')
                i=0
                for to in tone:
                    if to[0].isdigit():
                        print(to)
                        char_tone += '<span class="char-tone' + to[0] + '">' + simplified[i] + '</span>'
                        i+=1
                
                #char_tone = '<div class="pinyin">' + char_tone + '<div class="meaning">' + meaning[j]
                j+=1
                char_tone = '<div class="char">' + char_tone + '</div><div class="pinyin">' + pin + "</div>"
                char_tone_list.append(char_tone)
            k=0
            result = split[0] + "\t" + split[1] + "\t" + split[2] + "\t" + split[3] + "\t"
            char_mean = ""
            for ct in char_tone_list:
                char_mean += ct + "<div class='meaning'>" + meaning[k]
                k+=1
            
            result += char_mean
            out.write(result)

out1 = open("zhuyin/HSK 7-9 with zhuyin.tsv", "w", encoding="utf-8")
def add_zhuyin():
    with open("hsk/HSK 7-9.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            split = line.split("\t")
            pinyin = split[2].split(",")
            #print(split[2])
            zy = ""
            zhy_list = []
            for pin in pinyin:
                pin = BeautifulSoup(pin).text.strip()
                if pin == 'o' or pin == 'ó' or pin == 'ò':
                    print(zhy)
                    continue
                
                #print(pin, split[0])
                zhy = transcriptions.to_zhuyin(pin.lower())
                if zhy.strip() not in zhy_list:
                    zhy_list.append(zhy.strip())
                    zy += '<span class="zhuyin">' + zhy + "</span>"
            
            result = split[0] + "\t" + split[1] + "\t" + split[2] + "\t" + zy + "\t" + split[3] + "\t" + split[4]
            print(result)
            out1.write(result)

# meaning_generate()
# add_zhuyin()
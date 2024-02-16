# HSK 3.0 words list

The words list with meaning generated using
- [word list shared by Pleco](https://plecoforums.com/threads/hsk-3-0-flashcards.6706/)
- [CC-CEDICT](https://cc-cedict.org/wiki/)
- [cedict-json](https://github.com/krmanik/cedict-json)
- [Anki Chinese Vocabulary Generator](https://github.com/krmanik/Anki-Chinese-Vocabulary-Generator)
- [wiktionary, Mandarin Frequency lists](https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists)

## How it generated?
The meanings in `HSK list with meaning` taken in following order
1. if found in `wiktionary` then get meaning
2. else take meaning from `CC-CEDICT` 
3. if not found then translate using Google Translate

## HSK Grammar
- [HSK Grammar](https://github.com/krmanik/HSK-3.0-words-list/tree/main/HSK%20Grammar)

The Grammar OCRed using Foxit Reader and Microsoft Snipping tool. It may contain some errors.

## HSK Hanzi

- [HSK Hanzi](https://github.com/krmanik/HSK-3.0-words-list/tree/main/HSK%20Hanzi)

## Scripts and data
The [Scripts and data](https://github.com/krmanik/HSK-3.0-words-list/tree/main/Scripts%20and%20data) contains files that used to create HSK 3.0 lists.

The [main.py](https://github.com/krmanik/HSK-3.0-words-list/blob/main/Scripts%20and%20data/main.py) is used to create HSK 3.0 word list with meaning. The script is not so optimized, it may need improvements.

### Data
The following data used to generate list
- [10k Mandarin from wiktionary](https://github.com/krmanik/HSK-3.0-words-list/blob/main/Scripts%20and%20data/10k%20Mandarin.txt)
- [all_cedict.json](https://github.com/krmanik/HSK-3.0-words-list/blob/main/Scripts%20and%20data/all_cedict.json)
- HSK 1.txt to HSK 7-9.txt (view in the folder)

The following data generated (view in the folder)
- HSK 1 to HSK 7-9 with clear meaning .txt files 
- tsv list for importing in Anki

### For running the script
1. Install Python
2. Install following python modules using `pip`

```
pinyin
pycedict
hanziconv
googletrans
pinyin_jyutping_sentence
```
3. The script reads characters/words per line and fetch meaning. Then it write the data .txt files
4. Uncomment functions to use the script
```
# uncomment below and run
# get_meaning()


# some other helper functions
# find_dup()

# get_sound()
# count_field()
```

## Find duplicates
```
cd HSK-3.0-words-list/Scripts and data/
python dups.py
```

## Generate Zhuyin
```
cd HSK-3.0-words-list/Scripts and data/
python to_zhuyin.py
```

### Note:
- The meaning translated using Google when not found in CC-CEDICT.
- This generated using python program, may contain errors and need improvements.

### License
View [License](License.md)
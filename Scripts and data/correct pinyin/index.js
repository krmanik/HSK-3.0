// Convert to Number to Tone marks 
// Arrange in Traditional, Simplified and Pinyin (Tone Marks)
// These file will be used in merge.py
// Change number in HSK1 to 1,2,3,4,5,6,7-9

var PinyinConverter = require('./pinyin_converter.js')
const fs = require('fs');
const readline = require('readline');

function convert(filename) {
    var rd = readline.createInterface({
        input: fs.createReadStream(filename + '.txt'),   // change 1 to 7-9
        output: process.stdout,
        console: false
    });
    
    rd.on('line', function(line) {
        data = line.trim().split("\t")
        pinyin = PinyinConverter.convert(data[2])
        new_line = data[1] + "\t" + data[0] + "\t" + pinyin + "\n"
        
        console.log(new_line);
        // change 1 to 7-9
        fs.appendFile("pinyin/" + filename + '-pinyin.txt', new_line, function (err) {
            if (err) throw err;
          });
    });
}

// change 1 to 7-9
convert("HSK1")
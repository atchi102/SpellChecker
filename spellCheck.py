from __future__ import division
from enchant.checker import SpellChecker

import enchant
import os



def SpellCheck(contents, filename):
    print("FILE " + filename)

    count = 0

    chkr = SpellChecker("en_US")
    chkr.set_text(contents)
    for err in chkr:
        contents = contents.replace(str(err.word),"*"+str(err.word)+"*")

    print contents
    newChkr = SpellChecker("en_US")
    newChkr.set_text(contents)
    d = enchant.Dict("en_US")
    for err in newChkr:
        print("ERROR: " + err.word)
        print(d.suggest(err.word))
        replaceWith = raw_input('Enter correction: ')
        contents = contents.replace(str(err.word),str(replaceWith))
        count+=1

    numWords = len(contents.split())
    return {'contents':contents, 'errors':count, 'numWords':numWords}


directory = "/Users/abigailatchison/Desktop/MLAT/RTFProcessing/EssaysTxt/test"
storePercent = open(os.path.join(directory + "/Output", "stats.txt"),'w')
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        #print(os.path.join(directory, filename))
        log = open(os.path.join(directory, filename), 'r')
        fileContents = log.read()

        results = SpellCheck(fileContents, filename)

        newFile = open(os.path.join(directory + "/Output", filename),'w')
        newFile.truncate()
        newFile.write(results['contents'])
        newFile.close()

        print("Total words: " + str(results['numWords']))
        print("Total errors: " + str(results['errors']))
        print("Percentage errors: " + str(results['errors']/results['numWords']))


        storePercent.write(str(results['errors']/results['numWords'])+ "\n")


        continue
    else:
        continue

storePercent.close()

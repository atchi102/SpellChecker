from enchant.checker import SpellChecker
import enchant
import os



def SpellCheck(contents, count, filename):
    print("FILE " + filename)

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

    return {'contents':contents, 'errors':count}


directory = "/Users/abigailatchison/Desktop/MLAT/RTFProcessing/EssaysTxt/test"
numErrs = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        #print(os.path.join(directory, filename))
        log = open(os.path.join(directory, filename), 'r')
        fileContents = log.read()

        results = SpellCheck(fileContents, numErrs, filename)

        newFile = open(os.path.join(directory + "/Output", filename),'w')
        newFile.truncate()
        newFile.write(results['contents'])
        newFile.close()


        continue
    else:
        continue

print("NUM ERRORS: " + str(numErrs))

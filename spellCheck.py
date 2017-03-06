from enchant.checker import SpellChecker
import os



def SpellCheck(contents, count):
    chkr = SpellChecker("en_US")
    chkr.set_text(contents)
    for err in chkr:
        count+=1
    return count



directory = "/Users/abigailatchison/Desktop/MLAT/RTFProcessing/EssaysTxt"
numErrs = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        #print(os.path.join(directory, filename))
        log = open(os.path.join(directory, filename), 'r')
        fileContents = log.read()
        numErrs = SpellCheck(fileContents, numErrs)

        continue
    else:
        continue

print("NUM ERRORS: " + str(numErrs))

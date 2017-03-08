from __future__ import division
from enchant.checker import SpellChecker

import enchant
import os


#Run PyEnchant on contents
def SpellCheck(contents, filename):
    print("FILE " + filename)

    #Var to keep track of number of errors
    count = 0

    contentsStarred = contents
    #Run through errors and mark them with *
    chkr = SpellChecker("en_US")
    chkr.set_text(contentsStarred)
    for err in chkr:
        contentsStarred = contentsStarred.replace(str(err.word),"**"+str(err.word)+"**")

    print contentsStarred

    #Run through errors and correct them with user input
    newChkr = SpellChecker("en_US")
    newChkr.set_text(contents)
    d = enchant.Dict("en_US")
    for err in newChkr:
        print("ERROR: " + err.word)
        print(d.suggest(err.word))
        replaceWith = raw_input('Enter correction: ')
        #If user input is a "y" then keep the word otherwise change
        if replaceWith!="y":
            contents = contents.replace(str(err.word),str(replaceWith))
            count+=1

    #Number of words in the text file
    numWords = len(contents.split())
    #Return the corrected contents, number of errors, number of words in the doc
    return {'contents':contents, 'errors':count, 'numWords':numWords}


#Directory of the text file essays
directory = "/Users/abigailatchison/Desktop/MLAT/RTFProcessing/EssaysTxt"

#Open a file to place percentages in a text file
storePercent = open(os.path.join(directory + "/Output", "stats.txt"),'r')
statsContent = storePercent.read()
storePercent.close()


#Loop through all text files
for filename in os.listdir(directory):


    if filename.endswith(".txt"):
        if filename in statsContent:
            continue;
        #Open text file and read in contents
        f = open(os.path.join(directory, filename), 'r')
        fileContents = f.read()

        results = SpellCheck(fileContents, filename)

        #Place corrected files in the output file
        newFile = open(os.path.join(directory + "/Output", filename),'w')
        newFile.truncate()
        newFile.write(results['contents'])
        newFile.close()

        print("Total words: " + str(results['numWords']))
        print("Total errors: " + str(results['errors']))
        if results['numWords'] == 0:
            print("Percentage errors: " + "0.0")
            #Write percentages to document and save file
            storePercent = open(os.path.join(directory + "/Output", "stats.txt"),'a')
            storePercent.write("\n" + filename + " :: " + "0.0")
            storePercent.close()
        else:
            print("Percentage errors: " + str(results['errors']/results['numWords']))
            #Write percentages to document and save file
            storePercent = open(os.path.join(directory + "/Output", "stats.txt"),'a')
            storePercent.write("\n" + filename + " :: " + str(results['errors']/results['numWords']))
            storePercent.close()




        continue
    else:
        continue

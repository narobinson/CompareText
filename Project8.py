## @author Nasi Robinson
## The file compares all the nouns in the text files in the folder and shows 
## which nouns are shared by each text file. It also shows the most common nouns used in each


import sys
import nltk


def count(dictionaries):
    
    i = 0
    placeholder = 0
    nouns = [0] * 45
    notShared = [0] * 45
    sharedNouns = [[] for x in range(46)]
    nonSharedNouns = [[] for x in range(46)]
    for dictionary in dictionaries:
        length = 9
        j = placeholder
        while j < length:
            for word in dictionary:
                if word in dictionaries[j+1]:
                    nouns[i] += 1
                    sharedNouns[i].append(word)
                else:
                    notShared[i] += 1
                    nonSharedNouns[i].append(word)
            j+= 1
            i+= 1
        placeholder+=1

    index = 0
    for numbers in nouns:
        if index < 9:
            print "\n\n*********Documents 1 and", (index + 2), "share:", numbers, "words*************"
            print sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]

        if index >= 9 and index < 17:
            print "\n\n*********Documents 2 and", (index % 9 + 3), "share:", numbers, "words*********"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]
        
        if index >= 17 and index < 24:
            print "\n\n*********Documents 3 and", (index % 17 + 4), "share:", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]

        if index >= 24 and index < 30:
            print "\n\n*********Documents 4 and", (index %24 + 5), "share:", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]


        if index >= 30 and index < 35:
            print "\n\n*********Documents 5 and", (index % 30 + 6), "share:", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]
        
        if index >= 35 and index < 39:
            print "\n\n*********Documents 6 and", (index % 35 + 7), "share:", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]

        if index >= 39 and index < 42:
            print "\n\n*********Documents 7 and", (index % 39 + 8), "share:", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]

        if index >= 42 and index < 44:
            print "\n\n*********Documents 8 and", (index % 42 + 9), "share:", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]

        if index + 1 > 44:
            print "\n\n*********Documents 9 and 10", "share: ", numbers, "words*************"
            print  sharedNouns[index]
            print "*********", "Do not share: ", len(nonSharedNouns[index]), "words**************"
            print  nonSharedNouns[index]

        

        index += 1


file = open("files.txt","r").readlines()


storys = list()

for fables in file:
    storys.append(open(fables.replace("\n","")
, "r").read())



dictionaries = list()
dictionariesNouns = list()
for story in storys:
    tokens = nltk.word_tokenize(story)
    tagged = nltk.pos_tag(tokens)
    rowNouns = list()
    rowWords = list()
    for words in tagged:
        if words[0] in rowWords:
            continue
        else:
            rowWords.append(words[0])
        if words[1][0] == 'N':
            if words[0] in rowNouns:
                continue
            else:
                rowNouns.append(words[0])
    rowNouns.sort()
    rowWords.sort()
    dictionaries.append(rowWords)
    dictionariesNouns.append(rowNouns)
i = 0
placeholder = 0
nouns = [0] * 45

for dictionary in dictionaries:
    print dictionary
    print "-------------------------"


count(dictionaries)
count(dictionariesNouns)






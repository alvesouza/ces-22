import string
def cleanword(word):
    char = string.ascii_letters
    cleanedWord = ""
    for x in word:
        if x in char:
            cleanedWord += x
    return cleanedWord
def has_dashdash(word):
    if "--" in word:
        return True
    return False
def extract_words(word):
    char = string.ascii_letters
    wordList = []
    addString = ""
    n = len(word)
    for x in word:
        if x in char:
            x = x.lower()
            addString += x
        else:
            if addString == "":
                continue
            else:
                wordList.append(addString)
                addString = ""
    if not addString == "":
        wordList.append(addString)
    return wordList

def wordcount(word,List):
    n = 0
    for x in List:
        if x == word:
            n += 1
    return n

def wordset(List):
    newList = []
    for x in List:
        if x in newList:
            continue
        else:
            newList.append(x)
    newList.sort()
    return newList#.sort()

def longestword(List):
    n = 0
    for x in List:
        a = len(x)
        if a > n:
            n = a
    return n
myFile = open('wordleDictionary.txt')

import numpy as np

def dictionaryMaker(myFile):
    indexOccurance = {}
    letterTotal = {}
    wordTotal = {}
    letterScore = {}
    indexScore = {}
    words = {}
    for line in myFile:
        array = np.array(['s','t','a','r','t'])
        word = line.strip()
        letterSet = set(word)
        
        if word not in words:
            words[word] = 0
        
        for letter in letterSet:
            if letter not in wordTotal:
                wordTotal[letter] = 0
            wordTotal[letter] += 1
            
        for index in range(5):
            array[index] = word[index]
            
        for index in range(5):           
            if array[index] not in indexOccurance:
                indexOccurance[array[index]] = np.zeros(5)
            indexOccurance[array[index]][index] += 1
    
    for key in indexOccurance:
        letterTotal[key] = sum(indexOccurance[key])
    
    for key in wordTotal:
        letterScore[key] = (letterTotal[key]) / (wordTotal[key])**.5
    
    for key in indexOccurance:
        indexOccurance[key] /= sum(indexOccurance[key])
    
    for key in indexOccurance:
        indexScore[key] = indexOccurance[key] * letterScore[key]
    return indexScore, words

x = dictionaryMaker(myFile)
# for key in a[0]:
#     print(key, a[0][key])

def wordScore(word, indexScore):
    score = 0
    for index in range(5):
        score += indexScore[word[index]][index]
    return score

def guessesRefine(guesses, indexScore):
    for word in guesses:
        guesses[word] = wordScore(word, indexScore)
    return guesses
    
scoreBank = guessesRefine(x[1], x[0])

def refineOne(badLetters, scoreBank):
    '''return: words without used letters
    parameter: 
        badLetters - used letters that are not in the word
        scoreBank - dictionary of words with scores
    '''
    refine1 = {}
    for word in scoreBank:
        valid = True
        for letter in word:
            if letter in badLetters:
                valid = False
        if valid == True:
            refine1[word] = scoreBank[word]
    return refine1

def refineTwo(rwLetters, refine1):
    '''return: words without used good letters in the same place
    parameter: 
        rwLetters - a list of tuples (letter, index)
        refine1 - dictionary of words gone through refineOne
    '''
    refine2 = {}
    for key in refine1:
        valid = True
        for letter in rwLetters:
            if letter[0] == key[letter[1]]:
                valid = False
            if letter[0] not in set(key):
                valid = False
        if valid:
            refine2[key] = refine1[key]
    return refine2

def refineThree(rLetters, refine2):
    refine3 = {}
    for key in refine2:
        valid = True
        for letter in rLetters:
            if letter[0] != key[letter[1]]:
                valid = False
        if valid == True:
            refine3[key] = refine2[key]
    return refine3

def refineFour(letterLimits, refine3):
    refine4 = {}
    for key in refine3:
        valid = True
        for letter in letterLimits:
            count = letter[0]
            if count != key.count(letter[1]):
                valid = False
        if valid == True:
            refine4[key] = refine3[key]
    return refine4    

def dilution(guesses):
    # singleLetters = input('Enter all of the letters that only occur once: ')
    wrong = set(input('Enter the letters that were wrong (ex. asdf): '))
    maybe = input('Enter the right letter wrong spots paired with index (ex. p0u1p2p3y5): ')
    correct = input('Enter the right letters paired with index (ex. p0u1p2p3y4): ')
    letterCount = input('Optional - enter how many of some letters there are (ex. 4 "l"s -> 4l): ')
    
    letterPairs = []
    for index in range(0,len(letterCount),2):
        letterPairs.append((int(letterCount[index]), letterCount[index + 1]))
        
    maybePairs = []
    for index in range(0,len(maybe),2):
        maybePairs.append((maybe[index], int(maybe[index + 1])))
        
    correctPairs = []
    for index in range(0,len(correct),2):
        correctPairs.append((correct[index], int(correct[index + 1])))
        
    a = refineOne(wrong, guesses)
    b = refineTwo(maybePairs, a)
    c = refineThree(correctPairs, b)
    d = refineFour(letterPairs, c)
    return d

def maxDifLetters(dilution):
    '''return: the set of letters that should be used when eliminating guesses
    parameter: refined guesses   
    '''
    letterCounts = {} #counts of all the letters
    counts = {} #letters with a certain count
    for word in dilution:
        letterSet = set(word)
        for letter in letterSet:
            if letter not in letterCounts:
                letterCounts[letter] = 0
            letterCounts[letter] += 1
    
    for key in letterCounts:
        if letterCounts[key] not in counts:
            counts[letterCounts[key]] = ''
        counts[letterCounts[key]] += key
    
    possibleCounts = list(counts.keys())
    possibleCounts.sort()
    returnSet = set()
    for i in possibleCounts:
        if len(returnSet) < 4:
            for j in counts[i]:
                if len(returnSet) < 4:
                    returnSet.add(j)
    return returnSet
    
def wordPick(scoreBank, letter, guessedLetters):
    '''return: a word that has the most letters in given letter set
    parameter: the list of words, and letter set
    '''
    bestWord = ''
    maxCount = -20
    for word in scoreBank:
        count = 0
        for i in set(word):
            if i in letter:
                count += 1
            if i in guessedLetters:
                count -= 1       
        if count > maxCount:
            maxCount = count
            bestWord = word
    return bestWord 
    
def earlyPick(guessedLetters, scoreBank):
    '''return: a word without any guessed letters
    parameter: the current guessed letters and the bank of total words
    '''
    goodWords = {}
    for key in scoreBank:
        valid = True
        for letter in key:
            if letter in guessedLetters:
                valid = False
        if valid:
            goodWords[key] = scoreBank[key]
    return goodWords

def maxScore(bankOfwords):
    maxScore = -1
    wordPick = ''
    for word in bankOfwords:
        if bankOfwords[word] > maxScore:
            maxScore = bankOfwords[word]
            wordPick = word
    return wordPick
    

def bestWord(guesses, scoreBank, guessedLetters):
    if len(guesses) == len(scoreBank):
        word = maxScore(scoreBank)
    elif len(guesses) > 60:
        word = maxScore(earlyPick(guessedLetters, scoreBank))
    elif len(guesses) > 30:
        word = maxScore(guesses)
    elif len(guesses) > 3:
        word = wordPick(scoreBank, maxDifLetters(guesses), guessedLetters)
    else:
        word = guesses
    return word

letterSoFar = set()
test = 1
guess = bestWord(scoreBank, scoreBank, letterSoFar)
print("Enter '{}' as your first word.".format(guess))
b = dilution(scoreBank)
while test == 1:
    if len(b) <= 2:
        test = 0
    for letter in guess:
        letterSoFar.add(letter)
    guess = bestWord(b, scoreBank, letterSoFar)
    print('Number of guesses: {}'.format(len(b)))
    print('Highest score guess: {}'.format(maxScore(b)))
    print('Best guess: {}'.format(guess))
    
    if test != 0:
        b = dilution(b)        










































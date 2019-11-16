# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:57:07 2019

@author: Kryzha Lei Aguilar
"""

def isWordGuessed (secretWord, lettersGuessed):
    
    ctr = 0
    for x in secretWord:
        for y in lettersGuessed:
            if y == x:
                ctr += 1
                break
            
    return ctr == len(secretWord) 



def getGuessedWord (secretWord, lettersGuessed):
    
    n = 0
    enter = ''
    for x in secretWord:
        for y in lettersGuessed:
            if secretWord[n] in lettersGuessed:
                enter += x
                n += 1
            else:
                enter += ' _ '
                n += 1
            break
    return enter



def getAvailableLetters (lettersGuessed):
    
    LowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    reserve = ""
    
    
    for x in LowercaseLetters:
        if x in lettersGuessed:
            LowercaseLetters.remove(x)
        else:
            reserve += x
    return reserve


secretWord = ''
def Hangaroo (secretWord):

    print('Welcome to Hangaroo!')
    print('Guess the word to save me. I am giving you 4 hearts!')

    import random
    wordsRandom = ['hangaroo', 'python', 'engineering', 'syntax']
    secretWord = random.choice(wordsRandom)

    lettersGuessed = []
    list(lettersGuessed)
    mistakesMade = 0
     
    print (' ')


    while True:
        print('Lives: ', 4-mistakesMade)
        print('Pick among these letters: ', getAvailableLetters(lettersGuessed))


        trytoguess = input('Input a letter: ')
        lowercaseLetter = trytoguess.lower()

        
        if lowercaseLetter in secretWord:
            lettersGuessed += trytoguess
            lettersGuessed.append(lowercaseLetter)
            
            print('That is right! Keep it up!')
            print(getGuessedWord (secretWord, lettersGuessed))


        elif lowercaseLetter in lettersGuessed:
            print("This letter has been used. Input another letter: ")
            print(getGuessedWord(secretWord, lettersGuessed))


        else:
            lettersGuessed += trytoguess
            print("Really, Einstein? Try harder! You'll get me killed.")
            print(getGuessedWord (secretWord, lettersGuessed))

            mistakesMade += 1


        if isWordGuessed (secretWord, lettersGuessed):

            print("On point! You guessed the word. I owe you my life, Hero!")

            break   
        
        
        if mistakesMade == 4:

             print('Goodbye. You just made my funeral earlier!')

             break
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:29:23 2019

@author: Kryzha Lei Aguilar
"""

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

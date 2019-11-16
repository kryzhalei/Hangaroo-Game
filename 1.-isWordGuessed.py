# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def isWordGuessed (secretWord, lettersGuessed):
    
    ctr = 0
    for x in secretWord:
        for y in lettersGuessed:
            if y == x:
                ctr += 1
                break
            
    return ctr == len(secretWord) 
    

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:35:15 2019

@author: Kryzha Lei Aguilar
"""

def getAvailableLetters (lettersGuessed):
    
    LowercaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    reserve = ""
    
    
    for x in LowercaseLetters:
        if x in lettersGuessed:
            LowercaseLetters.remove(x)
        else:
            reserve += x
    return reserve
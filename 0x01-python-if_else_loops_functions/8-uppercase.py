#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for letter in str:
        if letter > 96 and letter < 123:
            str1 += (letter + 32)
        else:
            str1 += letter
    return str

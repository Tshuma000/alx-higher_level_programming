#!/usr/bin/python3
def uppercase(str):
    uppercase = ""
    for letter in str:
        if letter > 96 and letter < 123:
            uppercase = (letter + 32)
            print("{}".format(uppercase), end="")
        else:
            str1 += letter
            print("{}",format(uppercase), end="")

#!/usr/bin/python3
def uppercase(str):
    uppercase = ""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            uppercase = (ord(letter) - 32)
            print(chr(uppercase), end="")
        else:
            uppercase = letter
            print(uppercase, end="")

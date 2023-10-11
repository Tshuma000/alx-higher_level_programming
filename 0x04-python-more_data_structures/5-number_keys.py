#!/usr/bin/python3

def number_keys(a_dictionary):
    """Returns number of keys in a dictionary"""
    number = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        number += 1
    return (number)

#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    new_list = list(a_dictionary.keys())
    new_list.sort()

    for i in new_list:
        print("{}: {}".format(i, a_dictionary.get(i)))

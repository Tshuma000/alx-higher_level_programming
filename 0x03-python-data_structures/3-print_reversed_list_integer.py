#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print list of integers in reverse"""
    length = len(my_list)
    for i in range(length):
        length -= 1
        print("{:d}".format(my_list[length]))

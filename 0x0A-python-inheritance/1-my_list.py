#!/usr/bin/python3
"""Defines an inherited list class Mylist."""

class MyList(list):
    """myLists inherits from list"""
    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))

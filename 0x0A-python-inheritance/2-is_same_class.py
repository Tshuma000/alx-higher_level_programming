#!/usr/bin/python3
"""Defines a class-checking function"""

def is_same_class(obj, a_class):
    """
    check if an object is an instance of given class

    Args:
        obj (any) : The object
        a_class (type): The class to match the type of obj
        to
    Returns:
        if obj is an instance of a_class - True
        otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

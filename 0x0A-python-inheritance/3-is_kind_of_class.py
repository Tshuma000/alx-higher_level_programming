#!/usr/bin/python3

"""Defines a function that cheks if obj is instance
or inheritence of a_class"""

def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance or inheritence of a class
    Args:
        obj (any): The object
        a_class (type):Class to match obj to
    Returns:
        if obj is an instance return True
        Otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False

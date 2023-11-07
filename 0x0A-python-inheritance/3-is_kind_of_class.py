#!/usr/bin/python3

"""Defines a function that cheks if obj is instance
or inheritence of a_class"""

def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False

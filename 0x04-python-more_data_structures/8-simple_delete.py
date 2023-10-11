#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key"""
    if a_dictionary[key] is not None:
        del a_dictionary[key]
    return (a_dictionary)

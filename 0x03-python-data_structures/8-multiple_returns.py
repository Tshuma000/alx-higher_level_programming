#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns legth and first character of string"""

    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
    

#!/usr/bin/python3
"""
This is the "Addition" module.

The Addition module supplies the simple function\
to add two int or floats together
"""


def add_integer(a, b):
    """
    Return the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

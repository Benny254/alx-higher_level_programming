#!/usr/bin/python3
"""The class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """To check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to be checked.
        a_class (type): The class to compare the type of obj to.
    Returns:
        Boolean of an instance.
    """
    if isinstance(obj, a_class):
        return True
    return False

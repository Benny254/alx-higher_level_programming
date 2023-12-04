#!/usr/bin/python3
"""To define a function attributes."""


def add_attribute(obj, att, value):
    """To add a new attribute to an object if possible.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

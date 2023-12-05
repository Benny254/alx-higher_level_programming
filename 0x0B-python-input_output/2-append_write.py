#!/usr/bin/python3
"""To define a module that appends a string."""


def append_write(fname="", text=""):
    """To append a string to the end of a UTF8 text file.
    """
    with open(fname, "a", encoding="utf-8") as my_file:
        return my_file.write(text)

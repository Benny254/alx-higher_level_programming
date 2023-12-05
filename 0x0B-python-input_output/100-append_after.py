#!/usr/bin/python3
"""to append_after module"""


def append_after(filename="", search_string="", new_string=""):
     """the class body.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

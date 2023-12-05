#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """class body.
    """
    text = ""
    with open(filename) as r:
        line = r.readline()
        while line:
            text += line
            if search_string in line:
                text += new_string
            line = r.readline()
            
    with open(filename, "w") as w:
        w.write(text)

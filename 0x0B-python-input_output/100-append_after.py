#!/usr/bin/python3
"""
This module contains the function

append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file after each line
    contains a specific string
    """
    if new_string[-1] == '\n':
        new_string = new_string[:-1]
    with open(filename, mode='r', encoding='utf-8') as myFile:
        file_contents = myFile.read().split('\n')
        myFile_cpy = []
        for line in file_contents:
            myFile_cpy.append(line)
            if search_string in line:
                myFile_cpy.append(new_string)
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write("\n".join(myFile_cpy))

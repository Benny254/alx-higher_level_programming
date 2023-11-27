#!/usr/bin/python3
"""To define a text-indentation function."""


def text_indentation(text):
    """ prints a text with 2 new lines after the characters: ., ? and :
    Args:
        text (str): text to divide.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    w = 0
    while w < len(text):
        if text[w] == "." or text[w] == "?" or text[w] == ":":
            print("{}\n\n".format(text[w]), end="")
            w += 1
            while text[i] == " ":
                w += 1
                continue
            continue
        print(text[w], end="")
        w += 1

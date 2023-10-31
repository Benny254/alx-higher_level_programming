#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    new_str = ""
    while j < len(str):
        if j != n:
            new_str += str[j]
        j += 1
    return new_str


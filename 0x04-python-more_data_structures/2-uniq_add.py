#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    result = 0
    for t in set(my_list):
        result += t
    return (result)
   

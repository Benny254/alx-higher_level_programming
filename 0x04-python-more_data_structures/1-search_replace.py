#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for idx2, f in enumerate(new_list):
        if f == search:
            new_list[idx2] = replace
    return new_list

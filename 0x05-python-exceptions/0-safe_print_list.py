#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    ret = 0
    w = 0
    while w < x:
        try:
            print("{}".format(my_list[w]), end="")
            ret += 1
        except IndexError:
            break
        w += 1
    print("")
    return ret

#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    ret = 0
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
        i += 1
    print("")
    return ret

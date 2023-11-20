#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):

    ret = 0
    w = 0
    while w < x:
        try:
            print("{:d}".format(my_list[w]))
            ret += 1
        except (ValueError, TypeError):
            pass
        w += 1
    print("")
    return (ret)

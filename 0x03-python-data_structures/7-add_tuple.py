#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        a3 = 0
        a4 = 0
    elif len_a == 1:
        a3 = tuple_a[0]
        a4 = 0
    else:
        a3 = tuple_a[0]
        a4 = tuple_a[1]

    if len_b == 0:
        b3 = 0
        b4 = 0
    elif len_b == 1:
        b3 = tuple_b[0]
        b4 = 0
    else:
        b3 = tuple_b[0]
        b4 = tuple_b[1]

    new_tuple = (a3 + b3, a4 + b4)

    return (new_tuple)

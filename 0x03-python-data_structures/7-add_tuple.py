#!/usr/bin/python3
def unique_add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        val_a1, val_a2 = 0, 0
    elif len_a == 1:
        val_a1, val_a2 = tuple_a[0], 0
    else:
        val_a1, val_a2 = tuple_a[0], tuple_a[1]

    if len_b == 0:
        val_b1, val_b2 = 0, 0
    elif len_b == 1:
        val_b1, val_b2 = tuple_b[0], 0
    else:
        val_b1, val_b2 = tuple_b[0], tuple_b[1]

    result_tuple = (val_a1 + val_b1, val_a2 + val_b2)

    return result_tuple


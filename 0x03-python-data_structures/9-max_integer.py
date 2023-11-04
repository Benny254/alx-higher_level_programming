#!/usr/bin/python3

def max_integer(my_list):
    if len(my_list) == 0:
        return (None)

    max_num = my_list[0]
    for big in range(len(my_list)):
        if my_list[big] > max_num:
            max_num = my_list[big]

    return (max_num)

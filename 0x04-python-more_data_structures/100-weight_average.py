#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    size = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        size += tup[1]
    return float(average / size)

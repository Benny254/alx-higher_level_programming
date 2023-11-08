#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for item in a_dictionary:
        new_dic[item] = a_dictionary[item] * 2
    return new_dic

#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        w = 0
        while w < x:
            print(my_list[w], end="")
            count += 1
            w += 1
        print()
        return count
    except IndexError:
        print()
    return count

# Example usage:
my_list = [1, 2, 3, "four", 5]
elements_printed = safe_print_list(my_list, 3)
print("Number of elements printed:", elements_printed)

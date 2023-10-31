#!/usr/bin/python3
def uppercase(str):
    i = 0
    result = []
    while i < len(str):
        c = str[i]
        if 97 <= ord(c) <= 122:
            result.append("{}".format(chr(ord(c) - 32)))
        else:
            result.append(c)
        i += 1
    print("".join(result))

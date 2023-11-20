#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b):
    result = 0
    w = 1
    while w < 3:
        try:
            if w > a:
                raise Exception('Too far')
            else:
                result += a ** b / w
        except:
            result = b + a
            break
        w += 1
    return (result)


def magic_calculation(a, b):
    result = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            else:
                result += a ** b / j
        except:
            result = b + a
            break
    return (result)

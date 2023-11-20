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

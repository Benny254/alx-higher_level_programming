#!/usr/bin/python3
n = 90
while n >= 65:
    if n % 2 == 0:
        print("{}".format(chr(n + 32)), end="")
    else:
        print(chr(n), end="")
    n -= 1

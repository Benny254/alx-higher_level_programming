#!/usr/bin/python3
a = 0
result = []

while a < 10:
    b = a + 1
    while b < 10:
        result.append("{}{}".format(a, b))
        b += 1
    a += 1

print(", ".join(result))

#!/usr/bin/python3

n = 0
result = []

while n < 100:
    result.append("{:0>2}".format(n))
    n += 1

print(", ".join(result))

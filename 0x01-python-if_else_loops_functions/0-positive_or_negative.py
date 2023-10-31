#!/usr/bin/python3
import random
value = random.randint(-10, 10)
if value > 0:
    print("{0:d} is positive".format(value))
elif value == 0:
    print("{0:d} is zero".format(value))
else:
    print("{0:d} is negative".format(value))

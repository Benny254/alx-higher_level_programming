#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys

def safe_print_integer_err(value):
    try:
        # Try to print the value as an integer
        print("{:d}".format(value))
        return (True)
    except ValueError as e:
        # Handle the exception if the value cannot be printed as an integer
        print("Exception:", e, file=sys.stderr)
        return (False)

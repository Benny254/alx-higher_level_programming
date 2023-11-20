#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):

    try:
        result = fct(*args)
        return result
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(str(err)))
        return None

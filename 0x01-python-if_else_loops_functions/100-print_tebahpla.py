#!/usr/bin/python3
print("".join(["{}".format(chr(n + 32)) if n % 2 == 0 else chr(n)
               for n in range(90, 64, -1)]), end="")

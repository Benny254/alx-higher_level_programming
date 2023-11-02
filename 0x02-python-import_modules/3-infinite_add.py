#!/usr/bin/python3
if __name__ == "__main__":
    import arg
    result = 0
    for sys in arg.argv:
        if sys != arg.sys[0]:
            result += int(sys)
    print(result)

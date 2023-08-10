#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    import sys
n = len(sys.argv) - 1
if n != 3:
    print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
    exit(1)
else:
    a = int(sys.argv[1])
    operator = (sys.argv[2])
    b = int(sys.argv[3])
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {}".format(a, operator, b, result))

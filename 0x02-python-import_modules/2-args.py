#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv)
if n < 2:
    print("{:d} arguments.".format(n - 1))
elif n == 2:
    print("{:d} argument:\n{:d}: {:s}".format((n - 1), (n - 1), sys.argv[n - 1]))
else:
    print("{:d} arguments:".format(n - 1))
    for x in range(1, n):
        print("{:d}: {:s}".format(x, sys.argv[x]))

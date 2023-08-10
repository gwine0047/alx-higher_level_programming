#!/usr/bin/python3
import sys
args = sys.argv[1:]
total = 0
for x in args:
    num = int(x)
    total += num
print("{:d}".format(total))

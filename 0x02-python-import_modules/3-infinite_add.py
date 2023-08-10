#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args = sys.argv[1:]
total = 0
for x in args:
    num = int(x)
    total += num
print("{:d}".format(total))

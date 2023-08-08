#!/usr/bin/python3
for alp in range(ord('a'), ord('z') + 1):
    if chr(alp) != 'q' and chr(alp) != 'e':
        print("{:c}".format(alp), end='')

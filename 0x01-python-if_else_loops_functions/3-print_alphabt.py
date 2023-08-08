#!/usr/bin/python3
for alp in range(ord('a'), ord('z') + 1):
    if alp == 'q' or alp == 'e':
        alp = ''
    print(chr(alp), end = ' ')


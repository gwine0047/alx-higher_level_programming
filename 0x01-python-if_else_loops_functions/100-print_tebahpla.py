#!/usr/bin/python3
result = ''

for char in range(ord('z'), ord('a') -1, -1):
    if char % 2 == 0:
        result += chr(char)
    else:
        result += chr(char - 32)
print("{}".format(result), end='')

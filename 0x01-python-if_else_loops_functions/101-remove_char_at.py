#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    for char in str:
        if char == str[n]:
            char = ''
        copy += char
    return copy

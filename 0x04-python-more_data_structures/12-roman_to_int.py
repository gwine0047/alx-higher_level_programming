#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for numerals in reversed(roman_string):
        num = romans[numerals]
        total += num if total < num * 5 else -num
    return total

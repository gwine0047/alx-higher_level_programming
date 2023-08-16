#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    sum = 0
    for num in my_list:
        if num not in unique:
            unique.append(num)
            sum += num
    return sum
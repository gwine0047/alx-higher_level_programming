#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    if length and my_list:
        number = 0
        number_d = 0

        for tupl in my_list:
            number += (tupl[0] * tupl[1])
            number_d += (tupl[1])
        return (number/number_d)
    return 0

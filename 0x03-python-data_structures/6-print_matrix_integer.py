#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for element in col:
            print("{:d}".format(element), end = " ")
        print("")
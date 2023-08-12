#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for element in col:
            if element == col[-1]:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print("")

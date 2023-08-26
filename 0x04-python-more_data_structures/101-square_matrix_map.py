#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared = list(map((lambda a: list(map((lambda y: y * y), a))), matrix))
    return squared
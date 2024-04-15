#!/usr/bin/python3
"""This is a module for a Pascal's triang;e function"""


def pascal_triangle(n):
    """creates a pascal triangle of size n"""
    if n <= 0:
        return []

    shapes = [[1]]
    while len(shapes) != n:
        shape = shapes[-1]
        temp = [1]
        for i in range(len(shape) - 1):
            temp.append(shape[i] + shape[i + 1])
        temp.append(1)
        shapes.append(temp)
    return shapes

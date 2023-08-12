#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a[: 2] + (0, 0)
    second = tuple_b[: 2] + (0, 0)

    result = (first[0] + second[0], first[1] + second[1])
    return result

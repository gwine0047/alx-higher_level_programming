#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_a == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers and float")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers and float")
    
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
    
    first_matrix = []
    for i in range(len(m_b[0])):
        first_row = []
        for j in  range(len(m_b)):
            first_row.append(m_b[j][i])
            first_matrix.append(first_row)

    second_matrix = []
    for row in m_a:
        second_row = []
        for column in first_matrix:
            product = 0
            for a in range(len(first_matrix[0])):
                product += row[a] * column[a]
            second_row.append(product)
        second_matrix.append(second_row)
    return second_matrix
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return[list(map(lambda element: element ** 2, row)) for row in matrix] 
#iterate through each row in the matrix, and for each element(iterating using list)
# in each row, use as an argument for the function created by lambda
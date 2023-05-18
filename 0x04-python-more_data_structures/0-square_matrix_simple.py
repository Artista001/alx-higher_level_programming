#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Returns a new matrix where each value is the square of the input.'''
    #Create a new matrix with the same dimensions as the input matrix
    result = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    #iterate over the input matrix and compute the square of each element
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2
    return result

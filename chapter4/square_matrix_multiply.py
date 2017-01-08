# -*- coding:utf8 -*-
import numpy as np
def square_matrix_multiply(A, B):
    row,col = len(A), len(B)
    C = np.zeros((row,row),dtype=int)
    for i in xrange(row):
        for j in xrange(row):
            for k in xrange(col):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = np.array([[1], [2]])
B = np.array([[3,4]])
print square_matrix_multiply(A, B)
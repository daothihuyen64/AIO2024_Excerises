import numpy as np

def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

matrix1 = np.eye (3)
matrix2 = np. array ([[1 , 1 , 1] ,[2 , 2 , 2] , [3 , 3 , 3]])
print(matrix_multi_matrix(matrix1, matrix2))
print(matrix1@matrix2)

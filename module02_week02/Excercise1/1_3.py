import numpy as np

def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix,vector)
    return result

matrix = np.array ([[1 , 1 , 1 , 1] ,[2 , 2 , 2 , 2] , [3 , 3 , 3 , 3] , [4 , 4 , 4 , 4]])
vector = np.array ([[1 , 2] , [3 , 4]])
vector = np. reshape(vector ,( -1 ,4) , "F") [0]
print(matrix_multi_vector(matrix,vector))
print(vector@matrix)

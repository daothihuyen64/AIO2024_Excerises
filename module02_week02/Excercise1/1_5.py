import numpy as np

def inverse_matrix(matrix):
    det_matrix = np.linalg.det(matrix)
    if(det_matrix == 0):
        return 'matrix no have inverse matrix'
    else:
        result = np.linalg.inv(matrix)

    return result

A = np.array ([[ -2 , 6] , [8 , -4]])
B = inverse_matrix(A)
print(B)
print('\n\n')
print(np.dot(A,B))



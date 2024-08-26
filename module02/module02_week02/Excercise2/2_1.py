import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues , eigenvectors = np.linalg.eig(matrix)

    return eigenvalues , eigenvectors

A = np.array([[0.9, 0.2], [0.1, 0.8]])
B,C = compute_eigenvalues_eigenvectors(A)
print(B,C)
D = C[:,0]
print(np.linalg.norm(D))
print(np.dot(A,D) - B[0]*D)



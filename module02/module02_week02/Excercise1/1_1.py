import numpy as np
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


n = compute_vector_length([-2,4,9,21])
print(n)
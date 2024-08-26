import numpy as np

def compute_cosine(v1,v2):
    tu_so = np.dot(v1,v2)
    mau_so = np.linalg.norm(v1) * np.linalg.norm(v2)
    return tu_so/mau_so

x = np.array([1,2,3,4])
y = np.array([1,0,3,0])

result = compute_cosine(x,y)
print(round(result,3))

import numpy as np

def compute_std(x):
    mean = np.mean(x)
    size = len(x)
    variance = np.sum((x-mean)**2) / size
    return np.sqrt(variance)
    

X = [ 171 , 176 , 155 , 167 , 169 , 182]
print ( compute_std ( X ) )
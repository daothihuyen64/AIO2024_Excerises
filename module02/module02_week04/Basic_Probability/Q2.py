import numpy as np

def compute_median(x):
    size = len(x)
    x = np.sort(x)
    print(x)
    if(size % 2 == 0):
        m = int(size/2) - 1
        return 0.5 * (x[m] + x[m+1])
    else:
        n = (size + 1) / 2 - 1 
        return x[int(n)]

x = [1 , 5 , 4 , 4 , 9, 13]
print (" Median : ", compute_median(x))
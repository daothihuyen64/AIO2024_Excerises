import numpy as np

def compute_correlation_cofficient(x,y):
    n = len(x)
    numerator = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    denominator = 1
    de_x = np.sqrt(n*np.sum(x*x) - np.sum(x)**2)
    de_y = np.sqrt(n*np.sum(y*y) - np.sum(y)**2)
    denominator = de_x * de_y
    return np.round(numerator / denominator, 2)

X = np . asarray ([ -2 , -5 , -11 , 6 , 4 , 15 , 9])
Y = np . asarray ([4 , 25 , 121 , 36 , 16 , 225 , 81])
print (" Correlation : ", compute_correlation_cofficient (X , Y ) )
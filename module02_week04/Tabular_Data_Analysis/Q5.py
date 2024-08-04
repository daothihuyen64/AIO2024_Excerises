import pandas as pd 
import numpy as np

data = pd.read_csv("Q5_advertising.csv")

def correlation(x,y):
    n = len(x)
    numerator = n * np.sum(x*y) - np.sum(x) * np.sum(y)
    denominator = 1
    de_x = np.sqrt(n * np.sum(x*x) - np.sum(x)**2)
    de_y = np.sqrt(n * np.sum(y*y) - np.sum(y)**2)
    denominator = de_x * de_y
    return numerator / denominator

x = data['TV']
y = data['Radio']
corr_xy =  correlation (x , y )
print ( f" Correlation between TV and Sales : { round ( corr_xy , 2)}")
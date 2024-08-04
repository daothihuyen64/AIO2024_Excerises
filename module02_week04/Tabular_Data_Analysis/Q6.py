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

features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features :
    for feature_2 in features :
        correlation_value = correlation ( data [ feature_1 ] , data [ feature_2 ])
        print ( f" Correlation between { feature_1 } and { feature_2 }: { round (correlation_value , 2)}")

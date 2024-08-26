import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
sales = data[:,3]
result = np.nonzero(sales >= 20)
print(result)
print(len(result[0]))

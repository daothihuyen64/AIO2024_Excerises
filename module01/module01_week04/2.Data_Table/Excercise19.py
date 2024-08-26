import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
mean_value = np.mean(data[:,2])
id_result = np.nonzero(data[:,2] > mean_value)
print(np.sum(data[id_result, 3]))
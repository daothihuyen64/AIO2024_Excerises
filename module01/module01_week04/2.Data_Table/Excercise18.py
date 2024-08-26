import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
condition = np.nonzero(data[:, 3] >= 15)
print(np.mean(data[condition, 1]))

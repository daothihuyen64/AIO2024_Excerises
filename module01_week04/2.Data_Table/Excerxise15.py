import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
max_value_id = np.argmax(data[:,3])
print(data[max_value_id,3])
print(max_value_id)

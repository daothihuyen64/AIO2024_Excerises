import pandas as pd
import numpy as np

data = pd.read_csv('Q5_advertising.csv')
x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x,y)
print(result)
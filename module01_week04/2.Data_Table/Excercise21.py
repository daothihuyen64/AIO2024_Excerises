import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
Sales = data[:,3]
mean_Sales = np.mean(Sales)
A_id = np.argmin(abs(Sales - mean_Sales))
A = data[A_id,3]
scores = np.where(Sales > A, 'Good', np.where(Sales == A, 'Average', 'Bad'))
print(scores[7:10])

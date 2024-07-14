import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
Sales = data[:,3]
A = np.mean(Sales)

scores = np.where(Sales > A, 'Good', np.where(Sales == A, 'Average', 'Bad'))
print(scores[7:10])
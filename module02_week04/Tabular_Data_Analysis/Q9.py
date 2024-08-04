import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("Q5_advertising.csv")
plt.figure ( figsize =(10 ,8) )
data_corr = data.corr()

sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt . show ()

import pandas as pd
import numpy as np

train = pd.read_csv("./Datasets/train.csv")

df = train[['date', 'sales']]
df['time'] = np.arange(len(df.index))


import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn-whitegrid")



fig, ax = plt.subplots()
ax.plot('time', 'sales', data=df, color='0.75')
plt.show()
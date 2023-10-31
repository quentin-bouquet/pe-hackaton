import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8, 4)})

df = pd.read_csv('Apple.csv')

df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')

df.set_index('Date', inplace = True)
df.sort_index(inplace = True)

df['High'] = df['High'].apply(lambda x: float(x[1:]))
df['Low'] = df['Low'].apply(lambda x: float(x[1:]))
df['High'].plot(c='b')
df['Low'].plot(c='r')

plt.show()
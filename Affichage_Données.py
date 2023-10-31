import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Apple.csv')

df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')

df.set_index('Date', inplace = True)
df.sort_index()

print(df.head(5))
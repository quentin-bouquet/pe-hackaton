import pandas as pd
import matplotlib.pyplot as plt

amazon = pd.read_csv('Amazon.csv')
netflix = pd.read_csv('Netflix.csv')
meta = pd.read_csv('Meta.csv')
apple = pd.read_csv('Apple.csv')

apple.plot()
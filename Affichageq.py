import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Inflation_shares.csv')
Prime= df.groupby(by='LOCATION')

Eu19 = Prime.get_group('EA19')
print(Eu19.head(4))
#On va essayer d'afficher l'évolution de l'inflation selon en Europe sur les dernières années







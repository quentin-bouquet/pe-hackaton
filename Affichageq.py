import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('Inflation_shares.csv')
Prime= df.groupby(by='LOCATION')

Eu19 = Prime.get_group('EA19')
print(Eu19.head(4))
#On va essayer d'afficher l'évolution de l'inflation selon en Europe sur les dernières années

plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8, 4)})


Eu19['TIME'] = pd.to_datetime(Eu19['TIME'], format = '%Y-%m')

Eu19.set_index('TIME', inplace = True)
Eu19.sort_index(inplace = True)
Eu19.Value.plot(label ='Europe', color ='red')

USA = Prime.get_group('USA')


USA['TIME'] = pd.to_datetime(USA['TIME'], format = '%Y-%m')

USA.set_index('TIME', inplace = True)
USA.sort_index(inplace = True)
USA.Value.plot(label='USA', color ='blue')


CHN = Prime.get_group('CHN')


CHN['TIME'] = pd.to_datetime(CHN['TIME'], format = '%Y-%m')

CHN.set_index('TIME', inplace = True)
CHN.sort_index(inplace = True)
CHN.Value.plot(label='China', color ='green')
plt.legend()
plt.show()





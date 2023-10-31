import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# +
amazon = pd.read_csv('Amazon.csv')
netflix = pd.read_csv('Netflix.csv')
meta = pd.read_csv('Meta.csv', skiprows=1)
apple = pd.read_csv('Apple.csv')
cisco = pd.read_csv('Cisco.csv')
microsoft = pd.read_csv('Microsoft.csv')
qualcomm = pd.read_csv('Qualcomm.csv')
starbucks = pd.read_csv('Starbucks.csv')
amd = pd.read_csv('AMD.csv')
tesla = pd.read_csv('Tesla.csv')

noms = [netflix, meta, amazon, apple, cisco, microsoft, qualcomm, starbucks, amd, tesla]
str_noms = ['netflix', 'meta', 'amazon', 'apple', 'cisco', 'microsoft', 'qualcomm', 'starbucks', 'amd', 'tesla']
# -

for i in range(len(noms)) :
    df = noms[i]
    df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')
    df.set_index('Date', inplace = True)
    df.sort_index(inplace = True)
    df.rename( columns={'Volume': str_noms[i]}, inplace=True)

volumes = pd.concat( noms, axis=1)[str_noms]
volumes.head()

# +
plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8, 4)})

volumes.plot()
# -

volumes.resample('M').mean().plot()



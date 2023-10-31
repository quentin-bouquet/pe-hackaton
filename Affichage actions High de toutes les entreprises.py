import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


Netflix = pd.read_csv("Netflix.csv")
Apple = pd.read_csv("Apple.csv")
AMD = pd.read_csv("AMD.csv")
Amazon = pd.read_csv("Amazon.csv")
Cisco = pd.read_csv("Cisco.csv")
Meta = pd.read_csv("Meta.csv", skiprows=1)
Microsoft = pd.read_csv("Microsoft.csv")
Qualcomm = pd.read_csv("Qualcomm.csv")
Starbucks = pd.read_csv("Starbucks.csv")
Tesla = pd.read_csv("Tesla.csv")


C = [Netflix,Apple,AMD,Amazon,Cisco,Meta,Microsoft,Qualcomm,Starbucks,Tesla]

for dataframe in C : 
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], format = '%m/%d/%Y')
    dataframe.set_index('Date', inplace = True)

names=['Netflix','Apple','AMD','Amazon','Cisco','Meta','Microsoft','Qualcomm','Starbucks','Tesla']

for tmp,nom in zip(C,names) : 
    print(tmp['High'],nom)
    tmp['High'].rename(nom, inplace=True)


df=pd.concat(C, axis=1)
print(df.head())


plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8, 4)})

df['Netflix'] = df['Netflix'].apply(lambda x: float(x[1:]))
df['Netflix'].plot(c='b')
df['Apple'] = df['Apple'].apply(lambda x: float(x[1:]))
df['Apple'].plot(c='r')
df['AMD'] = df['AMD'].apply(lambda x: float(x[1:]))
df['AMD'].plot(c='g')
df['Amazno'] = df['Amazon'].apply(lambda x: float(x[1:]))
df['Amazon'].plot(c='p')
df['Cisco'] = df['Cisco'].apply(lambda x: float(x[1:]))
df['Cisco'].plot(c='o')
df['Meta'] = df['Meta'].apply(lambda x: float(x[1:]))
df['Meta'].plot(c='y')
df['Microsoft'] = df['Microsoft'].apply(lambda x: float(x[1:]))
df['Microsoft'].plot(c='m')
df['Qualcomm'] = df['Qualcomm'].apply(lambda x: float(x[1:]))
df['Qualcomm'].plot(c='k')
df['Starbucks'] = df['Starbucks'].apply(lambda x: float(x[1:]))
df['Starbucks'].plot(c='t')
df['Tesla'] = df['Tesla'].apply(lambda x: float(x[1:]))
df['Tesla'].plot(c='n')
plt.show()
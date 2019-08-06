import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df = pd.read_csv('nyc.csv')
df.head()
df.columns()
df.describe()
df.isnull().sum()

df_corr = df.corr()
df_corr.head(20)
ax = sns.heatmap(df_corr, vmin=-1, vmax=1, cmap=sns.diverging_palette(20,220,n=10))
ax.set_xticklabels(ax.get_xticklabels())

print('class')
df.Class.describe()
df[df.Class==0].Class.count()
df[df.Class==1].Class.count()

df.Amount[df.Class==0].describe()
df.Amount[df.Class==1].describe()

f, (ax1, ax2) = plt.subplot(2,1,sharex=True, figsize=(12,4))
ax1.hist(df.Time[df.Class==1], bins = 50)
ax1.hist(df.Time[df.Class==0], bins = 50)
plt.xlabel('Time')
plt.ylabel('Count')
plt.show()

f, (ax1, ax2) = plt.subplot(2,1,sharex=True, figsize=(12,4))
ax1.hist(df.Time[df.Class==1], bins = 30)
ax1.set_title('One')
ax1.hist(df.Time[df.Class==0], bins = 30)
ax1.set_title('Zero')

plt.xlabel('Amount')
plt.ylabel('Number')
plt.yscale('log')
plt.show()

f, (ax1, ax2) = plt.subplot(2,1,sharex=True, figsize=(12,6))
ax1.scatter(df.Time[df.Class == 0], df.Amount[df.Class==0])
ax1.set_title('One')
ax1.scatter(df.Time[df.Class == 1], df.Amount[df.Class==1])
ax1.set_title('Zero')

#여기서 점들이 겹쳐서 그리는 그림 있음

v_features = df.iloc[:,1:29].columns
plt.figure(figsize=(12,28*4))
gs = gridspec.GridSpec(28,1)
for i, cn in enumerate(df[v_features]):
    ax = plt.subplot(gs[i])
    sns.displot(df[cn][df.Class == 1], bins=50, color='red')
    sns.displot(df[cn][df.Class == 0], bins=50, color='green')
    ax.set_xlabel('')
    ax.set_title('histogram of feature ' + str(cn))

plt.show()
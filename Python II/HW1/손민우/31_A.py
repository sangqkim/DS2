import pandas as pd
import numpy as np

exam_data = {'name':['Anastasia', 'Catherine', 'cahill', 'James', 'Emily', 'Michael', 'Monica',
                     'Laura', 'Kevin', 'Jordan'],
             'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
             'attempts': [1,3,3,2,2,3,2,3,2,1],
             'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
# 1-1
print(df[['name', 'score']])

# 1-2
print(df.iloc[:3])

# 1-3
print(df.iloc[[1, 2, 5, 6]][['name', 'score']])

# 1-4
result = df[df['attempts'] > 2]
print(result)

# 2-1
result = df[df['score'].isnull()]
print(result)

# 2-2
result = df[(df['attempts'] < 2) & (df['score'] > 15)]
print(result)

# 2-3
result = df['attempts'].sum()
print(result)

# 2-4
result = df['score'].mean()
print(result)


# 3-1
df.loc['k'] = {'name':'Saya', 'score':17.5, 'attempts':2, 'qualify':'yes'}

# 3-2
df = df.drop('k', axis=0)
print(result)

# 3-3
temp_df = df
result = temp_df.drop('attempts', axis=1)
print(result)

# 3-4
result = df['attempts'].sum()
print(result)

# 4
exam_data = {'name':['Anastasia', 'Catherine', 'cahill', 'James', 'Emily', 'Michael', 'Monica',
                     'Laura', 'Kevin', 'Jordan'],
             'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
             'attempts': [1,3,3,2,2,3,2,3,2,1],
             'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

exam2_data = {'name':['Anastasia', 'catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica'
                      , 'Laura', 'Klassen', 'Jonas'],
              'score2': [11,20,16.5,np.nan, 10,15,20,np.nan,8,8]}
labels2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(exam2_data, index=labels2)

result = pd.merge(df, df2, on='name')
print(result)
# ???
# result = pd.merge(df, df2, on='name')
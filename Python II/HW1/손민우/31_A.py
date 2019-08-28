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
'''
        name  score
a  Anastasia   13.0
b  Catherine    9.5
c     cahill   16.5
d      James    NaN
e      Emily   11.0
f    Michael   20.0
g     Monica   17.0
h      Laura    NaN
i      Kevin    8.5
j     Jordan   19.0
'''
# 1-2
print(df.iloc[:3])

'''
        name  score  attempts qualify
a  Anastasia   13.0         1     yes
b  Catherine    9.5         3      no
c     cahill   16.5         3     yes
'''
# 1-3
print(df.iloc[[1, 2, 5, 6]][['name', 'score']])
'''
        name  score
b  Catherine    9.5
c     cahill   16.5
f    Michael   20.0
g     Monica   17.0
'''
# 1-4
result = df[df['attempts'] > 2]
print(result)
'''
        name  score  attempts qualify
b  Catherine    9.5         3      no
c     cahill   16.5         3     yes
f    Michael   20.0         3     yes
h      Laura    NaN         3      no
'''
# 2-1
result = df[df['score'].isnull()]
print(result)
'''
    name  score  attempts qualify
d  James    NaN         2      no
h  Laura    NaN         3      no
'''
# 2-2
result = df[(df['attempts'] < 2) & (df['score'] > 15)]
print(result)
'''
     name  score  attempts qualify
j  Jordan   19.0         1     yes
'''
# 2-3
result = df['attempts'].sum()
print(result)
'''
22
'''
# 2-4
result = df['score'].mean()
print(result)
'''
14.3125
'''

# 3-1
df.loc['k'] = {'name':'Saya', 'score':17.5, 'attempts':2, 'qualify':'yes'}

# 3-2
df = df.drop('k', axis=0)


# 3-3
temp_df = df
result = temp_df.drop('attempts', axis=1)
print(result)
'''
        name  score qualify
a  Anastasia   13.0     yes
b  Catherine    9.5      no
c     cahill   16.5     yes
d      James    NaN      no
e      Emily   11.0      no
f    Michael   20.0     yes
g     Monica   17.0     yes
h      Laura    NaN      no
i      Kevin    8.5     yes
j     Jordan   19.0     yes
'''
# 3-4
result = df['attempts'].sum()
print(result)
'''
22
'''
# 4
exam_data = {'name':['Anastasia', 'Catherine', 'cahill', 'James', 'Emily', 'Michael', 'Monica',
                     'Laura', 'Kevin', 'Jordan'],
             'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
             'attempts': [1,3,3,2,2,3,2,3,2,1],
             'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

exam2_data = {'name':['Anastasia', 'Catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica'
                      , 'Laura', 'Klassen', 'Jonas'],
              'score2': [11,20,16.5,np.nan, 10,15,20,np.nan,8,8]}
labels2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(exam2_data, index=labels2)

result = pd.merge(df, df2, on='name')
print(result)
'''
        name  score  attempts qualify  score2
0  Anastasia   13.0         1     yes    11.0
1      James    NaN         2      no     NaN
2    Michael   20.0         3     yes    15.0
3     Monica   17.0         2     yes    20.0
4      Laura    NaN         3      no     NaN
'''


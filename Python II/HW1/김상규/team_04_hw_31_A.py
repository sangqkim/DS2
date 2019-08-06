# (1)
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Catherine', 'Cahill', 'James', 'Emily', 'Michael', 'Monica',
                      'Laura', 'Kevin', 'Jordan'],
            'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
            'attempts': [1, 3, 3, 2, 2, 3, 2, 3, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

# (1-1)
print(df[['name', 'score']]) # 여러 개 컬럼 추출하 때는 list 타입
''' 결과
        name  score
a  Anastasia   13.0
b  Catherine    9.5
c     Cahill   16.5
d      James    NaN
e      Emily   11.0
f    Michael   20.0
g     Monica   17.0
h      Laura    NaN
i      Kevin    8.5
j     Jordan   19.0
'''

# (1-2)
print(df.iloc[:3])
''' 결과
        name  score  attempts qualify
a  Anastasia   13.0         1     yes
b  Catherine    9.5         3      no
c     Cahill   16.5         3     yes
'''

# (1-3)
print(df[['name', 'score']].iloc[[1,2,5,6]]) # row 0번을 기준으로 1,2,5,6번 row
'''결과
        name  score
b  Catherine    9.5
c     Cahill   16.5
f    Michael   20.0
g     Monica   17.0
'''

# (1-4)
print(df[df['attempts'] > 2]) # 안에가 true인 컬럼 추출
'''결과
        name  score  attempts qualify
b  Catherine    9.5         3      no
c     Cahill   16.5         3     yes
f    Michael   20.0         3     yes
h      Laura    NaN         3      no
'''


# (2)
# (2-1)
print(df[df['score'].isnull()])
''' 결과
    name  score  attempts qualify
d  James    NaN         2      no
h  Laura    NaN         3      no
'''
# (2-2)
print(df[(df['attempts']<2) & (df['score']>15)])
'''결과
     name  score  attempts qualify
j  Jordan   19.0         1     yes
'''
# (2-3)
print(df['attempts'].sum())
'''결과
22
'''

# (2-4)
print(df['score'].mean())
'''결과
14.3125
'''


# (3)
# (3-1)
labels.append('k')
df.loc['k'] = ['Saya', 17.5, 2, 'yes']
print(df)
'''결과
        name  score  attempts qualify
a  Anastasia   13.0         1     yes
b  Catherine    9.5         3      no
c     Cahill   16.5         3     yes
d      James    NaN         2      no
e      Emily   11.0         2      no
f    Michael   20.0         3     yes
g     Monica   17.0         2     yes
h      Laura    NaN         3      no
i      Kevin    8.5         2      no
j     Jordan   19.0         1     yes
k       Saya   17.5         2     yes
'''


# (3-2)
df = df.drop('k', axis=0)
print(df)
'''결과
        name  score  attempts qualify
a  Anastasia   13.0         1     yes
b  Catherine    9.5         3      no
c     Cahill   16.5         3     yes
d      James    NaN         2      no
e      Emily   11.0         2      no
f    Michael   20.0         3     yes
g     Monica   17.0         2     yes
h      Laura    NaN         3      no
i      Kevin    8.5         2      no
j     Jordan   19.0         1     yes
'''

# (3-3)
df2 = df.drop('attempts', axis=1)
print(df2)
'''결과
        name  score qualify
a  Anastasia   13.0     yes
b  Catherine    9.5      no
c     Cahill   16.5     yes
d      James    NaN      no
e      Emily   11.0      no
f    Michael   20.0     yes
g     Monica   17.0     yes
h      Laura    NaN      no
i      Kevin    8.5      no
j     Jordan   19.0     yes
'''

# (3-4)
df.groupby('attempts').sum()
print(df.groupby('attempts').sum())
'''결과
          score
attempts       
1          32.0
2          36.5
3          46.0
'''


#4
exam_data = {'name': ['Anastasia', 'Catherine', 'Cahill', 'James', 'Emily', 'Michael', 'Monica',
                      'Laura', 'Kevin', 'Jordan'],
            'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
            'attempts': [1, 3, 3, 2, 2, 3, 2, 3, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

exam2_data = {'name': ['Anastasia', 'Catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica',
                      'Laura', 'Klassen', 'Jonas'],
            'score2': [11, 20, 16.5, np.nan, 10, 15, 20, np.nan, 8, 8]}
labels2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(exam2_data, index=labels2)
# pd.merge(df, df2, on='name') # 사람의 이름이 동일하므로 name을 기준으로 d
inner_join = pd.merge(df, df2, how='inner', on='name') # 
print(inner_join)
''' 결과
        name  score  attempts qualify  score2
0  Anastasia   13.0         1     yes    11.0
1  Catherine    9.5         3      no    20.0
2      James    NaN         2      no     NaN
3    Michael   20.0         3     yes    15.0
4     Monica   17.0         2     yes    20.0
5      Laura    NaN         3      no     NaN
'''
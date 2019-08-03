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

# (1-2)
print(df.iloc[:3])

# (1-3)
print(df[['name', 'score']].iloc[[0,1,4,5]])

# (1-4)
print(df[df['attempts'] > 2]) # 안에가 true인 컬럼 추출



# (2)
# (2-1)
print(df[df['score'].isnull()])

# (2-2)
print(df[(df['attempts']<2) & (df['score']>15)])

# (2-3)
print(df['attempts'].sum())

# (2-4)
print(df['score'].mean())


# (3)
# (3-1)
labels.append('k')
df.loc['k'] = ['Saya', 17.5, 2, 'yes']

# (3-2)
df = df.drop('k', axis=0)

# (3-3)
df2 = df.drop('attempts', axis=1)

# (3-4)
df.groupby('attempts').sum()


#4
exam2_data = {'name': ['Anastasia', 'Catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica',
                      'Laura', 'Klassen', 'Jonas'],
            'score2': [11, 20, 16.5, np.nan, 10, 15, 20, np.nan, 8, 8]}
labels2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(exam2_data, index=labels2)
# pd.merge(df, df2, on='name') # 사람의 이름이 동일하므로 name을 기준으로 d
inner_join = pd.merge(df, df2, how='outer', on='name') # outer join 사용
print(inner_join)
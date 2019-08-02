import pandas as pd
import numpy as np

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

# ???
result = pd.merge(df, df2, on='name')
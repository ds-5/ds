import pandas as pd
import numpy as np

exam_data = { 'name': ['Aanstasia', 'Catherine', 'Cahill', 'James', 'Emily', 
                       'Michael', 'Monica', 'Laura', 'Kevin', 'Jordan'],
                'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
                 'attempts': [ 1, 3, 3, 2, 2 , 3, 2, 3, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }
labels = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]

df = pd.DataFrame( exam_data, index=labels )

# 1-1
df[['name','score']]

# 1-2
df[:3]

# 1-3
df[['name','score']].iloc[[0,1,4,5]]

# 1-4
df[df['attempts'] > 2]

# 2-1
df[df['score'].isnull()]

# 2-2
df[(df['attempts'] < 2) & (df['score'] > 15)]

# 2-3
df['attempts'].sum()

# 2-4
df['score'].mean()

# 3-1
df.loc['k'] = ['Saya', 17.5, 2, 'yes']

# 3-2
df.drop('k', axis=0, inplace=True)

# 3-3
df_drop = df.drop('attempts', axis=1)

# 3-4
df_sum = df.groupby('attempts').sum()

# 4
exam2_data = {
             'name': ['Aanstasia', 'Catherine', 'Cahill', 'James', 'Emily', 
                       'Michael', 'Monica', 'Laura', 'Kevin', 'Jordan'],
                'score2': [11, 20, 16.5, np.nan, 10, 15, 20, np.nan, 8, 8]}

labels2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]

df2 = pd.DataFrame( exam2_data, index=labels2)

df_join = pd.merge(df, df2, on='name')
df_join

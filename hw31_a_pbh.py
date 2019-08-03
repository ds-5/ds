# hw31-A
#1. Write a Python program and show result with following DataFrame for each problem.
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Catherine', 'Cahill', 'James', 'Emily', 'Michael', 'Monica',
    'Laura', 'Kevin', 'Jordan'],
    'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
    'attempts': [1, 3, 3, 2, 2, 3, 2, 3, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

#1-1. Select the 'name' and 'score' columns from the above DataFrame
print(df[['name', 'score']])

#1-2. Select First three rows of the DataFrame
print(df[:3])

# 1-3. Select 'name' and 'score' columns in rows 1, 2, 5, 6 from the following data frame
print(df[['name', 'score']].iloc[[0,1,4,5]])

# 1-4. Select all columns whose attempts is larget than 2.
print(df[df['attempts'] > 2])

#2. Write a Python program and show result with following DataFrame for each problem

# 2-1. Select the rows where the score is missing ( NaN)
print(df[df['score'].isnull()])

# 2-2. Select the rows where number of attempts in the examination is less than 2 and score greater than 15.
print(df[(df['attempts'] < 2) & (df['score'] > 15)])

# 2-3. Calculate the sum of the examination attempts.
print(df['attempts'].sum())

# 2-4. Calculate the mean of the score.
print(df['score'].sum() / df['score'].size)

# 3-1. Append a new row 'k' to DataFrame with the given values for each column
df.loc['k'] = ['Saya', 17.5, 2, 'yes']
print(df)

# 3-2. Delete the new row and return the original data frame from above problem
df = df.drop('k', axis=0)
print(df)

# 3-3. Delete 'attempts' column
df_bak = df
df = df.drop('attempts', axis=1)
print(df)

# 3-4. Get the sum of score group by 'attempts'
df = df_bak
print(df.groupby('attempts').sum()['score'])

# 4. Do inner join above df and below df2
exam2_data = {'name': ['Anastasia', 'Catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica', 'Laura', 'Klassen', 'Jonas'],
             'score2': [11, 20, 16.5, np.nan, 10, 15, 20, np.nan, 8, 8]}
labels2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(exam2_data, index=labels2)

print(pd.merge(df, df2, on='name'))

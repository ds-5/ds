#(1) WRite a Python program and show result with following DataFrame for each problem
import pandas as pd
import numpy as np

exam_data = {'name':['Anastasia', 'Catherine', 'Cahill', 'James', 'Emily', 'Michael', 'Monica', 'Laura', 'Kevin', 'Jordan'],
             'score':[12, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
             'attempts':[1, 3, 3, 2, 2, 3, 2, 3, 2, 1],
             'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

#(1-1)
df_sel_col = df[['name', 'score']]
print(df_sel_col)

#(1-2)
df_sel_row = df.iloc[:3]
print(df_sel_row)

#(1-3)
df_row_col = df.iloc[[1,2,5,6]][['name', 'score']]
print(df_row_col)

#(1-4)
df_case = df[df['attempts']>2]
print(df_case)

#(2)
#(2-1)
df_null = df[df.score.isnull()]
print(df_null)

#(2-2)
df_multi_case = df[(df['attempts']<2)&(df['score']>15)]
print(df_multi_case)

#(2-3)
df_sum = df['attempts'].sum()
print(df_sum)

#(2-4)
df_mean = df['score'].mean()
print(df_mean)

#(3)
#(3-1)
df.loc['k'] = ['Saya', 17.5, 2, 'yes']
print(df)

#(3-2)
df=df.drop('k', axis=0)
print(df)

#(3-3)
df_del = df.drop('attempts', axis=1)
print(df_del)

#(3-4)
df_grp_sum = df.groupby('attempts').sum()
print(df_grp_sum)

#(4)
exam2_data = {'name':['Anastasia', 'Catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica', 'Laura', 'Klassen', 'Jonas'],
             'score2' : [11,20,16.5,np.nan,10,15,20,np.nan,8,8]}
labels2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(exam2_data, index=labels2)

df_join = pd.merge(df, df2, on='name')
print(df_join)

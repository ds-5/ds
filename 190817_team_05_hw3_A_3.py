import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# file open
df = pd.read_csv('35-data-Data_Prep.csv')


# check not null data
for col in df.columns:
    if df[col].notnull().sum() == df.shape[0]:
        print(col)
     
    
# change index column
df.set_index('iduser', inplace=True)
df = df.drop('Unnamed: 0', axis=1)


# remove missing label data
label_data = [col for col in df.columns if df[col].dtype == 'object']
df.dropna(how='any', subset=label_data, inplace=True)


# outlier
def outlier(df, types): # for not string type, skip NaN value
    b = np.full(df.shape[0], False)
    for i in range(len(df.iloc[1])):
        col_data = df.iloc[:,i]
        if col_data.dtype != 'object': # not for string
            if types == 'std': # std_based
                b |= ( abs(col_data - col_data.mean()) > 3 * col_data.std() )
            elif types == 'iqr': # iqr_based
                qt1, qt3 = np.nanpercentile(col_data, [25,75]) # ignoring NaN values
                iqr = qt3 - qt1
                lb, ub = qt1 - (iqr*1.5), qt3 + (iqr*1.5)
                b |= ((col_data > ub) | (col_data < lb))
    return df[~b]

df_std = outlier(df, 'std')
df_iqr = outlier(df, 'iqr')

# df_std : missing data to avg
df_std_filled = df_std.copy()
for col in df_std_filled.columns:
    if df_std_filled[col].isnull().sum():
        df_std_filled.fillna(value={col:df_std_filled[col].mean()}, inplace=True)
        
        
# plot without Nan values
plt.figure(figsize=(12,70))
plt.subplots_adjust(hspace=.5)
for i in range(2,20):
    plt.subplot(18,2,2*(i-2)+1)
    plt.title(df.columns[i])
    plt.boxplot((df.dropna(how='any').iloc[:,i],
                 df_iqr.dropna(how='any').iloc[:,i],
                 df_std.dropna(how='any').iloc[:,i],
                 df_std_filled.dropna(how='any').iloc[:,i]),
                labels=('org', 'iqr', 'std', 'std_filled'))
    plt.subplot(18,2,2*(i-1))
    plt.title(df.columns[i])
    sns.kdeplot(df_std.iloc[:,i].dropna(), label='std')
    sns.kdeplot(df_std_filled.iloc[:,i], label='std_filled')
plt.plot()
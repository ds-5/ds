%matplotlib inline
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Pracice 1 ======================================================================================================================

"""
    1. Standard, MinMax Max-Abs, Robust 함수 구현
"""
def standard(X):
        return (X-X.mean()) / X.std()
    
def minmax(X):
        return (X-X.min()) / (X.max()-X.min())
    
def maxabs(X):
        return X / np.abs(X).max()
    
def robust(X):
        return (X - X.median()) / (np.percentile(X, 75) - np.percentile(X, 25))
    
"""
    2. Test용 Random Data 생성 
""" 
np.random.seed(2019)
df = pd.DataFrame({
    'x1': np.random.chisquare( 8, 10000 ),
    'x2': np.random.normal( 5, 3, 10000 ),
    'x3': np.random.normal( -5, 5, 10000 ) })

"""
    3. 시각화를 위한 Plot 생성
       # 1 : base data
       # 2 : 위 구현 함수를 적용한 Scaling data
       # 3 : 구현 함수의 정합성을 검증하기 위한 SK Learn Module Scaler data
""" 
_, (ax1, ax2, ax3) = plt.subplots( ncols = 3, figsize = (9,5) )

"""
    4. Scaling 알고리즘 적용 (
       4.1 Standard Scaling 
            평균은 0, 표준편차는 1인 분포로 변환
""" 
np.random.seed(2019)
df = pd.DataFrame({
    'x1': np.random.chisquare( 8, 10000 ),
    'x2': np.random.normal( 5, 3, 10000 ),
    'x3': np.random.normal( -5, 5, 10000 ) })
_, (ax1, ax2, ax3) = plt.subplots( ncols = 3, figsize = (9,5) )

ax1.set_title('Before')
sns.kdeplot( df['x1'], ax = ax1 )
sns.kdeplot( df['x2'], ax = ax1 )
sns.kdeplot( df['x3'], ax = ax1 )

ax2.set_title('My Standard')
sns.kdeplot( standard(df['x1']), ax = ax2 )
sns.kdeplot( standard(df['x2']), ax = ax2 )
sns.kdeplot( standard(df['x3']), ax = ax2 )

scaled = preprocessing.StandardScaler().fit_transform(df)
scaled = pd.DataFrame(scaled, columns = ['x1', 'x2', 'x3'])

ax3.set_title('SK Learn StandardScaler')
sns.kdeplot( scaled['x1'], ax = ax3 )
sns.kdeplot( scaled['x2'], ax = ax3 )
sns.kdeplot( scaled['x3'], ax = ax3 )

plt.show()

"""
    4. Scaling 알고리즘 적용 (
       4.2 Min-Max scaling
            특정 범위 (0~1)로 데이터 변환
""" 
np.random.seed(2019)
df = pd.DataFrame({
    'x1': np.random.chisquare( 8, 10000 ),
    'x2': np.random.normal( 5, 3, 10000 ),
    'x3': np.random.normal( -5, 5, 10000 ) })

_, (ax1, ax2, ax3) = plt.subplots( ncols = 3, figsize = (9,5) )

ax1.set_title('Before')
sns.kdeplot( df['x1'], ax = ax1 )
sns.kdeplot( df['x2'], ax = ax1 )
sns.kdeplot( df['x3'], ax = ax1 )

ax2.set_title('My MinMax')
sns.kdeplot( minmax(df['x1']), ax = ax2 )
sns.kdeplot( minmax(df['x2']), ax = ax2 )
sns.kdeplot( minmax(df['x3']), ax = ax2 )

scaled = preprocessing.MinMaxScaler().fit_transform(df)
scaled = pd.DataFrame(scaled, columns = ['x1', 'x2', 'x3'])

ax3.set_title('SK Learn MinMaxScaler')
sns.kdeplot( scaled['x1'], ax = ax3 )
sns.kdeplot( scaled['x2'], ax = ax3 )
sns.kdeplot( scaled['x3'], ax = ax3 )

plt.show()

"""
    4. Scaling 알고리즘 적용 (
       4.3 Max-abs scaling
            최대 절대 값이 1이 되도록 변환
""" 
np.random.seed(2019)
df = pd.DataFrame({
    'x1': np.random.chisquare( 8, 10000 ),
    'x2': np.random.normal( 5, 3, 10000 ),
    'x3': np.random.normal( -5, 5, 10000 ) })

_, (ax1, ax2, ax3) = plt.subplots( ncols = 3, figsize = (9,5) )

ax1.set_title('Before')
sns.kdeplot( df['x1'], ax = ax1 )
sns.kdeplot( df['x2'], ax = ax1 )
sns.kdeplot( df['x3'], ax = ax1 )

ax2.set_title('My Max-abs')
sns.kdeplot( maxabs(df['x1']), ax = ax2 )
sns.kdeplot( maxabs(df['x2']), ax = ax2 )
sns.kdeplot( maxabs(df['x3']), ax = ax2 )

scaled = preprocessing.MaxAbsScaler().fit_transform(df)
scaled = pd.DataFrame(scaled, columns = ['x1', 'x2', 'x3'])

ax3.set_title('SK Learn MaxAbsScaler')
sns.kdeplot( scaled['x1'], ax = ax3 )
sns.kdeplot( scaled['x2'], ax = ax3 )
sns.kdeplot( scaled['x3'], ax = ax3 )

plt.show()


"""
    4. Scaling 알고리즘 적용 (
       4.4 Robust scaling
            median, IQR 사용, Outlier 영향 최소화
""" 
np.random.seed(2019)
df = pd.DataFrame({
    'x1': np.random.chisquare( 8, 10000 ),
    'x2': np.random.normal( 5, 3, 10000 ),
    'x3': np.random.normal( -5, 5, 10000 ) })

_, (ax1, ax2, ax3) = plt.subplots( ncols = 3, figsize = (9,5) )

ax1.set_title('Before')
sns.kdeplot( df['x1'], ax = ax1 )
sns.kdeplot( df['x2'], ax = ax1 )
sns.kdeplot( df['x3'], ax = ax1 )

ax2.set_title('My Robust')
sns.kdeplot( robust(df['x1']), ax = ax2 )
sns.kdeplot( robust(df['x2']), ax = ax2 )
sns.kdeplot( robust(df['x3']), ax = ax2 )

scaled = preprocessing.RobustScaler().fit_transform(df)
scaled = pd.DataFrame(scaled, columns = ['x1', 'x2', 'x3'])

ax3.set_title('SK Learn RobustScaler')
sns.kdeplot( scaled['x1'], ax = ax3 )
sns.kdeplot( scaled['x2'], ax = ax3 )
sns.kdeplot( scaled['x3'], ax = ax3 )

plt.show()

# Pracice 2 ======================================================================================================================

import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = datasets.load_boston()
dfX = pd.DataFrame( data.data, columns=data.feature_names )
dfX = dfX.drop( ['CHAS', 'RAD'], axis=1 )
dfY = pd.DataFrame( data.target, columns=['MEDV'])
regr = LinearRegression()

#TODO ++++
_, axes = plt.subplots( 11, 1, figsize = (5, 26) )
for i, ax in enumerate(axes):
    sns.kdeplot( dfX.iloc[:,i], ax=ax)
    
plt.show()

dfX.LSTAT = np.log( dfX.LSTAT )
dfX.DIS = np.log( dfX.DIS )
#TODO ----

n= 1000
avg = 0
for i in range(n):
    X_train, X_test, y_train, y_test = train_test_split( dfX, dfY, train_size = 0.7 )
    regr.fit( X_train, y_train )
    avg += regr.score( X_test, y_test )
avg/n

# Pracice 3 ======================================================================================================================

df = pd.read_csv( '35-data-Data_Prep.csv.txt', index_col=0)
df_ = df.drop( ['iduser', 'mdutype', 'group'], axis = 1)
scaler = [ preprocessing.StandardScaler() for i in df_.columns ]

def std_based_outlier(df):
    s = set()
    for colname in df.colums:
    #?? outlier = np.abs( df[colname][df[colname].notnull()] - df[colname][df[colname].notnull()] )
        s.update( outlier[outlier==True].index.tolist())
    df = df.iloc[ list( set( range( len(df))).differences(s))]
    return df

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.nanpercentile( ys, [25,75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5 )
    upper_bound = quartile_3 - (iqr * 1.5 )
    return np.where( (ys > upper_bound) | (ys<lower_bound) )

_, axes = plt.subpolt(19, 1, figsize = (5, 50))

for i, ax in enumerate(axes):
    colname = df_.columns[i]
    col = df_[colname][df_[colname].notnull()]
    col = col.values.reshape(col.shape[0], 1)
    scaler[i].fit(col)
    sns.kdeplot( scaler[i].transform(col).reshape(-1), ax = ax, label=colname )
    
df_ = std_based_outlier(df_)
df_.info()    

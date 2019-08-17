# source code
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = datasets.load_boston()
dfX = pd.DataFrame(data.data, columns=data.feature_names)
dfX = dfX.drop(['CHAS', 'RAD'], axis=1)
dfY = pd.DataFrame(data.target, columns=['MEDV'])
regr = LinearRegression()

##########################################################################
# practice 2
import numpy as np
from sklearn.preprocessing import StandardScaler, scale, robust_scale
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 1.check data
dfX.head() # eye-check
dfY.head() # eye-check
#dfX.info() # data type
dfX.describe()   # range, outlier
dfY.describe()   # range, outlier

# 2. missing values
dfX.isnull().sum() # none
dfY.isnull().sum() # none

# 3. outlier
def std_based_outlier(dfX, dfY):
    b = np.full(len(dfX), False)
    for i in range(0, len(dfX.iloc[1])):
        b |= (np.abs(dfX.iloc[:,i] - dfX.iloc[:,i].mean()) > 3 *dfX.iloc[:,i].std())
    return dfX[~b], dfY[~b]

dfX, dfY = std_based_outlier(dfX, dfY)

# 4. scaling (log or sqrt)
def plot_functions(df):
    sns.kdeplot(np.random.randn(len(df)), label='z-dist')
    sns.kdeplot(scale(df), label='normal')
    sns.kdeplot(scale(np.log(df)), label='log')
    sns.kdeplot(scale(np.sqrt(df)), label='sqrt')
    sns.kdeplot(scale(np.power(df,2)), label='x^2')
    sns.kdeplot(scale(np.power(df,3)), label='x^3')
    sns.kdeplot(robust_scale(df), label='robust')

plot_functions(dfX['AGE'])
#dfX['ZN'] = scale(np.power(dfX['ZN'], 1/3))

# 74.8
dfX['CRIM'] = scale(np.log(dfX['CRIM']))
dfX['RM'] = scale(np.power(dfX['RM'],3))
dfX['LSTAT'] = scale(np.log(dfX['LSTAT']))

dfX.describe()

##########################################################################

n = 1000
avg = 0
for i in range(n):
    X_train, X_test, y_train, y_test = train_test_split(dfX, dfY, train_size=0.7)
    regr.fit(X_train, y_train)
    avg+=regr.score(X_test, y_test)
print(avg/n)
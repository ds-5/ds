import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict

# sclaers
def standard_scaling(X):
    return (X-X.mean())/X.std()
    
def min_max_scaling(X):
    return (X-X.min())/(X.max()-X.min())
    
def max_abs_scaling(X):
    return X/((X.abs()).max())

def robust_scaling(X):
    #return (X-X.median()) / (np.percentile(X,75) - np.percentile(X,25))
    return (X-X.median()) / (stats.scoreatpercentile(X,75) - stats.scoreatpercentile(X,25))

scalers = OrderedDict([('standard', standard_scaling), ('min-max', min_max_scaling),
                       ('max-abs', max_abs_scaling), ('robust', robust_scaling)])

# sample data
np.random.seed(2019)
df = pd.DataFrame({
    'x1' : np.random.chisquare(8, 10000),
    'x2' : np.random.normal(5, 3, 10000),
    'x3' : np.random.normal(-5, 5, 10000)
})

# plot
_, axs = plt.subplots(nrows=4, ncols=2, figsize=(10,12))
plt.subplots_adjust(hspace=0.5)
for n, scaler in enumerate(scalers.keys()):
    axs[n,0].set_title('Before Scaling')
    axs[n,1].set_title('After ' + scaler + ' scaler')
    for col in df.columns:
        sns.kdeplot(df[col], ax=axs[n,0])
        sns.kdeplot(scalers[scaler](df[col]), ax=axs[n,1])
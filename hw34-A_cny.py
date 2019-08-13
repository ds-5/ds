import numpy as np
import pandas as pd
import sklearn
import sklearn.neural_network as nn
import sklearn.svm as svm
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors

rawdata = pd.read_csv('sklearn_practice.csv.txt')

class_zero = rawdata[rawdata['Class']==0]
class_one = rawdata[rawdata['Class']==1]
# 위의 2개를 합해서.. 0인 위에서 부터 250개, 밑에서 250개를 뽑아서 합치면
# 0과 1의 1:1 비율의 Test Set을 만들 수 있다.

# 정상 거래 내역 28만개에서 정상:비정상 학습 비율을 맞추기 위해 500개를 산출한다.
sampled = class_zero.sample( n=len(class_one ) )

# 정상 비정상 데이터를 합쳐 1000개 학습 데이터를 만들고 무작위로 섞는다.
data = pd.concat([class_one, sampled])
data = data.sample(frac=1)

# Train 데이터와 Test 데이터를 분리하여, 학습된 함수의 정확성을 검증한다.
train_data = data[:700]
x_train = train_data.loc[:,'Time':'Amount']
y_train = train_data.loc[:,'Class']

test_data = data[700:]
x_test = test_data.loc[:,'Time':'Amount']
y_test = test_data.loc[:,'Class']

# 학습 모델을 선정하여 적용한다.

model = lm.LogisticRegression()
#model = svm.SVC( gamma ='scale' )
#model = neighbors.KNeighborsClassifier()
#model = nn.MLPClassifier( learning_rate_init = 0.01)

model.fit(x_train, y_train)

# Test 값을 입력하여 학습 결과를 확인한다.
y_pred = model.predict(x_test)

cnt = 0
for i in range( len(y_pred) ):
    if y_pred[i] == y_test.iloc[i]:
        cnt += 1
print( cnt / len(y_pred) )

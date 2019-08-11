import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# 1-a
samples = np.random.normal(size=500)

# 1-b
np.median(samples)

# 1-c
np.std(samples)

# 1-d
stats.scoreatpercentile(samples,80)

# 1-e
loc, std = stats.norm.fit(samples)
loc, std

#2
from scipy import linalg
import numpy as np
arr = np.array([[1,3,5],
               [2,4,6],
               [6,5,8]])

#2-a
from scipy import linalg
import numpy as np
arr = np.array([[1,3,5],
               [2,4,6],
               [6,5,8]])
linalg.det(arr)

#2-b
linalg.inv(arr)

#3.
arr2 = np.array([[1,2,3,4],
                [3,8,5,2],
                [4,3,6,2]])
print(linalg.det(arr2))
# det 를 계산하는 행렬은 정방행렬이어야 하는데,
# arr2 는 3x4 행렬이므로 행과 열이 불일치.

# 4.
import numpy as np
A = np.array( [[2,2,2],[4,7,7],[6,18,22]] )
U = np.identity(3)
np.copyto(U,A)
#print('U= \n' + str(U))

# step1
U[1] = U[1] + (-2)*U[0]
E_21 = np.identity(3)
E_21[1,0] = -2
print('U = \n' + str(U))
print('E_21 = \n' + str(E_21))

# step2
U[2] = U[2] + (-3)*U[0]
E_31 = np.identity(3)
E_31[2,0] = -3
print('U = \n' + str(U))
print('E_31 = \n' + str(E_31))

#step3
U[2] = U[2] + -4*U[1]
E_32 = np.identity(3)
E_32[2,1] = -4
print('U = \n' + str(U))
print('E_32 = \n' + str(E_32))

#step4
L = np.linalg.inv(np.matmul(np.matmul(E_32, E_31), E_21))
print('L = \n' + str(L))
print('U = \n' + str(U))
print('A = \n' + str(np.matmul(L,U)))

#5. #test
P, L, U = linalg.lu(A)
print('P = \n' + str(P))
print('L = \n' + str(L))
print('U = \n' + str(U))
print('A = (inv P)LU\n' + str(np.matmul(np.matmul(linalg.inv(P), L),U)))

#6.
x_data = np.linspace(-5, 5, num=50)
y_data = 4 * np.cos(2*x_data) + np.random.normal(size=50) # mag=4, T = 2

import matplotlib.pyplot as plt
plt.scatter(x_data, y_data)
plt.show()

#7.
from scipy import optimize
cos_params, cos_params_covariance = optimize.curve_fit(lambda x, a, b : a * np.cos(b*x), x_data, y_data, p0 = [2,2])
sin_params, sin_params_covariance = optimize.curve_fit(lambda x, a, b : a * np.sin(b*x), x_data, y_data, p0 = [2,2])
plt.plot(x_data, y_data)
plt.plot(x_data, cos_params[0] * np.cos(cos_params[1]*x_data))
plt.plot(x_data, sin_params[0] * np.sin(sin_params[1]*x_data))
plt.show()

#8.
class1 = [65.9, 53.6, 57.3, 59.3, 63.8, 59.2, 64.2, 75.0, 62.9]
class2 = [76.3, 82.1, 73.3, 69.3, 59.9, 72.1, 59.1, 86.8, 78.1]
loc1, std1 = stats.norm.fit(class1)
loc2, std2 = stats.norm.fit(class2)
print('class1 =', loc1, std1)
print('class2 =', loc2, std2)
import matplotlib.pyplot as plt
from scipy.stats import norm
min_v = np.min(np.concatenate((class1,class2),0))
max_v = np.max(np.concatenate((class1,class2),0))
plt.plot(np.arange(min_v, max_v), norm.pdf(np.arange(min_v,max_v), loc=loc1, scale=std1), 'r')
plt.plot(np.arange(min_v, max_v), norm.pdf(np.arange(min_v,max_v), loc=loc2, scale=std2))

# 평균과 표준편차가 다르므로 기대값 역시 동일하지 않을 것이다.

np.min(np.concatenate((class1,class2),0))
np.max(np.concatenate((class1,class2),0))


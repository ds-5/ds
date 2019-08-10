import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# Practice 1 =====================================================================================================================

# 1-a. 정규 분포 랜덤 샘플 500개
np.random.seed(0)
samples = np.random.normal(size=500)

# 1-b. 랜덤 샘플 중앙값
np.median(samples)

# 1-c. 랜덤 샘플 표준편차
np.std(samples)

# 1-d. 랜덤 샘플 상위 20% 값
stats.scoreatpercentile(samples, 20)

# 1-e. parameter 2개(평균, 표준 편차)
loc, std = stats.norm.fit(samples)

# Practice 2 =====================================================================================================================

from scipy import linalg
import numpy as np

arr = np.array([[1,3,5],
                [2,4,6],
                [6,5,8]])
                
# 2-a. 행렬 determinant
linalg.det(arr)

# 2-b. 역행렬
linalg.inv(arr)

# Practice 3 =====================================================================================================================

arr2 = np.array( [[1,2,3,4],
                  [3,8,5,2],
                  [4,3,6,2]])
print( linalg.det(arr2) )

# 3. 위 행렬의 역행렬은? 오류의 원인은?
# 역행렬은 Square matrix에서 구할 수 있다. 주어진 행렬은 Squre matrix가 아니므로, 역행렬을 구할 수 없다.

# Practice 4 =====================================================================================================================

import numpy as np
A = np.array( [[2,2,2],[4,7,7],[6,18,22]])
U = np.identity(3)
np.copyto(U,A)
print( 'U = \n' + str(U) )

# 4. 위 행렬의 LU Decomposition 


# Practice 5 =====================================================================================================================

A = np.array( [[2,2,2],[4,7,7],[6,18,22]])

# 5. Scipy LU Decomposition
P, L, U = linalg.lu(A)
print( 'L = \n' + str(L) )
print( 'U = \n' + str(U) )
print( 'LU = \n' + str( np.matmul(P, np.matmul(L, U))) )

# Practice 6 =====================================================================================================================

# 6. 진폭 4, 주기 2인 cos 파동을 만들고, 정규 분포를 따르는 noise를 추가하시오
np.random.seed(0)
x_data = np.linspace( -5, 5, num = 50 )
y_data = 4 * np.cos(2*x_data) + np.random.normal( size=50 )

print(x_data)

%matplotlib inline
import matplotlib.pyplot as plt
plt.scatter( x_data, y_data )
plt.show()

# Practice 7 =====================================================================================================================

# 7. 위 파동 데이터 로그에서 cos 함수, sin 함수로 생성 되었을 때의 진폭과 주기를 구하시오
from scipy import optimize

cos_params, cos_params_covariance = optimize.curve_fit( lambda x, a, b : a * np.cos(b*x), x_data, y_data, p0 = [2,2] )
sin_params, sin_params_covariance = optimize.curve_fit( lambda x, a, b : a * np.sin(b*x), x_data, y_data, p0 = [2,2] )
cos_params, sin_params

# Practice 8 =====================================================================================================================

# 8. class1,2 몸무게 분포의 기댓값이 동일한가? → 동일하지 않음 

class1 = np.array( [65.9, 53.6, 57.3, 59.3, 63.8, 59.2, 64.2, 75.0, 62.9])
class2 = np.array( [76.3, 82.1, 73.3, 69.3, 59.9, 72.1, 59.1, 86.8, 78.1])

print( 'class 1 mean is ' + str(np.mean(class1)) )
print( 'class 2 mean is ' + str(np.mean(class2)) )

class 1 mean is 62.35555555555555
class 2 mean is 73.0

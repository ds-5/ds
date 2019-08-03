# hw30-A
import numpy as np
# 1. Create an array of size 10 filled with 0
np.zeros(10)
# 2. Set fifth value to 1 from above array
tmp = np.zeros(10)
tmp[4] = 1
#3. Create an aray with values ranging from 10 to 49 
np.arange(10,50)
#4. Create a 5 * 5 matrix with values ranging from 0 to 24
np.arange(0,25).reshape(5,5)
#5. Create a 5 * 5 identity matrix
np.eye(5)
#6. Create a 5 * 5 array with random values and find the minimum and maximum value
rand_arr = np.random.random((5,5))
min_var = rand_arr.min()
max_var = rand_arr.max()
#7. Multiply a 4 * 3 matrix by a 3 * 2 matrix
#a. 4 * 3 matrix is filled with 1
#b. 3 * 2 matrix is filled with random number
a = np.ones((4,3))
b = np.random.random((3,2))
c = np.dot(a,b)
#8.  Transpose the above matrix
c.T
#9. Create two matrices ranging from 0 to 24 and 25 to 49, (5 * 5 matrix!?)
#a. Add two matrix
#b. Subtract two matrix
arr1 = np.arange(0,25).reshape((5,5))
arr2 = np.arange(25,50).reshape((5,5))
op_add = arr1 + arr2
op_sub = arr1 - arr2

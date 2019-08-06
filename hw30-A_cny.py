import numpy as np

# 1. Create an array of size 10 filled with 0
a1 = np.zeros(10)

# 2. Set fifth value to 1 from above array
a1[4] = 1

# 3. Create an array with values ranging from 10 to 49
a3 = np.arange(10, 50, 1)

# 4. Create a 5 * 5 matrix with values ranging from 0 to 24
a4 = np.arange(0,25,1).reshape(5,5)

# 5. Create a 5 * 5 identity matrix
a5 = np.eye(5)

# 6. Create an 5 * 5 array with random values and find the minimum and maximun value
a6 = np.random.rand( 5,5 )
a6.min()
a6.max()

# 7. Multyply a 4 * 3 matrix by a 3.2 matrix
    #. 4 * 3 matrix is filled with 1
    #. 3 * 2 matrix is filled with random number
a7_1 = np.ones( (4,3) )
a7_2 = np.random.rand( 3, 2)
a7 = np.dot(a7_1, a7_2)

# 8. Transpose the above matrix
a8 = a7.T

# 9. Create two matrices ranging from 0 to 24 and 25 to 49
    #. Add two matrix
    #. Subtract two matrix
a9_1 = np.arange(0,25)
a9_2 = np.arange(25,50)
a9_add = a9_1 + a9_2
a9_sub = a9_1 - a9_2

import numpy as np

#(1) Create an array of size 10 filled with 0
x=np.zeros(10, dtype='i')

#(2) Set fifth value to 1 from above array
x[4] = 1

#(3) Create an array with values ranging from 10 to 49
x=np.arange(10,50)

#(4) Create a 5 * 5 matrix with values ranging from 0 to 24
x=np.arange(25).reshape((5,5))

#(5) Create a 5*5 identity matrix
x=np.eye(5, dtype='i')

#(6) Create an 5*5 array with random values and find the minimum and maximum value
x=np.random.rand(5,5)
min_x = x.min()
max_x = x.max()

'''
(7) Multiply a 4*3 matrix by a 3*2 matrix
      4*3 matrix is filled with 1
      3*2 matrix is filled with random number
'''
A=np.ones((4,3), dtype='i')
B=np.random.rand(3,2)
Mul_mat = A@B

#(8) Transpose the above matrix
Mul_mat.T

'''
(9) Create two matrices ranging from 0 to 24 and 25 to 49
     Add two matrix
     Subtract two matrix
'''
A=np.arange(25).reshape(5,5)
B=np.arange(25, 50).reshape(5,5)
Add_mat = A+B
Sub_mat = A-B

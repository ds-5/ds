# 36-A

import numpy.linalg as NL

# Q1 ==========================================================================================================================
a1_1 = np.array( [ [1,2], [3,4] ])
a1_2 = np.array( [ [1,2], [3,4], [5,6] ])

NL.eig(a1_1)
(array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356], [ 0.56576746, -0.90937671]]))

NL.eig(a1_2)
LinAlgError: Last 2 dimensions of the array must be square

NL.svd(a1_1, full_matrices=True)
(array([ [-0.40455358, -0.9145143 ],
         [-0.9145143 ,  0.40455358] ]),
 array(  [ 5.4649857 ,  0.36596619] ),
 array([ [-0.57604844, -0.81741556],
         [ 0.81741556, -0.57604844] ]))
         
NL.svd(a1_1, full_matrices=False)
(array([ [-0.40455358, -0.9145143 ],
         [-0.9145143 ,  0.40455358] ]),
 array(  [ 5.4649857 ,  0.36596619]),
 array([ [-0.57604844, -0.81741556],
         [ 0.81741556, -0.57604844] ]))
         
NL.svd(a1_2, full_matrices=True)
(array([ [-0.2298477 ,  0.88346102,  0.40824829],
         [-0.52474482,  0.24078249, -0.81649658],
         [-0.81964194, -0.40189603,  0.40824829]]),
 array(  [ 9.52551809,  0.51430058] ),
 array([ [-0.61962948, -0.78489445],
         [-0.78489445,  0.61962948]] ))
     
NL.svd(a1_2, full_matrices=False)
(array([ [-0.2298477 ,  0.88346102],
         [-0.52474482,  0.24078249],
         [-0.81964194, -0.40189603]]),
 array(  [ 9.52551809,  0.51430058]),
 array([ [-0.61962948, -0.78489445],
         [-0.78489445,  0.61962948]] ))

# Q2 ==========================================================================================================================
a2 = np.array([[7,1],[1,7]])
x, y = NL.eig(a2)
x,y

(array([8., 6.]), # ← Eigen Value 
 array([[ 0.70710678, -0.70710678], # ← Eigen Vector 
        [ 0.70710678,  0.70710678]]))

# Q3 ==========================================================================================================================
a3 = np.array([[1,1,1,0,0],[3,3,3,0,0],[4,4,4,0,0],[5,5,5,0,0],
               [0,2,0,4,4],[0,0,0,5,5],[0,1,0,2,2]])
U, S, V = NL.svd(a3, full_matrices=False)
U, S, V   

#full_matrices is False에 따라, 
# U = 7 * 5 matrix
# S = 5개 Singler Value
# V = 5 * 5 matrix 로 표현된다.

(array([[-1.37599126e-01,  2.36114514e-02,  1.08084718e-02,
          9.90147543e-01, -1.26568534e-16],
        [-4.12797378e-01,  7.08343543e-02,  3.24254153e-02,
         -5.94088526e-02, -8.85034377e-01],
        [-5.50396503e-01,  9.44458057e-02,  4.32338870e-02,
         -7.92118034e-02,  4.24264069e-01],
        [-6.87995629e-01,  1.18057257e-01,  5.40423588e-02,
         -9.90147543e-02,  1.91609371e-01],
        [-1.52775087e-01, -5.91100963e-01, -6.53650843e-01,
         -9.73880310e-17,  4.77815907e-17],
        [-7.22165140e-02, -7.31311857e-01,  6.78209218e-01,
          4.93038066e-32, -7.10764783e-17],
        [-7.63875433e-02, -2.95550482e-01, -3.26825421e-01,
         -4.86940155e-17, -3.16203559e-17]]),
 array([1.24810147e+01, 9.50861406e+00, 1.34555971e+00, 1.84716760e-16,
        9.74452038e-33]),
 array([[-5.62258405e-01, -5.92859901e-01, -5.62258405e-01,
         -9.01335372e-02, -9.01335372e-02],
        [ 1.26641382e-01, -2.87705846e-02,  1.26641382e-01,
         -6.95376220e-01, -6.95376220e-01],
        [ 4.09667482e-01, -8.04791520e-01,  4.09667482e-01,
          9.12571001e-02,  9.12571001e-02],
        [-7.07106781e-01,  3.72941547e-16,  7.07106781e-01,
         -2.84242227e-17,  2.70869285e-17],
        [-0.00000000e+00,  1.27687359e-16, -1.27687359e-16,
          7.07106781e-01, -7.07106781e-01]]))

# Q4 ==========================================================================================================================
a4 = np.array( [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
a4.reshape( (3,2,3) ) # 층, 행, 열

array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]],

       [[13, 14, 15],
        [16, 17, 18]]])   



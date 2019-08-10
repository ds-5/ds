# 36-A

# Q1 ==========================================================================================================================

import numpy.linalg as NL
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
         
    

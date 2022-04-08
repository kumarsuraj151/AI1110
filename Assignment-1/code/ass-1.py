
from numpy import *
import numpy as np

'''
[[4 2]     [[6 0]
[-1 1]] M=  [0 6]]
we have to find the matrix M
M=(A^(-1))(6I)
'''

A= matrix('4,2;-1,1')
B= matrix('6,0;0,6')
a=np.linalg.inv(A)   #it is inverse of A
M=a*B
print(M)

#the value of matrix M is;
# [[ 1. -2.]
#  [ 1.  4.]]

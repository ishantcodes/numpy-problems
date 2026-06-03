"""
Broadcasting

Add:

[10,20,30]

to every row of matrix:

[[1,2,3],
 [4,5,6],
 [7,8,9]]
"""
import numpy as np

arr= np.array([10,20,30])
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr + arr1 )

"""
Matrix Operations

Create 2 matrices.

Perform:
a
t
addition
subtraction
multiplication
transpose
"""
import numpy as np

matx1 = np.array([[1,2,3],[4,5,6]])
matx2 = np.array([[2,3,4],[6,7,8]])


print(matx1+matx2)
print(matx1-matx2)
print(matx1*matx2)
print(np.transpose(matx1))
print(np.transpose(matx2))
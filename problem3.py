"""
Reshape Problem

Create array from 1 to 24.

Convert it into:

2D array
3D array

Print shapes.
"""

import numpy as np

arr = np.arange(1,25)

arr2d = arr.reshape(4,6)
print(arr2d, arr2d.shape)

arr3d = arr.reshape(1,4,6)
print(arr3d, arr3d.shape)
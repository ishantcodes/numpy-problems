"""
Normalization Problem

Take array:

[10,20,30,40,50]

Normalize values between:

0 and 1
"""

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

normalization = (arr - np.min(arr))/(np.max(arr) - np.min(arr))
print(normalization)
"""
Even Numbers

Create array from 1 to 50.

Print:

only even numbers
only odd numbers

(using slicing/filtering)
"""

import numpy as np

arr = np.arange(1,51)

print("EVEN")
print(arr[arr % 2 ==0])
print("ODD")
print(arr[arr % 2 !=0])
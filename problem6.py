"""
temperature Analysis

Generate 30 random temperatures.

Find:

hottest day
coldest day
days above average temperature
"""
import numpy as np
import random

temp = np.random.randint(-5,45,30)

print(f"\nThe hottest day temperature is: {np.max(temp)}\n")
print(f"The coldest day temperature is: {np.min(temp)}\n")
print(f"The average temperature is: {np.mean(temp)}\n")
print(f"Temperatures above average temperature: {temp[temp>np.mean(temp)]}")
print(f"No. of days when temperature were above average temperature: {len(temp[temp>np.mean(temp)])}\n")


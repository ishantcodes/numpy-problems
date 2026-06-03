"""
Student Result System

Generate random marks for:

100 students

Then:

find topper
average marks
failed students (<33)
distinction students (>75)
"""

import numpy as np
import random

student_marks = np.random.randint(20,101,100)


topper = np.max(student_marks)
avg_marks = np.mean(student_marks)
failed = student_marks[student_marks<30]
dist = student_marks[student_marks>75]

print(f"\nTopper score: {topper}\n")
print(f"Average score: {avg_marks}\n")
print(f"Failed students score: {failed}\nNo. of failed student: {len(failed)}\n")
print(f"Distinciton students score: {dist}\nNo. of distinciton students: {len(dist)}")
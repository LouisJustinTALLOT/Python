#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def next_multiple_of_5(nb):
    for i in range(6):
        if (nb + i) % 5 == 0:
            return nb + i

def grade_rounding(grade):
    if grade < 38:
        # too small, no rounding
        return grade
    
    next_mpt_5 = next_multiple_of_5(grade)
    if next_mpt_5 - grade < 3:
        return next_mpt_5
    
    return grade

def gradingStudents(grades):
    return list(map(grade_rounding, grades))
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

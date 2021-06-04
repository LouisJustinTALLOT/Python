#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def gameWithCells(n, m):
    if n%2 == 0 and m%2 == 0:
        return n*m //4
    if n%2 == 0:
        return n*(m-1)//4 + n//2
    if m%2 == 0:
        return m*(n-1)//4 + m//2  
    return (n-1)*(m-1)//4 + (n-1)//2 + (m-1)//2 + 1      
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()

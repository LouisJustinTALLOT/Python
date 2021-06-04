#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    nb_plus = nb_minus = nb_0 = 0
    
    for el in arr:
        if el > 0:
            nb_plus += 1
        elif el < 0:
            nb_minus += 1
        else:
            nb_0 += 1
            
    length = nb_plus + nb_minus + nb_0
    
    for nb in [nb_plus, nb_minus, nb_0]:
        print(f"{nb/length:1.6f}")
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

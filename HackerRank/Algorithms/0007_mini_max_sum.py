#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max_arr = max(arr)
    min_arr = min(arr)

    if max_arr == min_arr:
        print(f"{sum(arr[1:])} {sum(arr[1:])}")
        return
       
    deja_croise_min = deja_croise_max = False
    list_min = []
    list_max = []

    
    for el in arr:
        
        if el == min_arr:
            if deja_croise_min:
                list_max.append(el)
                list_min.append(el)
            else:
                deja_croise_min = True
                list_min.append(el)
        
        elif el == max_arr:
            if deja_croise_max:
                list_max.append(el)
                list_min.append(el)
            else:
                deja_croise_max = True
                list_max.append(el)
        else: 
            list_max.append(el)
            list_min.append(el)           
        

    print(f"{sum(list_min)} {sum(list_max)}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

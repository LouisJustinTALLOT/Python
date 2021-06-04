#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = s[:2]
    am_pm = s[-2:]
    
    if am_pm.lower() == "pm":
        if hour == "12":
            # then it is right
            return s[:-2]
        else :
            new_hour = str(int(hour) + 12)
            return new_hour + s[2:-2]
        
    else: # we have am
        if hour == "12":
            # then it's midnight
            return "00" + s[2:-2]
        else:
            return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest_sums = []

    for x_len in range(len(arr) - 2):
        for y_len in range(len(arr) - 2):
            highest_sums.append(arr[x_len][y_len]\
            + arr[x_len][y_len+1]\
            + arr[x_len][y_len+2]\
            + arr[x_len+1][y_len+1]\
            + arr[x_len+2][y_len]\
            + arr[x_len+2][y_len+1]\
            + arr[x_len+2][y_len+2])
    
    return max(highest_sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
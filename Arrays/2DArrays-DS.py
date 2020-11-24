#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = []
    for i in range(4):
        for j in range(4):
            if -9 <= arr[i][j] and arr[i][j] <= 9:
                max_sum.append(
                    arr[i + 1][j+1]
                    + sum(arr[i][j : j + 3])
                    +sum(arr[i + 2][j : j + 3])
                )
    return max(max_sum)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]]


    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')
    # fptr.close()

    print(result)

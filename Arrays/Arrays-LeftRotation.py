#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    if 1 <= n and n <= pow(10, 5):
        if 1 <= d and d <= n:
            while d > 0:
                if 1 <= a[n-1] and a[n-1] <= pow(10, 6):
                    temp = a[0]
                    del(a[0])
                    a.insert(n - 1, temp)

                d -= 1
    return a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    n = 5

    d = 4

    a = [1,2,3,4,5]

    result = rotLeft(a, d)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    print(result)

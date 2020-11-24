#!/bin/python3

import math
import os
import random
import re
import sys


def swap_list_items(q, i, j):
    q[i], q[j] = q[j], q[i] 
    return q

# Complete the minimumBribes function below.
def minimumBribes(q):

    swaps = 0
    for i in range(len(q)):
        if abs(q[i] - (i + 1)) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            print(j, q[i], max(0, q[i] - 2), i)
            if q[j] > q[i]:
                swaps += 1
        print("=====")    
    print(swaps)
if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)

    n = 5

    q = [2, 1, 5, 3, 4]

    # minimumBribes(q)

    # q = [1, 2, 5, 3, 4, 7, 8, 6]

    minimumBribes(q)
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
zero=[]
p_number=[]
n_number=[]

def plusMinus(arr,n):
    # Write your code here
    for i in range(0,len(arr)):
        if arr[i] == 0:
          zero.append(arr[i])
        if arr[i] < 0:
            n_number.append(arr[i])
        if arr[i] > 0:
            p_number.append(arr[i])  
    a = len(p_number)/n
    b = len(n_number)/n
    c= len(zero)/n
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)

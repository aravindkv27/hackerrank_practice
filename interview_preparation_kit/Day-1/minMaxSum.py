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
    # Write your code here
    arr.sort()
    max_sum=0
    min_sum=0
    length_array=len(arr)
    for i in range(1, len(arr)):
        max_sum= max_sum+arr[i]
    for i in range(0,length_array-1):
        min_sum=min_sum+arr[i]
    
    print(min_sum , max_sum)
    # print(max_sum)
    # print(min_sum)
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

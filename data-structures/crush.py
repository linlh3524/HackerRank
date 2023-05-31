#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    array = [0] * (n+1)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        
        array[a-1] += k
        if b+1 <= n:
            array[b] -= k
        
    res_max = 0
    res = 0
    for dif in array:
        res += dif
        res_max = max(res_max, res)
        
    print(res_max)
    
# 官方    
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here

    array = [0] * (n+1)
    for i in range(len(queries)):
        # for j in range(queries[i][0],queries[i][1]+1):
        #     array[j]+=queries[i][2]
        a,b,k=queries[i][0],queries[i][1],queries[i][2]
        array[a-1] += k
        if b+1 <= n:
            array[b] -= k
    res_max = 0
    res = 0
    for dif in array:
        res += dif
        res_max = max(res_max, res)
    return res_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

        
        

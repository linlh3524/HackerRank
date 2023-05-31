#!/bin/python3

import sys

def breakingRecords(score):
    arr_max = [score[0]]
    arr_min = [score[0]]
    
    for el in score[1:]:
        if el < arr_min[-1]:
            arr_min.append(el)
        if el > arr_max[-1]:
            arr_max.append(el)
            
    return str(len(arr_max)-1), str(len(arr_min)-1)
        

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))


    
    #我的解决方案
    #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    n_min,n_max,c_max,c_min=max(scores)+1,-1,0,0
    for i in scores:
        if n_min>i:
            n_min=i
            c_min+=1

        if n_max<i:
            n_max=i
            c_max+=1
    return [c_min-1,c_max-1]


if __name__ == '__main__':
    fptr = open('d:\\a.txt', 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


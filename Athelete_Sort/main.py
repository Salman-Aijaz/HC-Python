#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])
    
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    arr.sort(key=lambda row:row[k])
    for row in arr:
        print(" ".join(map(str,row)))


# FORMULA TO SOLVE 
my_list=[
    [2,300,1,4,6,5],
    [86,54,67,68,98,45]
]
my_list.sort(key=lambda x:x[1])
for row in my_list:
    print(row[1])
    print(row)



# ANY OR ALL
N=int(input())
numbers = list(map(int, input().split()))
print(all(x>0 for x in numbers) and any(str(x) == str(x)[::-1] for x in numbers))
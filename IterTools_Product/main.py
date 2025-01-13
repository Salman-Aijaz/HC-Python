from itertools import product

A=[1,2]
B=[3,4]
input_A = list(map(int, [1,2]))
input_B = list(map(int, [3,4]))


print(*list(product(input_A,input_B)))
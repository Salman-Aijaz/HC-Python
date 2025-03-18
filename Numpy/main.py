# NUMPY ARRAY
# import numpy

# def arrays(arr):
#     # complete this function
#     # use numpy.array
#     return numpy.array(arr, dtype=float)[::-1]

# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)


# RESHAPE
# import numpy

# arr_input = list(map(int, input().split())) 
# my_array = numpy.array(arr_input) 
# reshape_array = my_array.reshape(3, 3)  
# print(reshape_array)

# TRANSPOSE AND FLATTEN
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy

# n, m = map(int, input().split())

# M = numpy.array([input().split() for i in range(n)], numpy.int)

# print(M.transpose())
# print(M.flatten())

# CONCATENATE 
 # Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy

#  Read input dimensions
# n, m, p = map(int, input().split())


#  Read first array
# array_1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
#  print("Array 1 ->",array_1)

#  Read second array
# array_2 = numpy.array([list(map(int, input().split())) for _ in range(m)])
#  /print("Array 2 ->",array_2)

#  Concatenating along axis=0 (vertically)
# result = numpy.concatenate((array_1, array_2), axis=0)

# print(result)
 

# ZEROS AND ONES
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy
# N=tuple(map(int,input().split()))
# print(numpy.zeros(N, dtype = numpy.int))
# print(numpy.ones(N ,dtype = numpy.int))

# EYES AND IDENTITY 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy
# numpy.set_printoptions(sign=" ")
# print(numpy.eye(*map(int,input().split())))

# SUM AND PROD 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy

# N, M = map(int, input().split())
# data = []
# for _ in range(N):
#     data.append(list(map(int, input().split())))
# data = numpy.array(data)
# data = data.sum(axis=0)
# product = data.prod()
# print(product)  


# ARRAY MATHEMATICS
# Enter your code here. Read input from STDIN. Print output to 
# import numpy as np

# n, m = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(n)]
# B = [list(map(int, input().split())) for _ in range(n)]
# a=np.array(A)
# b=np.array(B)
# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.multiply(a, b))
# print(np.floor_divide(a, b))
# print(np.mod(a, b))
# print(np.power(a, b))

# MIN AND MAX
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy 
# N,M=map(int, input().split())
# A = numpy.array([input().split() for _ in range(N)], int)
# print(numpy.max(numpy.min(A,axis=1),axis=0))
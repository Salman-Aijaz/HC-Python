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


# MEAN AND VAR
# import numpy as np

# n, m = map(int, input().split())
# list1 = [list(map(int, input().split())) for _ in range(n)]

# arr = np.array(list1)
# np.set_printoptions(precision=11, suppress=True)  # Set precision to 11 decimal places

# print(np.mean(arr, axis=1))
# print(np.var(arr, axis=0))
# print(round(np.std(arr), 11))  # Manually round std to 11 decimal places

# DOT AND CROSS
# import numpy

# n = int(input())
# a = numpy.array([input().split() for _ in range(n)], int)
# b = numpy.array([input().split() for _ in range(n)], int)
# print(numpy.dot(a,b))

# INNER AND OUTER 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy as np
# a = np.array(input().split() , int)
# b = np.array(input().split(), int)
# print(np.inner(a, b), np.outer(a, b), sep='\n')


# LINEAR ALGEBRA 
# import numpy as np

# np.set_printoptions(legacy='1.13')

# n=int(input())

# my_array=np.array([input().split() for _ in range(n)],float)
# print(np.linalg.det(my_array))

# POLYNOMINAL 
# import numpy as np

# poly = [float(x) for x in input().split()]
# x = float(input())
# print(np.polyval(poly, x))
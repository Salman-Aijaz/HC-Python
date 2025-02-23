# input()
# a = set(map(int,input().split()))
# N = int(input())

# for i in range(N):
#     operation, length_set = input().split()
#     b = set(map(int,input().split()))
#     method = getattr(a,operation)
#     method(b)
# print(sum(a))

# CHECK SUBSET 
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5, 6}
# result = A.issubset(B)
# print(result)

for i in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))
    print(len(set_a))

    b = int(input())
    set_b = set(map(int, input().split()))
    # print(len(set_b))

    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")
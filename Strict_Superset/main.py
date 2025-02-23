A=set(map(int,input().split()))
# print(A)
for _ in range(int(input())):
    X = set(map(int, input().split()))
    # print(X)
    if A.issuperset(X) != True or len(A) == len(X): 
        print(False)
        break 
else: print(True)
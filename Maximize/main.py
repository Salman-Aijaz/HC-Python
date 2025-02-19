from itertools import product
K,M=list(map(int,input().split()))
# print(K,M)

lines=[]
for item in range(K):
    lines.append(list(map(int,input().split()))[1:])
print(lines)  #REMOVE THE FIRST ELEMENT

result_list=list(product(*lines))

result=[]
for tup in result_list:
    total=0
    for item in tup:
        total=total+(item **2)
    result.append(total%M)
# print(max(result))
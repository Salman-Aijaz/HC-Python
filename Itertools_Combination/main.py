from itertools import combinations


input_A,number=input().split()


for i in range(1,int(number)+1):
    for j in combinations(sorted(input_A),i):
        print("".join(j))
# print(list(combinations(input_A_upper,number)))
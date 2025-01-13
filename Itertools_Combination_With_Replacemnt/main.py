from itertools import combinations_with_replacement


input_A,number=input().split()


for j in combinations_with_replacement(sorted(input_A),int(number)):
    print("".join(j))
from itertools import combinations

n,l,k = int(input()), list(input().split()) , int(input())
c=list(combinations(l,k))

r= [i for i in c if "a" in i ]
print(len(r)/len(c))


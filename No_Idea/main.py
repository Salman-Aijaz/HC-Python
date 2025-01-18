# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().strip().split(' '))
element_arr=list(map(int,input().strip().split(' ')))

A=set(map(int,input().strip().split(' ')))
B=set(map(int,input().strip().split(' ')))

happiness=0
for i in element_arr:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1

print(happiness)
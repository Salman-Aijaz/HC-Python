n=int(input())
num1=set(map(int,input().split()))

n=int(input())
num2=set(map(int,input().split()))
New_Set=num1.union(num2)
print(len(New_Set))
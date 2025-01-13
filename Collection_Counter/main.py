from collections import Counter
# x = 10
# inventory = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
# z = 6
# customers = [
#     (6, 55),
#     (6, 45),
#     (6, 55),
#     (4, 40),
#     (18, 60),
#     (10, 50)
# ]

x=int(input())
y = Counter(map(int,input().split()))
z=int(input())

total=0

for i in range(z):
    size,rate = map(int,input().split())
    if y[size]:
        y[size]-=1
        total+=rate

print(total)




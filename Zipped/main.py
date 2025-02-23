# student_one=[89,90,78,93,80]
# student_two=[90,91,85,88,86]
# student_three=[91,92,83,89,90.5]
  
# X=[student_one]+[student_two]+[student_three]
# print(zip(*X))

n, x = map(int, input().split())


sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i) / len(i))
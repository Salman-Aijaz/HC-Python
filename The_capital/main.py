# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
K=int(input())
room_numbers = list(map(int, input().split()))
freq=collections.Counter(room_numbers)
print(freq)
for key, value in freq.items():
    # print(key,value)
    if value != K:
        print(key)

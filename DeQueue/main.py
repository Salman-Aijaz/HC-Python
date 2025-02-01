# WITHOUT INPUT METHOD

from collections import deque

n = 6
methods = [
    "append 1",
    "append 2",
    "append 3",
    "appendleft 4",
    "pop",
    "popleft",
]

d = deque()
for method in methods:
    if method.startswith("append "):
        value = int(method.split()[1]) 
        d.append(value)
    elif method.startswith("appendleft"):  
        value = int(method.split()[1])  
        d.appendleft(value)
    elif method == "pop":  
        d.pop()
    elif method == "popleft":  
        d.popleft()

print(*d)  



# WITH INPUT METHOD
# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import deque

# # Number of operations
# n = int(input())

# # Initialize the deque
# d = deque()

# # Process each command
# for _ in range(n):
#     method = input()
#     if method.startswith("append "):
#         value = int(method.split()[1])  
#         d.append(value)
#     elif method.startswith("appendleft"):  
#         value = int(method.split()[1])  
#         d.appendleft(value)
#     elif method == "pop":  
#         d.pop()
#     elif method == "popleft":  
#         d.popleft()

# print(*d)

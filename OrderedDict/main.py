# from collections import OrderedDict
# a=OrderedDict()
# input_=int(input())
# for _ in range(input_):
#     item,space,price=input().rpartition(" ")
#     a[item]=a.get(item,0)+int(price)
# for item,price in a.items():
#     print(item,price)

GEEK = set()
GEEK.add('s')
print("Letters are:", GEEK)

# adding 'e' again
GEEK.add('e')
print("Letters are:", GEEK)
# adding 's' again
GEEK.add('s')
print("Letters are:", GEEK)
GEEK.add('s')
print("Letters are:", GEEK)
# n={"UK","China","USA","France","New Zealand"}
# # n=set("UK","China","USA","France","New Zealand")
# n.add("UK")
# print("n--->",n.__len__())

# Input values
quantity = 9
n = {1, 2, 3, 4, 5, 6, 7, 8, 9}
methods = [
    "pop",
    "remove 9",
    "discard 9",
    "discard 8",
    "remove 7",
    "pop",
    "discard 6",
    "remove 5",
    "pop",
    "discard 5",
]

# Process the commands
for method in methods:
    if method == "pop":
        # Safely pop an element if the set is not empty
        if n:
            n.pop()
    elif method.startswith("remove"):
        # Extract the number and remove it
        _, val = method.split()
        val = int(val)
        if val in n:
            n.remove(val)
    elif method.startswith("discard"):
        # Extract the number and discard it
        _, val = method.split()
        val = int(val)
        n.discard(val)

# Output the sum of the remaining elements in the set
print(sum(n))

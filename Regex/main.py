#DETECTING THE FLOAT 
# import re 

# regex = r'^[+-]?[0-9]+\.[0-9]+$'


# def check(float_no):
#     if re.search(regex, float_no):  
#         print(True)
#     else:
#         print(False)

# if __name__=="__main__":
#     n = int(input())  
#     for _ in range(n):
#         float_no = input()
#         check(float_no)


# 2nd solution
import re
pattern = r"^[+-]?\d*\.\d+$"
T = int(input())

for testcase in range(T):
    N = input()
    if re.match(pattern,N): 
        print(True) 
    else: 
        print(False)


# R.SPLIT()
regex_pattern = r"[,\.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# GROUP() GROUPS() GROUPDICT()
import re 
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
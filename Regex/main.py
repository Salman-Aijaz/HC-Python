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


# Validating Email Addresses With a Filter
import re
def fun(s):
    # return True if s is a valid email, else return False
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.match(pattern,s):
        return True
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)



# Reduce Function
from fractions import Fraction
from functools import reduce

def product(fracs):
    # print(fracs)
    t =Fraction(reduce(lambda x, y : x * y,fracs))
 # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

# RE FIND ALL AND FINDITER()
import re
vowels="aeiou"
consonants = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))

# RE.START()
import re
s = input()
k = input()

pattern = fr"(?=({k}))"
matches = re.finditer(pattern, s)
matches_list = list(matches)
if matches_list:
    for m in matches_list:
        print((m.start(1), m.end(1)-1))
else:
    print((-1, -1))

# REGEX SUBSTITUOO
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())

for i in range(N):
    line = input()
    while (' && ' in line) or (' || ' in line):
        line = line.replace(' && ', ' and ')
        line = line.replace(' || ', ' or ')

    print(line)  
    

# VALIDATING PHONE NUMBER 
import re

N = int(input())
for i in range(0, N):
    # Must start with a 7, 8, or 9 according to the problem, must only contain 10 digits total
    print('YES') if re.match(r'[789]\d{9}$', input()) else print('NO') 
        
# from collections import Counter

# # word=input()
# word="aabbbccde"

# char_count=Counter(word)

# sorted_count=sorted(char_count.items(),key=lambda x:x[1],reverse=True)
# print("Sorted_cOunt",sorted_count)

# for char,count in sorted_count:
#     if count > 1:
#         print(f"{char} {count}")


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    char_count=Counter(s)

    # Sort by frequency in descending order and by character in ascending order
    most_common = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 most common characters
    for i in range(3):
        char, count = most_common[i]
        print(char, count)
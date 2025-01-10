
# Complete the solve function below.
import os


def solve(s):
    ans = s.split(" ")
    ans1=((i.capitalize())for i in ans)
    return " ".join(ans1)

if __name__ == '__main__':
    s = input()

    result = solve(s)


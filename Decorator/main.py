# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])

        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# NAME DIRECTORY
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        print(sorted_people)
        # return map(f,sorted_people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
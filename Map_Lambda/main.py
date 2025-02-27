cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    fib_sequence=[]
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
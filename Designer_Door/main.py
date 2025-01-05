# N, M = map(int, input().split())

N=7
M=N*3

# TOP-HALF
for i in range(1, N - 1, 2):
    print(('.|.' * i).center(M, '-'))


# WELCOME LINE
print("WELCOME".center(M,"-"))

# BOTTOM LINE
for i in range(N-2, 0, -2):
    print(('.|.' * i).center(M, '-'))

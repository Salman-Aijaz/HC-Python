n = int(input())
s = set(map(int, input().split()))
N = int(input())
for step in range(N):
    a = input().split()
    if a[0] == 'pop':
        if s:
            s.remove(min(s))
    elif a[0] == 'remove':
        try:
            s.remove(int(a[1]))
        except:
            pass
    else:
        s.discard(int(a[1]))
        
print(sum(s)) 
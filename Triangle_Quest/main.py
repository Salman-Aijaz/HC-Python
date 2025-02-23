# for i in range(1,int(input())+1): print(((10**i)//9)*((10**i)//9))

# x=divmod(177,10)
# print(x)
for i in range(1,int(input())):
    print( int((i*(pow(10, i) - 1)) / 9 )) 
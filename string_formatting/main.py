n=17

width = len(bin(n)[2:])

for i in range(1,n+1):
    decimal_val=str(i)
    octal_value=oct(i)[2:]
    hexadecimal_value=hex(i)[2:].upper()
    binary_value=bin(i)[2:]
    print(f"{decimal_val.rjust(width)} {octal_value.rjust(width)} {hexadecimal_value.rjust(width)} {binary_value.rjust(width)}")

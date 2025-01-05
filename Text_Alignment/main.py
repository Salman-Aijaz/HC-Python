# # Pyramid section
# width = 11
# for i in range(1, 10, 2):  # Loop for the pyramid (1, 3, 5, 7, 9)
#     print(("H" * i).center(width, " "))

# # Two-block section
# block = "HHHHH"
# space_between = 15  # Number of spaces between the two blocks
# lines = 6  # Number of lines for the two-block section

# for _ in range(lines):
#     print((" " * 3) + (block + " " * space_between + block))  # Add 2 spaces for alignment

# width=30
# words="HHHHHHHHHHHHHHHHHHHHHHHHH"
# lines=3
# for _ in range(lines):
#    print((" "*3)+(words)+(" "*3))


# # Two-block section
# block = "HHHHH"
# space_between = 15  # Number of spaces between the two blocks
# lines = 6  # Number of lines for the two-block section

# for _ in range(lines):
#     print((" " * 3) + (block + " " * space_between + block))  # Add 2 spaces for alignment


# # Reverse pyramid section
# width = 30
# for i in range(9, 0, -2):  # Loop for reverse pyramid (9, 7, 5, ..., 1)
#     print(("H" * i).rjust(width, " "))

n=5
c = 'H'
w = " "
for k in range(n):
    print((c*(2*(k+1)-1)).center(2*n))
for k in range(n+1):
    print((c*n + w*n*(3) + c*n).center(6*n))
for k in range((n+1) // 2):
    print((c*n*5).center(6*n))
for k in range(n+1):
    print((c*n + w*n*(3) + c*n).center(6*n))
for k in range(n):
    print((c*(2*(n-k)-1)).center(2*n).rjust(6*n))
# Give the number of rows of the rhombus as static input and store it in a variable.
rhombusrows = 19
# Using Nested For loops print the rhombus star pattern.
for m in range(rhombusrows, 0, -1):
    for n in range(1, m):
        print(' ', end='')
    for k in range(0, rhombusrows):
        print('*', end='')
    print()
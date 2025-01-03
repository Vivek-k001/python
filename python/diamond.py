# Give the number of rows of the diamond pattern as static input and store it in a variable.

diamondrows = 5
# Loop from 1 to the number of rows using For Loop.
for m in range(1, diamondrows+1):
    # Loop from 1 to the number of rows -iterator value of the parent
    # For loop using another For loop(Nested For loop).
    for n in range(1, diamondrows - m + 1):
        # Print the space character in the inner For loop.
        print(end=' ')
    # Loop from 0 to the 2* iterator value - 1 of the parent For loop
    # using another For loop(Nested For loop).
    for l in range(0, (2 * m) - 1):
        # Print the star character
        print('*', end='')
    # After the end of the inner for Loops print the Newline Character.
    print()

# Loop from 1 to the number of rows using For loop.
for m in range(1, diamondrows):
    # Loop from 1 to iterator value of the parent For loop
    # using another For loop(Nested For loop).
    for n in range(1, m+1):
        # Print the space character in the inner For loop.
        print(end=' ')
    # Loop from 1 to 2*(number of rows - iterator value of the parent for loop)
    # using another For loop(Nested For loop).
    for l in range(1, (2 * (diamondrows - m))):
        # Print the star character
        print('*', end='')

    # After the end of the inner for Loops print the Newline Character.
    print()
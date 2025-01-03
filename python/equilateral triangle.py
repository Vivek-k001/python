# Give the number of rows as static input and store it in a variable.
numberOfRows = 8
# Take a variable to say g and initialize its value with (2*number of rows)-2.
g = (2*numberOfRows)-2
# Loop from 0 to the number of rows using For loop.
for m in range(0, numberOfRows):
    # Loop from 0 to g using another For Loop(Inner For loop).
    for n in range(0, g):
      # Print the space character in the inner For Loop.
        print(end=" ")
    # Decrement the value of g by 1 after the end of the inner For loop.
    g = g-1
    # Loop from 0 to m+1 using another For loop(Nested For loop)
    # where m is the iterator value of the parent For loop.
    for n in range(0, m+1):
      # Print the star character with space.
        print('*', end=" ")
    # Print the Newline character after the end of the Two inner For loops.
    print()
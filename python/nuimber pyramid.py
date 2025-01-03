# Give the number of rows as static input and store it in a variable.
numberOfRows = 8
# Loop from 1 to the number of rows using For loop.
for m in range(1, numberOfRows + 1):
    # Loop from 1 to m-1 using another For loop(Nested For loop)
    # where m is the iterator value of the parent For loop.
    for n in range(1, m - 1):
      # Print the inner loop iterator value with space.
        print(n, end=" ")
    # Loop from m-1 to 0 in decreasing order using another For loop(Nested For loop)
    # where m is the iterator value of the parent For loop.
    for n in range(m - 1, 0, -1):
      # Print the inner loop iterator value with space.
        print(n, end=" ")
    # Print the Newline character after the end of the inner loop.
    print()
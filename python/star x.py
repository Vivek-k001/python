# Give the number of rows of the x pattern as static input and store it in a variable.
xrows=10

#Loop from 0 to the number of rows using For loop.
for m in range(0, xrows):
    # Loop from 0 to the number of rows using another For loop(Inner For loop).
    for n in range(0, xrows):
        '''Check if the parent loop iterator value is equal to the inner loop 
        iterator value or if the inner loop iterator value is equal to the number
        of rows-parent loop iterator value-1 using If conditional Statement.'''
        if(m==n or n==xrows - 1 - m):
          #Print the star character with space if the condition is true.
          print('*',end=' ')
        else:
          #Else print space character.
          print(' ',end=' ')
     #Print the newline character after the end of the inner For loop.      
    print()
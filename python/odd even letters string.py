
givenstring = 'ABCDEFGHIJKLMNOP'

evenChars = ""
oddChars = ""
strnglen = len(givenstring)
for itrvalue in range(strnglen):
    if itrvalue % 2 == 0:
        oddChars = oddChars + givenstring[itrvalue]
    else:
        evenChars = evenChars + givenstring[itrvalue]
print('The given string = ', givenstring)
print('The odd characters in given string = ', oddChars)
print('The even characters in given string =', evenChars)
def calculator():
    print("simple calculator")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter the choice (1-4: )"))
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the Second number : "))
    if choice == 1:
      print(num1, "+", num2, "=", num1 + num2)
    elif choice == 2:
      print(num1, "-", num2, "=", num1 - num2)
    elif choice == 3:
      print(num1, "*", num2, "=", num1 * num2)
    elif choice == 4:
     if num2 != 0:
      print(num1, "/", num2, "=", num1 / num2)
     else:
      print("Error ! Division by Zero is not allowed .")
    else:
      print("Invalid choice ")
calculator()

        

        
    
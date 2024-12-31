import random
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter Rock , Paper, Scissors: ")
if user_choice == computer_choice: 
    print("ITS A TIE !")
elif (user_choice == "Rock" and 
computer_choice == "Scissors") or \
    (user_choice == "Scissors" and
computer_choice == "Paper") or \
    (user_choice == "Paper" and 
computer_choice == "Rock"):
    print("YOU WON !")
else:
    print("Computer Wins !")      
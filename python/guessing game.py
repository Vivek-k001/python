import random
number_to_guess = random.randint(1,10)
guess = int(input("guess a number betweeen 1 and 10: "))
if guess == number_to_guess:
    print("you won!")
else:
    print("Better luck next time!")
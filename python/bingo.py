import random

# Define the Bingo card dimensions
CARD_WIDTH = 5
CARD_HEIGHT = 5

# Define the Bingo card values
VALUES = list(range(1, 76))

# Function to generate a Bingo card
def generate_card():
    card = []
    for _ in range(CARD_HEIGHT):
        row = random.sample(VALUES, CARD_WIDTH)
        card.append(row)
    return card

# Function to print a Bingo card
def print_card(card):
    for row in card:
        print(' '.join(str(value).ljust(2) for value in row))

# Function to mark a number on a Bingo card
def mark_number(card, number):
    for row in card:
        if number in row:
            row[row.index(number)] = 'X'

# Function to check for a Bingo
def check_bingo(card):
    # Check rows
    for row in card:
        if all(value == 'X' for value in row):
            return True
    # Check columns
    for col in range(CARD_WIDTH):
        if all(row[col] == 'X' for row in card):
            return True
    # Check diagonals
    if all(card[i][i] == 'X' for i in range(CARD_WIDTH)):
        return True
    if all(card[i][CARD_WIDTH - i - 1] == 'X' for i in range(CARD_WIDTH)):
        return True
    return False

# Main game loop
def play_bingo():
    card = generate_card()
    print("Your Bingo card:")
    print_card(card)
    while True:
        number = random.choice(VALUES)
        print(f"\nThe next number is: {number}")
        mark_number(card, number)
        print("Your updated Bingo card:")
        print_card(card)
        if check_bingo(card):
            print("\nCongratulations, you got a Bingo!")
            break

play_bingo()


import random
import time
import os

# Set up some constants
WIDTH, HEIGHT = 20, 20
SNAKE = 'S'
DOT = 'D'
EMPTY = ' '

# Set up the game variables
snake = [(5, 5), (5, 6), (5, 7)]
dot = (10, 10)
direction = 'RIGHT'

# Game loop
while True:
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Draw the game board
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print(SNAKE, end=' ')
            elif (x, y) == dot:
                print(DOT, end=' ')
            else:
                print(EMPTY, end=' ')
        print()

    # Get the user input
    command = input("Enter direction (W/A/S/D): ")
    if command.upper() == 'W' and direction != 'DOWN':
        direction = 'UP'
    elif command.upper() == 'A' and direction != 'RIGHT':
        direction = 'LEFT'
    elif command.upper() == 'S' and direction != 'UP':
        direction = 'DOWN'
    elif command.upper() == 'D' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - 1)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + 1)
    elif direction == 'LEFT':
        new_head = (head[0] - 1, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + 1, head[1])

    snake.append(new_head)

    # Check if the snake ate the dot
    if snake[-1] == dot:
        dot = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.pop(0)

    # Check if the snake hit the wall or itself
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
        snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
        snake[-1] in snake[:-1]):
        print("Game over!")
        break

    # Wait for a moment
    time.sleep(0.5)

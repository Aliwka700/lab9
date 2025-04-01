import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up screen dimensions and create the screen object
WIDTH, HEIGHT, CELL = 400, 400, 20
speed, level, score = 10, 1, 0

# Define colors
BLACK, GREEN, RED, WHITE = (0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255)

# Create screen and initialize clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
snake = [(5, 5)]  # Initial snake body
direction = (1, 0)  # Start by moving to the right

# Function to generate food with random size
def new_food():
    size = random.randint(10, 20)  # Random food size between 10 and 20
    while (pos := (random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))) in snake:
        pass
    return pos, size

# Function to check if food has disappeared due to time limit
def check_food_timer(food_time, max_time=5):
    # If the food is older than the max_time, regenerate it
    return time.time() - food_time > max_time

# Initialize food and its spawn time
food, food_size = new_food()
food_time = time.time()

# Set up game clock
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
            if event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
            if event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    # Update snake head position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # If the snake hits itself or the wall, end the game
    if new_head in snake or not (0 <= new_head[0] < WIDTH // CELL and 0 <= new_head[1] < HEIGHT // CELL):
        break

    snake.insert(0, new_head)

    # Check if the snake ate food
    if new_head == food:
        score += 1
        food, food_size = new_food()  # Generate new food
        food_time = time.time()  # Reset food timer

    else:
        snake.pop()  # Remove the last part of the snake if no food was eaten

    # Check if food has disappeared (food timer expired)
    if check_food_timer(food_time):
        food, food_size = new_food()  # Regenerate food if time has expired
        food_time = time.time()  # Reset food timer

    # Draw the snake
    for seg in snake:
        pygame.draw.rect(screen, GREEN, (seg[0] * CELL, seg[1] * CELL, CELL, CELL))

    # Draw the food with a random size
    pygame.draw.rect(screen, RED, (food[0] * CELL, food[1] * CELL, food_size, food_size))

    # Display score and level

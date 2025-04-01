import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and setting up the game window
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")  # Set the window title to "Racer"

# Load and set up images for the background, car, coin, and obstacle
bg_img = pygame.image.load("background-1.png")  # Load the background image
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))  # Scale the background to fit the screen
car_img = pygame.image.load("12.png")  # Load the car image
coin_img = pygame.image.load("Coin2.png")  # Load the coin image
obstacle_img = pygame.image.load("spr_boulder_0.png")  # Load the obstacle image

# Scale the images to appropriate sizes
car_img = pygame.transform.scale(car_img, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))
obstacle_img = pygame.transform.scale(obstacle_img, (50, 50))

# Game objects (car, coin, obstacle) with initial positions
car = pygame.Rect(225, 500, 50, 100)  # Car's coordinates and size
coin = pygame.Rect(random.randint(50, WIDTH - 50), -50, 30, 30)  # Coin's coordinates (randomly placed along x-axis)
obstacle = pygame.Rect(random.randint(50, WIDTH - 50), -150, 50, 50)  # Obstacle's coordinates (randomly placed along x-axis)

# Game settings (car speed, object speed, score, and font)
car_speed = 5
object_speed = 5
score = 0
font = pygame.font.Font(None, 36)  # Font for displaying the score

# Variables for random coin weight and increasing speed after collecting coins
coin_weight = random.randint(1, 3)  # Random weight of the coin
coins_collected = 0  # Number of coins collected
speed_increase_threshold = 10  # The threshold of coins collected to increase speed

# Main game loop
running = True
while running:
    screen.blit(bg_img, (0, 0))  # Draw the background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the game window if user clicks close
            running = False
    
    keys = pygame.key.get_pressed()  # Get the keys pressed by the user
    if keys[pygame.K_LEFT] and car.x > 0:  # Move left if the left arrow key is pressed
        car.x -= car_speed
    if keys[pygame.K_RIGHT] and car.x < WIDTH - car.width:  # Move right if the right arrow key is pressed
        car.x += car_speed
    
    # Move the coin and obstacle down the screen
    coin.y += object_speed
    obstacle.y += object_speed
    
    # Check if the car collides with the coin
    if car.colliderect(coin):
        score += coin_weight  # Increase score by the coin's weight
        coins_collected += 1  # Increment the number of coins collected
        coin.y = -50  # Reset the coin to a random position above the screen
        coin.x = random.randint(50, WIDTH - 50)
        coin_weight = random.randint(1, 3)  # Randomly change the weight of the next coin
    
    # Check if the car collides with the obstacle
    if car.colliderect(obstacle):
        running = False  # End the game if the car hits an obstacle
    
    # If coin or obstacle goes out of the screen, reset them to a random position
    if coin.y > HEIGHT:
        coin.y = -50
        coin.x = random.randint(50, WIDTH - 50)
    if obstacle.y > HEIGHT:
        obstacle.y = -150
        obstacle.x = random.randint(50, WIDTH - 50)
    
    # Increase the speed of objects when the player collects N coins
    if coins_collected >= speed_increase_threshold:
        object_speed += 1  # Increase the speed of the coin and obstacle
        speed_increase_threshold += 10  # Increase the threshold to raise the speed again

    # Draw the car, coin, and obstacle on the screen
    screen.blit(car_img, (car.x, car.y))
    screen.blit(coin_img, (coin.x, coin.y))
    screen.blit(obstacle_img, (obstacle.x, obstacle.y))
    
    # Display the current score on the screen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (350, 20))
    
    # Update the display
    pygame.display.flip()
    
    # Delay to control the game speed
    pygame.time.delay(30)

# Quit Pygame when the game ends
pygame.quit()


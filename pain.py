import pygame
import math

# Initialize Pygame
pygame.init()

# Set up screen dimensions and create the screen object
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Define colors for drawing (white for background, black, red, blue for drawing)
WHITE, BLACK, RED, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255)
colors = [BLACK, RED, BLUE]  # List of available colors
color_index = 0  # Start with the first color
current_color = colors[color_index]  # Current color to use for drawing

mode = "pen"  # Start in 'pen' mode (default drawing mode)
screen.fill(WHITE)  # Fill the screen with white color
pygame.display.flip()  # Update the display

# Variables to track the drawing state and mouse position
drawing, start_pos = False, None
running = True

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, color, position, size):
    x, y = position
    points = [
        (x, y - size),  # Top point
        (x - size * math.cos(math.radians(30)), y + size / 2),  # Bottom-left point
        (x + size * math.cos(math.radians(30)), y + size / 2)  # Bottom-right point
    ]
    pygame.draw.polygon(surface, color, points)

# Function to draw a rhombus
def draw_rhombus(surface, color, position, size):
    x, y = position
    points = [
        (x, y - size),  # Top point
        (x - size, y),  # Left point
        (x, y + size),  # Bottom point
        (x + size, y)   # Right point
    ]
    pygame.draw.polygon(surface, color, points)

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Key presses to change drawing mode
            if event.key == pygame.K_r: mode = "rect"       # Rectangle
            if event.key == pygame.K_c: mode = "circle"     # Circle
            if event.key == pygame.K_e: mode = "eraser"     # Eraser
            if event.key == pygame.K_p: mode = "pen"        # Pen
            if event.key == pygame.K_t: mode = "triangle"   # Equilateral Triangle
            if event.key == pygame.K_h: mode = "rhombus"    # Rhombus
            if event.key == pygame.K_SPACE:  # Change color when space is pressed
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing, start_pos = True, event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            # Based on the mode, draw different shapes
            if mode == "rect":
                pygame.draw.rect(screen, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                pygame.draw.circle(screen, current_color, start_pos, abs(end_pos[0] - start_pos[0]) // 2, 2)
            elif mode == "triangle":
                size = abs(end_pos[0] - start_pos[0])  # Use the width as the size
                draw_equilateral_triangle(screen, current_color, start_pos, size)
            elif mode == "rhombus":
                size = abs(end_pos[0] - start_pos[0])  # Use the width as the size
                draw_rhombus(screen, current_color, start_pos, size)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(screen, current_color, start_pos, event.pos, 2)
                start_pos = event.pos
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)
    
    pygame.display.flip()  # Update the screen

pygame.quit()  # Quit Pygame when the loop ends

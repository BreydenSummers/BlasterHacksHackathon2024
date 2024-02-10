import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update the screen
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()


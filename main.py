
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Screen Example")

# Game variables
scroll_speed = 5
scroll_x = 0

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Scroll screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        scroll_x += scroll_speed
    if keys[pygame.K_RIGHT]:
        scroll_x -= scroll_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw game elements (adjusted by scroll position)
    # For demonstration, let's draw a grid
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(screen, (0, 0, 0), (x + scroll_x, 0), (x + scroll_x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 50):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
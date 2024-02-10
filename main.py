
import pygame
import sys
from tower import tower
from map import map

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
side_scroll_speed = 5
scroll_x = 0
vertical_scroll_speed = 5
scroll_y = 0


objects = []
# We need a better way to keep track of the buildings
objects.append(tower(150, 300, 90, 2, stat=True))
objects.append(tower(1500, 300, 270, .3, stat=True, base="fountain"))
objects.append(tower(600, 150, mult=1, stat=False))
objects.append(tower(600, 700, rot=180, mult=1, stat=False))
objects.append(tower(1200, 130, 270, .15, stat=False, base="fountain"))
objects.append(tower(1200, 700, 270, .15, stat=False, base="fountain"))
game_map = map(scroll_x,scroll_y)

def update(screen, objects):
    for object in objects:
        object.update(scroll_x,scroll_y)

def render(screen, objects):
    game_map.render(screen, scroll_x, scroll_y)
    for object in objects:
        object.render(screen, scroll_x, scroll_y)

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
    if keys[pygame.K_a]:
        if scroll_x < 0:
            scroll_x += side_scroll_speed
    if keys[pygame.K_d]:
        if scroll_x > game_map.width:
            scroll_x -= side_scroll_speed
    if keys[pygame.K_w]:
        if scroll_y < 0:
            scroll_y += vertical_scroll_speed
    if keys[pygame.K_s]:
        if scroll_y > game_map.height:
            scroll_y -= vertical_scroll_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw game elements (adjusted by scroll position)
    # For demonstration, let's draw a grid
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(screen, (0, 0, 0), (x + scroll_x, 0), (x + scroll_x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 50):
        pygame.draw.line(screen, (0, 0, 0), (0, y + scroll_y), (SCREEN_WIDTH, y + scroll_y))

    update(screen, objects)
    render(screen, objects)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
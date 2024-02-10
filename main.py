
import pygame
import sys
from tower import Tower
from map import map
from units import Unit
from UI import UI
from units import Unit

# Initialize Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('amb.mp3')
pygame.mixer.music.play(loops=-1)

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
objects.append(Tower(150, 300, 90, 2, stat=True))
objects.append(Tower(1500, 300, 270, .3, stat=True, base="fountain"))
objects.append(Tower(600, 150, mult=1, stat=False))
objects.append(Tower(600, 700, rot=180, mult=1, stat=False))
objects.append(Tower(1200, 130, 270, .15, stat=False, base="fountain"))
objects.append(Tower(1200, 700, 270, .15, stat=False, base="fountain"))
objects.append(Unit(40,40,40,40,"BLUE"))

UI_table = UI(screen, scroll_x, scroll_y)
game_map = map(scroll_x, scroll_y)

def update(screen, objects, moveDestination):
    for object in objects:
        object.update(objects, moveDestination)

def render(screen, objects):
    game_map.render(screen, scroll_x, scroll_y)
    
    for object in objects:
        object.render(screen, scroll_x, scroll_y)

    UI_table.render(screen, scroll_x, scroll_y)

# Main game loop
clock = pygame.time.Clock()
running = True
dragging = False
start_drag_pos = None
selected_rects = []
selection_rect = None
draw_rect = None
while running:


    # Handle events

    

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

    moveDestination = None

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
                    start_drag_pos = event.pos
                    for sprite in objects:
                        sprite.selected = False
                    selected_rects = []
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
                    for sprite in objects:
                        if sprite.rect.colliderect(selection_rect):
                            sprite.selected = True
                            selected_rects.append(sprite)
                    selection_rect.width = 0
                    selection_rect.height = 0
                if event.button == 3:
                    moveDestination = event.pos

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    end_drag_pos = event.pos
                    selection_rect = pygame.Rect((start_drag_pos[0] - scroll_x, start_drag_pos[1] - scroll_y),
                                                (end_drag_pos[0] - start_drag_pos[0] + scroll_x , end_drag_pos[1] - start_drag_pos[1] + scroll_y ))
                    draw_rect = pygame.Rect(start_drag_pos, (end_drag_pos[0] - start_drag_pos[0], end_drag_pos[1] - start_drag_pos[1]))

    # Clear the screen
    screen.fill(WHITE)

    # Draw game elements (adjusted by scroll position)
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(screen, (0, 0, 0), (x + scroll_x, 0), (x + scroll_x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 50):
        pygame.draw.line(screen, (0, 0, 0), (0, y + scroll_y), (SCREEN_WIDTH, y + scroll_y))

    update(screen, objects, moveDestination)
    render(screen, objects)
    if dragging and selection_rect != None:
        pygame.draw.rect(screen, "BLUE", draw_rect, 1)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
import pygame

class Unit:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def update(self):
        # You can implement any update logic here, such as movement or AI behavior
        pass

    def render(self, screen, scroll_x, scroll_y):
        pygame.draw.rect(screen, self.color, (self.x + scroll_x, self.y + scroll_y, self.width, self.height))

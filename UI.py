import pygame

class UI:
    def __init__(self, screen, x, y):
        self.width = screen.get_width()
        self.height = 100
        self.x = 0
        self.y = screen.get_height() - self.height
        
        self.UI_block = pygame.Rect(self.x, self.y, self.width, self.height)


    def render(self, screen, scroll_x, scroll_y):
        pygame.draw.rect(screen, (130, 180, 130), self.UI_block)
        pygame.draw.rect(screen, (200, 225, 200), (self.x + 5, self.y + 5, self.width - 10, self.height - 10))


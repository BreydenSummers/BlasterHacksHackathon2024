import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.selected = False

    def update(self, scroll_x, scroll_y):
        if self.selected:
            self.image.fill("red")
        else:
            self.image.fill("blue")

    def render(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (scroll_x + self.rect.topleft[0], scroll_y + self.rect.topleft[1]))
        # pygame.draw.rect(screen, self.color, (self.x + scroll_x, self.y + scroll_y, self.width, self.height))

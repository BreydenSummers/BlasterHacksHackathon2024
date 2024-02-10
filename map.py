import pygame

class map:

    def __init__(self, x, y):
        self.center = 0
        #This has negative numbers due to counting backwards
        self.width = -1240
        self.height = -420

        self.layer = 0
        self.bg_map = pygame.image.load('images/lol.png').convert()

    def render(self, screen, scroll_x, scroll_y):
        screen.blit(self.bg_map, (scroll_x, scroll_y))



import pygame 

class tower :

    def __init__(self, x, y) :
        # sprite attributes
        # self.sprite
        # self.health
        # self.menu_description
        # self.team   #human or forest...

        # position attributes``
        self.x = x
        self.y = y

        self.width = 150
        self.height = 450

        # health bar attributes 
        self.hbar_x = (self.width/2)
        self.hbar_y = y-self.height/8

    def draw_health(self, screen, scroll_x, scroll_y): 
        GREEN = (0, 255, 0)
        pygame.draw.rect(screen, (0, 0, 0), (scroll_x + self.hbar_x-5, scroll_y + self.hbar_y-5, 60, 25))
        pygame.draw.rect(screen, GREEN, (scroll_x + self.hbar_x, scroll_y + self.hbar_y, 50, 15))

    def render(self, screen, scroll_x, scroll_y):
        BLUE = (0, 0, 255)
        self.draw_health(screen, scroll_x, scroll_y)
        pygame.draw.rect(screen, BLUE, (scroll_x + self.x, scroll_y + self.y, self.width, self.height))

    def update(self, x_offset, y_offset):

        pass
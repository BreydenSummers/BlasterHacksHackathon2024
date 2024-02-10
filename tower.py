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

        self.hbar_width = 50
        self.hbar_height = 15
        self.hbar_bordersize = 10

    def draw_health(self, screen, scroll_x, scroll_y): 
        GREEN = (0, 255, 0)
        pygame.draw.rect(screen, (0, 0, 0), (scroll_x + self.hbar_x-5, scroll_y + self.hbar_y-5, 
                                             self.hbar_width+self.hbar_bordersize, self.hbar_height+self.hbar_bordersize))
        pygame.draw.rect(screen, GREEN, (scroll_x + self.hbar_x, scroll_y + self.hbar_y, self.hbar_width, self.hbar_height))

    def render(self, screen, scroll_x, scroll_y):
        BLUE = (0, 0, 255)
        self.draw_health(screen, scroll_x, scroll_y)
        pygame.draw.rect(screen, BLUE, (scroll_x + self.x, scroll_y + self.y, self.width, self.height))

    def take_damage(self):
        pass

    def update(self, x_offset, y_offset):
        
        pass
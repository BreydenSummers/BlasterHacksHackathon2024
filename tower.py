import pygame 

class tower :
    def tower(self) :
        # sprite attributes
        self.sprite
        self.health
        self.menu_description
        self.team   #human or forest...

        # position attributes``
        self.x
        self.y

        # health bar attributes 
        self.hbar_x
        self.hbar_y

    def draw_health(): 
        pass

    def render(self, screen):
        BLUE = (0, 0, 255)
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 300, 900))

    def update(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

        self.hbar_x += x_offset
        self.hbar_y += y_offset
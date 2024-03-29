import pygame 
import math
from units import Unit

class Tower :

    def __init__(self, x, y, rot=0, mult=1, stat=False, base="Base") :
        # sprite attributes
        # self.sprite
        self.health = 5
        # self.menu_description
        # self.team   #human or forest...

        # position attributes``
        self.x = x
        self.y = y
        self.rot = rot
        self.mult = mult
        self.base = base
        self.stat = stat
        self.base_capture = 0

        self.rect = pygame.Rect(x,y,10,10)

        self.xshift = 0
        self.yshift = 0

        self.human_base = pygame.image.load(f'images/{self.base}.png').convert_alpha()
        self.width = self.human_base.get_width()
        self.height = self.human_base.get_height()

        # health bar attributes 
        self.hbar_x = (self.width/2)
        self.hbar_y = y-self.height/8

        self.hbar_width = self.health*10
        self.hbar_height = 15
        self.hbar_bordersize = 10

        
        self.human_base_main = pygame.transform.scale(self.human_base, (self.width * self.mult, self.height * self.mult))
        self.human_base_main = pygame.transform.rotate(self.human_base_main, self.rot)
        self.human_base_main_active = self.human_base_main
        if not stat:
            color_shift = (120, 120, 120)
            color_surface = pygame.Surface((self.width * self.mult, self.height * self.mult))
            color_surface.fill(color_shift)
            color_surface.set_alpha(50)
            # Chat GPT made this section as I didn't know about the special flags that were availible. This built an inmage on top of the first that added a multiply effect like in photoshop
            self.human_base_main.blit(color_surface, (0, 0), special_flags=pygame.BLEND_MULT)



    def draw_health(self, screen, scroll_x, scroll_y): 
        GREEN = (0, 255, 0)
        pygame.draw.rect(screen, (0, 0, 0), (scroll_x + self.hbar_x-5, scroll_y + self.hbar_y-5, 
                                             self.hbar_width+self.hbar_bordersize, self.hbar_height+self.hbar_bordersize))
        pygame.draw.rect(screen, GREEN, (scroll_x + self.hbar_x, scroll_y + self.hbar_y, self.hbar_width, self.hbar_height))

    def render(self, screen, scroll_x, scroll_y):
        self.draw_health(screen, scroll_x, scroll_y)
        if self.stat == False:
            screen.blit(self.human_base_main, (scroll_x + self.x, scroll_y + self.y))
        else:
            screen.blit(self.human_base_main_active, (scroll_x + self.x, scroll_y + self.y))

        self.xshift = scroll_x + self.x
        self.yshift = scroll_y + self.y


    def take_damage(self):
        pass

    # def update(self, x_offset, y_offset):

    def update(self, objectList, moveDestintation):
        for obj in objectList:
            if isinstance(obj, Unit):
                if self.stat == False:
                    if self.base_capture < 100:
                        if math.sqrt((obj.rect.x - self.xshift)**2 + (obj.rect.y - self.yshift)**2) <= 50:
                            print(obj.rect.x)
                            print(self.xshift)
                            print(obj.rect.y)
                            print(self.yshift)
                            self.base_capture = 100
                            self.stat = True

                    

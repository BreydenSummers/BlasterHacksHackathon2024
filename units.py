import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.selected = False

    def update(self, object_list, moveDestination):
        # You can implement any update logic here, such as movement or AI behavior
        # current_closest = Unit()
        # closest_distance = 10000
        # for object in object_list:
        #     distance = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
        #     if object.team is not self.team and distance < closest_distance:
        #         current_closest = object
        #         closest_distance = distance

            # TODO move the unit towards the enemies....ONWARDS!!!
        if self.selected:
            self.image.fill("red")
        else:
            self.image.fill("blue")

        if moveDestination != None and self.selected:
            self.rect.x = moveDestination[0]
            self.rect.y = moveDestination[1]

        pass

    def render(self, screen, scroll_x, scroll_y):
        pygame.draw.rect(screen, self.color, (self.x + scroll_x, self.y + scroll_y, self.width, self.height))


    
    # def update(self, scroll_x, scroll_y, moveDestination=None):
        
    def render(self, screen, scroll_x, scroll_y):
        screen.blit(self.image, (scroll_x + self.rect.topleft[0], scroll_y + self.rect.topleft[1]))
        # pygame.draw.rect(screen, self.color, (self.x + scroll_x, self.y + scroll_y, self.width, self.height))

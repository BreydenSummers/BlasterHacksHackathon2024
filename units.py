import pygame

class Unit:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        

    def update(self, object_list):
        # You can implement any update logic here, such as movement or AI behavior
        current_closest = Unit()
        closest_distance = 10000
        for object in object_list:
            distance = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
            if object.team is not self.team and distance < closest_distance:
                current_closest = object
                closest_distance = distance

            # TODO move the unit towards the enemies....ONWARDS!!!
        pass

    def render(self, screen, scroll_x, scroll_y):
        pygame.draw.rect(screen, self.color, (self.x + scroll_x, self.y + scroll_y, self.width, self.height))


    
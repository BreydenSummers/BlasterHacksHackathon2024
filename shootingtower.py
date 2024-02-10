from tower import Tower
class shootingTower (Tower) :
    def attack(self, object_list):
        for object in object_list:
            distance = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
            if object.team is not self.team and distance < 20: 
                # TODO put a animation here for attacking
                object.health - .1

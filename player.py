class player:
    def __init__(self):
        
        self.points = 200
        self.gen_points = 100
        self.control_points = 0
        
    def get_points(self):
        return self.points
    
    def get_control(self):
        return self.control_points
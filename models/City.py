class City(object):

    def __init__(self, index, x_coord, y_coord):
        self.number = index
        self.x = x_coord
        self.y = y_coord
    
    def __str__(self):
        return f"City {self.number}: ({self.x}, {self.y})"
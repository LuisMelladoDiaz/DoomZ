from constants import SCREEN_WIDTH


class Wall:
    def __init__(self, x1, y1, x2, y2, color):

        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

        self.color = color

class Sector:
    def __init__(self, first_wall, last_wall, floor, roof, bcolor, tcolor):

        self.first_wall = first_wall
        self.last_wall = last_wall

        self.floor = floor
        self.roof = roof

        self.center_x = 0
        self.center_y = 0

        self.distance = 0
        self.bcolor = bcolor
        self.tcolor = tcolor

        self.surface_points = [0] * SCREEN_WIDTH
        self.surface = 0

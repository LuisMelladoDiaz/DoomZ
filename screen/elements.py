from constants import SCREEN_WIDTH


class Wall:
    def __init__(self, x1, y1, x2, y2, color):

        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

        self.color = color

class Sector:
    def __init__(self, first_wall, last_wall, floor, roof, center_x, center_y, distance, bcolor, tcolor):

        self.first_wall = first_wall
        self.last_wall = last_wall

        self.floor = floor
        self.roof = roof

        self.center_x = center_x
        self.center_y = center_y

        self.distance = distance

        self.bcolor = bcolor
        self.tcolor = tcolor

        self.surface_points = [0] * SCREEN_WIDTH
        self.surface = 0


sectors = [
    Sector(0, 4, 0, 40, 0, 0, 0, 4, 5),
    Sector(4, 8, 0, 20, 0, 0, 0, 4, 5),
]

walls = [
    Wall(0, 0, 32 , 0, 0),
    Wall(32, 0, 32 , 32, 1),
    Wall(32, 32, 0 , 32, 0),
    Wall(0, 32, 0 , 0, 1),

    Wall(64, 0, 96 , 0, 2),
    Wall(96, 0, 96 , 32, 3),
    Wall(96, 32, 64 , 32, 2),
    Wall(64, 32, 64 , 0, 3),
]
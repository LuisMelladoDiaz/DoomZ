import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from constants import *
from maths.distances import distance_point_point
from player.player import P
from screen.clipping import clip, clip_behind_player
from screen.elements import *

tick = 0

# Function to draw a pixel
def pixel(x, y, c):
    rgb = [[255, 0, 0], [160, 160, 0], [0, 255, 0], [0, 160, 0],
           [0, 255, 255], [0, 160, 160], [160, 100, 0], [110, 50, 0],
           [0, 60, 130]]  # RGB values for colors

    glColor3ub(*rgb[c])
    glBegin(GL_POINTS)
    glVertex2i(int(x * PIXEL_SCALE + 2), int(y * PIXEL_SCALE + 2))
    glEnd()

# Function to clear the background
def clearBackground():
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            pixel(x, y, 8)

# Function to draw the 3D scene
def draw3D():

    cos = math.cos(P.horizontal_angle)
    sin = math.sin(P.horizontal_angle)

    for sector in range(NUM_SECTORS):
        sectors[sector].distance = 0

        if(P.z < sectors[sector].floor): sectors[sector].surface = 1
        elif(P.z > sectors[sector].roof): sectors[sector].surface = 2
        else: sectors[sector].surface = 0
        for i in range(0,2):
            for wall in range(sectors[sector].first_wall, sectors[sector].last_wall):

                x1 = walls[wall].x1 - P.x
                y1 = walls[wall].y1 - P.y

                x2 = walls[wall].x2 - P.x
                y2 = walls[wall].y2 - P.y

                if i == 0:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                #World X position
                wx = [0.0] * 5
                wx[0] = x1 * cos - y1 * sin
                wx[1] = x2 * cos - y2 * sin
                wx[2] = wx[0]
                wx[3] = wx[1]

                #World Y position (DEPTH)
                wy = [0.0] * 5
                wy[0] = y1 * cos + x1 * sin
                wy[1] = y2 * cos + x2 * sin
                wy[2] = wy[0]
                wy[3] = wy[1]

                sectors[sector].distance += distance_point_point(0, 0, (wx[0]+wx[1])/2, (wy[0]+wy[1])/2)

                #World Z position (HEIGHT)
                wz = [0.0] * 5
                wz[0] = sectors[sector].floor - P.z + ((P.vertical_angle*wy[0])/32.0)
                wz[1] = sectors[sector].floor - P.z + ((P.vertical_angle*wy[1])/32.0)
                wz[2] = wz[0] + sectors[sector].roof
                wz[3] = wz[1] + sectors[sector].roof

                #Handle Postions Behind Player
                if(wy[0] < 1 and wy[1] > 1): continue

                if wy[0] < 1:
                    wx[0], wy[0], wz[0] = clip_behind_player(wx[0], wy[0], wz[0], wx[1], wy[1], wz[1])
                    wx[2], wy[2], wz[2] = clip_behind_player(wx[2], wy[2], wz[2], wx[3], wy[3], wz[3])

                if wy[1] < 1:
                    wx[1], wy[1], wz[1] = clip_behind_player(wx[1], wy[1], wz[1], wx[0], wy[0], wz[0])
                    wx[3], wy[3], wz[3] = clip_behind_player(wx[3], wy[3], wz[3], wx[2], wy[2], wz[2])

                #Screen position
                wx[0] = wx[0] * 200 / wy[0] + HALF_SCREEN_WIDTH
                wy[0] = wz[0] * 200 / wy[0] + HALF_SCREEN_HEIGH

                wx[1] = wx[1] * 200 / wy[1] + HALF_SCREEN_WIDTH
                wy[1] = wz[1] * 200 / wy[1] + HALF_SCREEN_HEIGH

                wy[2] = wz[2] * 200 / wy[2] + HALF_SCREEN_HEIGH
                wy[3] = wz[3] * 200 / wy[3] + HALF_SCREEN_HEIGH

                draw_wall(wx[0], wx[1], wy[0], wy[1], wy[2], wy[3], walls[wall].color, sectors[sector])
            sectors[sector].distance /= (sectors[sector].last_wall - sectors[sector].first_wall)
            sectors[sector].surface *= -1


def draw_wall (x1, x2, b1, b2, t1, t2, color, sector):
    dyb = b2 - b1
    dyt = t2 - t1
    dx = x2 - x1

    x1 = clip(x1, SCREEN_WIDTH)
    x2 = clip(x2, SCREEN_WIDTH)

    for x in range(int(x1),int(x2)):
        y1 = dyb * (x - x1 + 0.5) / dx + b1
        y2 = dyt * (x - x1 + 0.5) / dx + t1

        y1 = clip(y1, SCREEN_HEIGHT)
        y2 = clip(y2, SCREEN_HEIGHT)

        if(sector.surface == 1):
            sector.surface_points[x] = y1
            continue

        if(sector.surface == 2):
            sector.surface_points[x] = y2
            continue

        if(sector.surface == -1):
            for y in range(int(sector.surface_points[x]), int(y1)):
                pixel(x,y,sector.bcolor)

        if(sector.surface == -2):
            for y in range(int(y2), int(sector.surface_points[x])):
                pixel(x,y,sector.bcolor)

        for y in range(int(y1),int(y2)):
            pixel(x,y,color)


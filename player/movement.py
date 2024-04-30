import math
from player.player import P


class Keys:
    def __init__(self):
        self.w = 0
        self.s = 0
        self.a = 0
        self.d = 0
        self.sl = 0
        self.sr = 0
        self.m = 0

K = Keys()


# Function to move the player
def movePlayer():

    if K.a == 1 and K.m == 0:
        P.horizontal_angle -= 0.15
        # if P.horizontal_angle < 0:
            # P.horizontal_angle += 360

    if K.d == 1 and K.m == 0:
        P.horizontal_angle += 0.15
        # if P.horizontal_angle > 359:
            # P.horizontal_angle -= 360

    dx = math.sin(P.horizontal_angle)*15.0
    dy = math.cos(P.horizontal_angle)*15.0

    if K.w == 1 and K.m == 0:
        P.x += dx
        P.y += dy

    if K.s == 1 and K.m == 0:
        P.x -= dx
        P.y -= dy

    if K.sr == 1:
        P.x += dy
        P.y -= dx

    if K.sl == 1:
        P.x -= dy
        P.y += dx

    if K.a == 1 and K.m == 1:
        P.vertical_angle -= 1

    if K.d == 1 and K.m == 1:
        P.vertical_angle += 1

    if K.w == 1 and K.m == 1:
        P.z -=4

    if K.s == 1 and K.m == 1:
        P.z += 4


# Keyboard function for key press
def KeysDown(key, x, y):
    global K
    if key == b'w':
        K.w = 1
    if key == b's':
        K.s = 1
    if key == b'a':
        K.a = 1
    if key == b'd':
        K.d = 1
    if key == b'm':
        K.m = 1
    if key == b',':
        K.sr = 1
    if key == b'.':
        K.sl = 1

# Keyboard function for key release
def KeysUp(key, x, y):
    global K
    if key == b'w':
        K.w = 0
    if key == b's':
        K.s = 0
    if key == b'a':
        K.a = 0
    if key == b'd':
        K.d = 0
    if key == b'm':
        K.m = 0
    if key == b',':
        K.sr = 0
    if key == b'.':
        K.sl = 0
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from constants import *
from player.movement import movePlayer
from screen.drawing import *

# Structures
class Time:
    def __init__(self):
        self.fr1 = 0
        self.fr2 = 0

# Global variables
T = Time()


# Display function
def display():
    global T
    if T.fr1 - T.fr2 >= 50:
        clearBackground()
        movePlayer()
        draw3D()
        T.fr2 = T.fr1
        glutSwapBuffers()
        glutReshapeWindow(int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
    T.fr1 = glutGet(GLUT_ELAPSED_TIME)
    glutPostRedisplay()
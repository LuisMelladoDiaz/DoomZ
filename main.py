from cmath import pi
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from constants import *
import sys
from player.player import P
from screen.display import *
from player.movement import KeysDown, KeysUp
from map.mapParser import read_map

MAP = read_map(f'map/maps_data/map1')
MAP_LENGTH = len(MAP)

# Initialization function
def init():

    P.x = 70
    P.y = -110
    P.z = 20
    P.horizontal_angle = 0
    P.vertical_angle = 0


# Main function
def main():
    MAP = read_map(f'map/maps_data/map1')
    map_editor_parser(MAP)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))
    glutInitWindowSize(int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
    glutCreateWindow(b"")
    glPointSize(PIXEL_SCALE)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(KeysDown)
    glutKeyboardUpFunc(KeysUp)
    glutMainLoop()

if __name__ == "__main__":
    main()
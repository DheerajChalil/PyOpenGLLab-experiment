import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
w,h = 500,500

def init2D(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (-500.0, 500.0, -500.0, 500.0)

def horizontal():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POINTS)
    for x1 in range(x2):
        glVertex2i(x1,y)    
    glEnd()
    glFlush()

def vertical():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for y1 in range(y2):
        glVertex2i(x,y1)    
    glEnd()
    glFlush()

def diagonal():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    for d1 in range(d2):
        glVertex2i(d1,d1)    
    glEnd()
    glFlush()

option = input('Enter 1 for horizontal line and 2 for verticle line and 3 for diagonal line : ')
if option == '1':
    print('selected for horizontal line')
    x1 = int(input('Enter x1 value : '))
    x2 = int(input('Enter x2 value : '))
    y = int(input('Enter y value : '))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b'Horizontal line')
    init2D(0.0,0.0,0.0)
    glutDisplayFunc(horizontal)
    glutMainLoop()

if option == '2':
    print('selected for verticle line')
    x = int(input('Enter x value : '))
    y1 = int(input('Enter y1 value : '))
    y2 = int(input('Enter y2 value : '))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b'Vertical line')
    init2D(0.0,0.0,0.0)
    glutDisplayFunc(vertical)
    glutMainLoop()

if option == '3':
    print('selected for diagonal line line')
    d1 = int(input('Enter value1 : '))
    d2 = int(input('Enter value2 : '))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b'Diagonal line')
    init2D(0.0,0.0,0.0)
    glutDisplayFunc(diagonal)
    glutMainLoop()

else:
    print('Invalid option')
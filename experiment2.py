  
import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
w,h = 500,500

def init2D(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0, 500.0, 0, 500.0)

def ROUND(a):
    return int(a + 0.5)

def drawDDA(x1,y1,x2,y2):
    x,y = x1,y1
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    for i in range(length):
        x += dx
        y += dy
        X[i] = ROUND(x)
        Y[i] = ROUND(y)

def plotDDA():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for i in range(length):
        glVertex2i(X[i],Y[i])    
    glEnd()
    glFlush()
        

a,b,c,d = [int(a) for a in input("Enter x1 y1 and x2 y2 value: ").split()]
global length 
length = (c-a) if (c-a) > (d-b) else (d-b)
X = [0] * length
Y = [0] * length
drawDDA(a,b,c,d)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(w, h)
glutInitWindowPosition(100,100)
glutCreateWindow(b'Lne using DDA')
init2D(0.0,0.0,0.0)
glutDisplayFunc(plotDDA)
glutMainLoop()


        

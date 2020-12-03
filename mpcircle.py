import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
w,h = 500,500

global x_centre,y_centre,r

def init2D():
    glClearColor(0.0,0.0,0.0,1.)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D(-50,100.0,-50.0,100.0)

def ROUND(a):
    	return int(a+0.4)

def setPixel(xcoordinate,ycoordinate):
    
	glColor3f(1.0,0.0,1.0) 
	glPointSize(5.0)
	glBegin(GL_LINES)
	glVertex2f(-500,0)
	glVertex2f(500,0)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(0,-500)
	glVertex2f(0,500)
	glEnd() 
	glColor3f(0.2,0.0,1.5)
	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()


def midPointCircleDraw(x_centre, y_centre, r): 
    x = r 
    y = 0
      
    # Printing the initial point the  
    # axes after translation  
    print("(", x + x_centre, ", ",  
               y + y_centre, ")",  
               sep = "", end = "")  
      
    # When radius is zero only a single  
    # point be printed  
    if (r > 0) : 
      
        print("(", x + x_centre, ", ", 
                  -y + y_centre, ")",  
                  sep = "", end = "")  
        print("(", y + x_centre, ", ",  
                   x + y_centre, ")", 
                   sep = "", end = "")  
        print("(", -y + x_centre, ", ",  
                    x + y_centre, ")", sep = "")  
      
    # Initialising the value of P  
    P = 1 - r  
  
    while x > y: 
      
        y += 1
          
        # Mid-point inside or on the perimeter 
        if P <= 0:  
            P = P + 2 * y + 1
              
        # Mid-point outside the perimeter  
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1
          
        # All the perimeter points have  
        # already been printed  
        if (x < y): 
            break
          
        # Printing the generated point its reflection  
        # in the other octants after translation  
        print("(", x + x_centre, ", ", y + y_centre, 
                            ")", sep = "", end = "")  
        print("(", -x + x_centre, ", ", y + y_centre,  
                             ")", sep = "", end = "")  
        print("(", x + x_centre, ", ", -y + y_centre, 
                             ")", sep = "", end = "")  
        print("(", -x + x_centre, ", ", -y + y_centre, 
                                        ")", sep = "")  
          
        # If the generated point on the line x = y then  
        # the perimeter points have already been printed  
        if x != y: 
          
            print("(", y + x_centre, ", ", x + y_centre,  
                                ")", sep = "", end = "")  
            print("(", -y + x_centre, ", ", x + y_centre, 
                                 ")", sep = "", end = "")  
            print("(", y + x_centre, ", ", -x + y_centre, 
                                 ")", sep = "", end = "")  
            print("(", -y + x_centre, ", ", -x + y_centre,  
                                            ")", sep = "") 

def outputDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    midPointCircleDraw(x_centre, y_centre, r)                        

print("*WELCOME TO circle DRAWING using Mid Point's Algorithm*")
x_centre=int(input('x1 coordinate:'))
y_centre=int(input('y1 coordinate:'))
r=int(input('Radius: '))
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(w, h)
glutInitWindowPosition(50,50)
glutCreateWindow(b'Circle using Mid-Point_Algo')
init2D()
glutDisplayFunc(outputDisplay)
glutMainLoop()
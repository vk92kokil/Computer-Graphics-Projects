##################################
# Name - Vikramaditya Kokil
# ID   - 201101103
##################################
import sys
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width = 600
height = 600
r = 1
global year, day,cent
year = 0.0
day = 0.0
cent = 0.0
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = [100.0]
light_position = [0.0, 0.0, 0.0, 1.0]
white_light = [1.0, 1.0, 1.0, 1.0]
lmodel_ambient = [0.1, 0.1, 0.1, 1.0]
def sphere():
    global day
    glPushMatrix()
    glTranslate(-1,-1.5,0)
    glScalef(1,0.1,1)
    glColor3f(0.1,0.1,0)
    glutSolidCube(10)
    glPopMatrix()
    glPushMatrix()
    glRotatef(day,1,1,1)
    glColor3f(1,1,1)
    glLineWidth(2)
    for phi in range(0,181,5):
        glBegin(GL_LINE_STRIP)
        for theta in range(0,365,5):
            
            x = r*cos(theta * pi/180) * sin(phi*pi/180)
            y = r*sin(theta * pi/180) * sin(phi*pi/180)
            z = r*cos(phi * pi/180)
            glVertex3f(x,y,z)
        glEnd()
		
    for theta in range(0,361,5):
        glBegin(GL_LINE_STRIP)
        for phi in range(0,185,5):
            
            x = r*cos(theta * pi/180) * sin(phi*pi/180)
            y = r*sin(theta * pi/180) * sin(phi*pi/180)
            z = r*cos(phi * pi/180)
            glVertex3f(x,y,z)
        glEnd()
    glPopMatrix()
    glutSwapBuffers()
    glFlush()
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    sphere()
def keyboard(key, x, y):
   global year, day
   if key == chr(27): sys.exit(0)
   elif key == 'R': 
    day = (day + 10) % 360
    glutPostRedisplay()
   elif key == 'r': 
    day = (day - 10) % 360
    glutPostRedisplay()
   elif key == 'c': 
    glRotatef(5,0,1,0)
    glutPostRedisplay()
   elif key == 'C': 
    glRotatef(5,0,1,0)
    glutPostRedisplay()
   
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Sphere with Lines")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, 1, 1.0, 20.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef (0.0, 0.0, 0.0)
    gluLookAt(0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
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
########
size = 3.5 #####cube size
val = 1 # cut edge length

turn = 0
flag = 0
vertex1 = [0,val,0]
vertex2 = [val,0,0]
vertex3 = [size-val,0,0]
vertex4 = [size,val,0]
vertex5 = [size,size-val,0]
vertex6 = [size-val,size,0]
vertex7 = [val,size,0]
vertex8 = [0,size-val,0]
vertex = [vertex1,vertex2,vertex3,vertex4,vertex5,vertex6,vertex7,vertex8]

mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = [100.0]
light_position = [-size/2,-size/2, size/2, 1.0]
white_light = [1.0, 1.0, 1.0, 1.0]
lmodel_ambient = [0.1, 0.1, 0.1, 1.0]

def cube():
	
	glPushMatrix()
	glTranslatef(-size/2,-size/2,-size/2)
	glPushMatrix()
	drawtriangle()
	glColor3f(1,0,0)
	drawface()
	glPopMatrix()
	
	glPushMatrix()
	glRotatef(90,1,0,0)
	glColor3f(0,1,0)
	drawface()
	glPopMatrix()
	
	glPushMatrix()
	glTranslatef(0,size,0)
	glRotatef(90,1,0,0)
	glColor3f(0,1,0)
	drawface()
	glPopMatrix()
	
	glPushMatrix()
	glTranslatef(0,0,size)
	glRotatef(90,0,1,0)
	glColor3f(0,0,1)
	drawface()
	glPopMatrix()
	
	glPushMatrix()
	glTranslatef(size,0,size)
	glRotatef(90,0,1,0)
	glColor3f(0,0,1)
	drawface()
	glPopMatrix()
	
	glPushMatrix()
	glTranslatef(0,0,size)
	glColor3f(1,0,0)
	drawface()
	glPopMatrix()
	glPopMatrix()
	
	glutSwapBuffers()
	glFlush()
def drawface():
	glPushMatrix()
	glBegin(GL_POLYGON)
	
	glVertex3f(0,val,0)
	glVertex3f(val,0,0)

	glVertex3f(size-val,0,0)
	glVertex3f(size,val,0)
	
	glVertex3f(size,size-val,0)
	glVertex3f(size-val,size,0)
	
	glVertex3f(val,size,0)
	glVertex3f(0,size-val,0)
	
	glEnd()

	glPopMatrix()
def drawtriangle():
	glPushMatrix()
	
	glColor3f(1,1,1)
	glBegin(GL_TRIANGLES)
	glVertex3f(0,val,0)
	glVertex3f(val,0,0)
	glVertex3f(0,0,val)
	glEnd()
	

	glBegin(GL_TRIANGLES)
	glVertex3f(size-val,0,0)
	glVertex3f(size,val,0)
	glVertex3f(size,0,val)
	glEnd()
	
	
	glBegin(GL_TRIANGLES)
	glVertex3f(size,size-val,0)
	glVertex3f(size-val,size,0)
	glVertex3f(size,size,val)
	glEnd()
	
	glBegin(GL_TRIANGLES)
	glVertex3f(val,size,0)
	glVertex3f(0,size-val,0)
	glVertex3f(0,size,val)
	glEnd()	
	###
	
	glBegin(GL_TRIANGLES)
	glVertex3f(0,val,size)
	glVertex3f(val,0,size)
	glVertex3f(0,0,size-val)
	glEnd()	
	
	
	glBegin(GL_TRIANGLES)
	glVertex3f(size-val,0,size)
	glVertex3f(size,val,size)
	glVertex3f(size,0,size-val)
	glEnd()	


	glBegin(GL_TRIANGLES)
	glVertex3f(size,size-val,size)
	glVertex3f(size-val,size,size)
	glVertex3f(size,size,size-val)
	glEnd()	
	

	glBegin(GL_TRIANGLES)
	glVertex3f(val,size,size)
	glVertex3f(0,size-val,size)
	glVertex3f(0,size,size-val)
	glEnd()	
	
	glPopMatrix()
def spin(x):
	global turn,flag
	turn+=1
	if(turn < 50):
		glRotatef(10,1,0,0)
		glutPostRedisplay()
	elif(turn < 100):
		glRotatef(10,0,1,0)
		glutPostRedisplay()
	else:
		if(turn >= 150):
			turn = 0
		glRotatef(10,0,0,1)
		glutPostRedisplay()
	if(flag == 0):
		glutTimerFunc(50,spin,1)
def display():
    glClear( GL_COLOR_BUFFER_BIT)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    cube()
def reshape (w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(60, w / h, 1.0, 20.0)
   glMatrixMode (GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt(0.0, 8.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard(key, x, y):
  global flag
  if(flag ==1):
   if key == chr(27): sys.exit(0)
   elif key == 'x': glRotatef(5,1,0,0)
   elif key == 'X': glRotatef(5,1,0,0)
   elif key == 'y': glRotatef(5,0,0,1)
   elif key == 'Y': glRotatef(5,0,0,1)
   elif key == 'z': glRotatef(5,0,1,0)
   elif key == 'Z': glRotatef(5,0,1,0)
  elif key == 's': 
    flag = 1-flag
    spin(1)
  elif key == 'S': 
    flag = 1-flag
    spin(1)
  glutPostRedisplay()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("PolyHydra")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(100,spin,0)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()



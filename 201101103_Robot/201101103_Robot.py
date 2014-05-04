##################################
# Name - Vikramaditya Kokil
# ID   - 201101103
##################################
if __name__ == '__build__':
	raise Exception

from sys import exit
from math import *

global shoulder, elbow
shoulder = 0.0
elbow = 0.0
head = -60.0
left_arm = 180.0
right_arm = 180.0 
left_hand = 0.0
right_hand = 0.0
left_leg = 180.0
left_foot = 0.0
right_leg = 180.0
right_foot = 0.0

right_arm_var = -5
left_arm_var = -5
right_hand_var = 5
left_hand_var = 5
right_leg_var = -5
left_leg_var = -5
left_foot_var = 5
right_foot_var = 5
up = 5.0 
down = -5.0
r_rot = 0.0
l_rot = 0.0
cam = 0.0
flag = 0
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = [100.0]
light_position = [0.0, 1.0, 1.0, 0.0]
white_light = [1.0, 1.0, 1.0, 1.0]
lmodel_ambient = [0.1, 0.1, 0.1, 1.0]
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except: print '''ERROR: PyOpenGL not installed properly.'''

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)
def body():
	
	global head,left_arm,right_arm,left_hand,right_hand,left_leg,left_foot,right_leg,right_foot
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glClear (GL_COLOR_BUFFER_BIT)
	
	glShadeModel(GL_SMOOTH)
	#glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	#glLightfv(GL_LIGHT1, GL_POSITION, [1,1,5,1])
	glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
	glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
	#glLightfv(GL_LIGHT1, GL_SPECULAR, [1,1,1,1])
	#glLightfv(GL_LIGHT1, GL_DIFFUSE, white_light)
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
	glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	#glEnable(GL_LIGHT1)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_COLOR_MATERIAL)
	quadratic0 = gluNewQuadric();
	quadratic1 = gluNewQuadric();
	quadratic2 = gluNewQuadric();
	
	glColor3f (1.0, 1.0, 1.0)
	
	glPushMatrix()
	glTranslatef(-5,-6,0)
	glScalef(20,0.5,10)
	glColor3f (0, 0.6, 0.2)
	glutSolidCube(2);
	glPopMatrix()
	#body
	glPushMatrix();
	
	glTranslate(0,0.7,0)
	glRotatef (head, 0.0, 1.0, 0.0);# for testing
	#head
	glPushMatrix();
	#glRotatef (head, 0.0, 1.0, 0.0);
	glScalef(1,1.2,0.8)
	glTranslate(0,3.0,0)
	glColor3f (1.0, 1.0, 0.0)
	glutSolidSphere(0.8,20,16)
	glColor3f (1.0, 1.0, 1.0)
	#eyes
	glPushMatrix();
	glColor3f (1.0, 0.0, 0.0)
	glTranslate(-0.4,0.2,0.6)
	glutSolidSphere(0.12,20,16)
	glTranslate(0.9,0,0)
	glutSolidSphere(0.1,20,16)
	glPopMatrix(); #eyes pop
	#mouth
	glPushMatrix();
	glScalef(0.2,0.05,0.2)
	glTranslate(0.0,-5,3.3)
	glColor3f (0.0, 0.0, 0.0)
	glutSolidCube(1.8)
	glTranslate(0.0,13,0)
	glScalef(5,20,8)
	glRotatef(90,1,0,0)
	glColor3f (0.0, 1.0, 0.0)
	gluCylinder(quadratic0,0,0.2,0.4,32,32);
	glPopMatrix();#mouth pop
	glPopMatrix();#head pop
	
	#neck
	glPushMatrix()
	glTranslate(0,2.7,0)
	glRotatef (90.0,1.0, 0.0, 0.0);
	glColor3f (1.0, 1.0, 1.0)
	gluCylinder(quadratic0,0.5,0.5,0.8,32,32);
	glPopMatrix()
	
	#body1
	glColor3f (1.0, 1.0, 1.0)
	
	glPushMatrix();
	glTranslate(0.0,2,0.0)	
	glScalef(5.0,5.0,3.0)
	glRotatef(90.0, 1.0, 0.0, 0.0);
	glColor3f (0.8, 0.8, 0.8)
	gluCylinder(quadratic0,0.2,0.2,0.8,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix(); #body1 pop
	
	
	glPushMatrix()##left side
	glTranslate(-1.2,1.8,0.0)
	glRotatef (left_arm, 1.0, 0.0, 0.0);
	
	glPushMatrix();#left arm
	glColor3f (1.0, 0.0, 0.0)
	glutSolidSphere(0.3,20,16)
	glColor3f (1.0, 1.0, 1.0)
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic1,0.3,0.25,2.0,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix();#left arm pop
	
	glTranslate(0,2,0.0)
	glRotatef (left_hand, 1.0, 0.0, 0.0);
	
	glPushMatrix();#left hand
	glColor3f (0.0, 1.0, 0.0)
	glutSolidSphere(0.25,20,16)
	glColor3f (1.0, 1.0, 1.0)
	
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic2,0.25,0.15,1.5,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix()#left hand pop
	
	glPopMatrix()##left side pop
	
	glPushMatrix()##right side
	glTranslate(1.2,1.8,0.0)
	glRotatef (right_arm, 1.0, 0.0, 0.0);
	glPushMatrix();#right arms
	glColor3f (1.0, 0.0, 0.0)
	glutSolidSphere(0.3,20,16)
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic2,0.3,0.25,2.0,32,32);
	glPopMatrix();#right arm pop
	
	glTranslate(0,2,0.0)
	glRotatef (right_hand, 1.0, 0.0, 0.0);
	
	glPushMatrix();#right hand push
	glColor3f (0.0, 1.0, 0.0)
	glutSolidSphere(0.25,20,16)
	
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic2,0.25,0.15,1.5,32,32);
	glPopMatrix() #right hand pop
	glPopMatrix() #right side pop
	################################
	
	glPushMatrix()##left side
	glTranslate(-0.5,-2,0.0)
	glRotatef (left_leg, 1.0, 0.0, 0.0);
	glPushMatrix();#left leg
	glColor3f (1.0, 0.0, 0.0)
	glutSolidSphere(0.4,20,16)
	glColor3f (1.0, 1.0, 1.0)
	
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic1,0.4,0.3,2.0,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix();#left leg pop
	
	glTranslate(0,2,0.0)
	glRotatef (left_foot, 1.0, 0.0, 0.0);
	
	glPushMatrix();#left foot
	glColor3f (0.0, 1.0, 0.0)
	glutSolidSphere(0.3,20,16)
	glColor3f (1.0, 1.0, 1.0)
	#glTranslatef(0.0,1.5,0.0)
	#glScalef(0.3,3,1.0);
	#glutWireCube(1.0);
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic2,0.3,0.25,2.0,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix()#left foot pop
	glTranslate(0,2.2,0)
	glScalef(0.5,0.2,1.0)
	glColor3f(0,0,1)
	glutSolidCube(1)
	glPopMatrix()##left side pop
	
	glPushMatrix()##right side push
	glTranslate(0.5,-2,0.0)
	glRotatef (right_leg, 1.0, 0.0, 0.0);
	glPushMatrix();#right leg
	glColor3f (1.0, 0.0, 0.0)
	glutSolidSphere(0.4,20,16)
	glColor3f (1.0, 1.0, 1.0)
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic2,0.4,0.3,2.0,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix();#right leg pop
	
	glTranslate(0,2,0.0)
	glRotatef (right_foot, 1.0, 0.0, 0.0);
	
	glPushMatrix();#right foot push
	glColor3f (0.0, 1.0, 0.0)
	glutSolidSphere(0.3,20,16)
	glColor3f (1.0, 1.0, 1.0)
	
	glRotatef(-90,1,0,0)
	glColor3f (0.0, 0.0, 1.0)
	gluCylinder(quadratic2,0.3,0.25,2.0,32,32);
	glColor3f (1.0, 1.0, 1.0)
	glPopMatrix() #right foot pop
	glTranslate(0,2.2,0)
	glScalef(0.5,0.2,1.0)
	glColor3f(0,0,1)
	glutSolidCube(1)
	glPopMatrix() #right side pop
	
	glPopMatrix();#body pop
	glutSwapBuffers();
	
def reshape (w, h):

        glViewport (0, 0, w, h) 

        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, w / h, 1.0, 20.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef (0.0, 0.0, -5.0)
        
        gluLookAt(-1.0, 2.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
           

def keyboard(key, x, y):
  global shoulder, elbow,head,left_arm,right_arm,left_hand,right_hand,up,down,r_rot,l_rot
  global left_leg,left_foot,right_leg,right_foot,flag
  global right_arm_var,left_arm_var,right_hand_var,left_hand_var,right_leg_var,left_leg_var,left_foot_var,right_foot_var

  if(flag == 1):
   if key == chr(27): sys.exit(0)
   elif key == 't':
           head = (head+5) % 360
           glutPostRedisplay()
   elif key == 'T':
           head = (head+5) % 360
           glutPostRedisplay()
   elif key == 'g':
           if(left_arm == 180):
			left_arm_var = -5
           elif(left_arm == 0):
			left_arm_var = 5
           left_arm += left_arm_var
           glutPostRedisplay()
   elif key == 'G':
           if(left_arm == 180):
			left_arm_var = -5
           elif(left_arm == 0):
			left_arm_var = 5
           left_arm += left_arm_var
           glutPostRedisplay()
   elif key == 'H':
           if(right_arm == 180):
			right_arm_var = -5
           elif(right_arm == 0):
			right_arm_var = 5
           right_arm += right_arm_var
           glutPostRedisplay()
   elif key == 'h':
           if(right_arm == 180):
			right_arm_var = -5
           elif(right_arm == 0):
			right_arm_var = 5
           right_arm += right_arm_var
           glutPostRedisplay()
   elif key == 'j':
           if(right_hand == -180):
			right_hand_var = 5
           elif(right_hand == 0):
			right_hand_var = -5
           right_hand = right_hand+right_hand_var
           glutPostRedisplay()
   elif key == 'J':
           if(right_hand == -180):
			right_hand_var = 5
           elif(right_hand == 0):
			right_hand_var = -5
           right_hand = right_hand+right_hand_var
           glutPostRedisplay()
   elif key == 'f':
           if(left_hand == -180):
			left_hand_var = 5
           elif(left_hand == 0):
			left_hand_var = -5
           left_hand += left_hand_var
           glutPostRedisplay()
   elif key == 'F':
           if(left_hand == -180):
			left_hand_var = 5
           elif(left_hand == 0):
			left_hand_var = -5
           left_hand += left_hand_var
           glutPostRedisplay()
   elif key == 'b':
           if(left_leg == 180):
			left_leg_var = -5
           elif(left_leg == 90):
			left_leg_var = 5
           left_leg += left_leg_var
           glutPostRedisplay()
		   
   elif key == 'B':
           if(left_leg == 180):
			left_leg_var = -5
           elif(left_leg == 90):
			left_leg_var = 5
           left_leg += left_leg_var
           glutPostRedisplay()
   elif key == 'n':
           if(right_leg == 180):
			right_leg_var = -5
           elif(right_leg == 90):
			right_leg_var = 5
           right_leg += right_leg_var
           glutPostRedisplay()
   elif key == 'N':
           if(right_leg == 180):
			right_leg_var = -5
           elif(right_leg == 90):
			right_leg_var = 5
           right_leg += right_leg_var
           glutPostRedisplay()
   elif key == 'm':
           if(right_foot == 180):
			right_foot_var = -5
           elif(right_foot == 0):
			right_foot_var = 5
           
           right_foot += right_foot_var
           glutPostRedisplay()
		   
   elif key == 'M':
           if(right_foot == 180):
			right_foot_var = -5
           elif(right_foot == 0):
			right_foot_var = 5
           right_foot += right_foot_var
           glutPostRedisplay()
   elif key == 'v':
           if(left_foot == 180):
			left_foot_var = -5
           elif(left_foot == 0):
			left_foot_var = 5
           left_foot += left_foot_var
           glutPostRedisplay()
   elif key == 'V':
           if(left_foot == 180):
			left_foot_var = -5
           elif(left_foot == 0):
			left_foot_var = 5
           left_foot += left_foot_var
           glutPostRedisplay()
  if key == 's':
           flag = 1-flag;
           move(1)
           glutPostRedisplay()
  elif key == 'S':
           flag = 1-flag;
           move(1)
           glutPostRedisplay()

def SpecialKeys(key,x,y):
	if key == GLUT_KEY_LEFT:
           glRotatef(-5, 0, 1, 0);
           glutPostRedisplay()
	elif key == GLUT_KEY_RIGHT:
           glRotatef(5, 0, 1, 0);
           glutPostRedisplay()

def move(x):
           global shoulder, elbow,head,left_arm,right_arm,left_hand,right_hand,up,down,r_rot,l_rot,flag
           global left_leg,left_foot,right_leg,right_foot
           global right_arm_var,left_arm_var,right_hand_var,left_hand_var,right_leg_var,left_leg_var,left_foot_var,right_foot_var
           if(not (right_leg>=120 and right_leg<=220)):
		    right_leg = 180
           #if(not (left_leg>=120 and left_leg<=220)):
		    #left_leg = 180
           if(not (left_arm<=220 and left_arm >=0)):
		    left_arm = 180
           if(not (right_arm<=220 and right_arm>=0)):
		    right_arm = 180
           
           if(right_leg == 120):
			tmp = up
			up = down
			down = tmp
           elif(right_leg == 220):
			tmp = up
			up = down
			down = tmp
           if(right_foot == 40):
            r_rot = -5
           elif(right_foot == 0):
            r_rot = 5
           if(left_foot == 40):
            l_rot = -5
           elif(left_foot == 0):
            l_rot = 5
		   
           left_leg = (left_leg + up)
           right_leg = (right_leg+down)
           
           right_foot = right_foot + r_rot
           left_foot = left_foot + l_rot
           left_arm = left_arm + down
           right_arm = right_arm + up
           left_hand = -90
           right_hand = -90
           head = head + 1
           if(flag == 0):
            glutTimerFunc(100,move,1)
           glutPostRedisplay()
glutInit(sys.argv)
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize (600, 600)	
glutInitWindowPosition (100, 100)
glutCreateWindow ('Humanoid')
init ()
glutDisplayFunc(body)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutSpecialFunc(SpecialKeys);
glutTimerFunc(100,move,0)
glutMainLoop()

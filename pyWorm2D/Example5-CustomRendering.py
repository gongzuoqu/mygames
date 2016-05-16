from worm2d import Engine, Viewport
import pygame
from OpenGL.GL import *

#A function for drawing a triangle.
def DrawTriangle(x,y,w,h,r,g,b):
    #you can use any opengl call, to do anything you want.
    glDisable(GL_TEXTURE_2D)
    glPushMatrix();
    glTranslatef( x, y, 0 );
    glColor4f(r,g,b,1)
    glScalef(w,h,1);
        
    glBegin(GL_TRIANGLES)
    glVertex3f(0,-1,0)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    glEnd()

    glPopMatrix();
    glEnable(GL_TEXTURE_2D)


def main():
    
    engine = Engine(640,480, 32, False, "Worm2D")
    view = Viewport(0,0,1,1, 100.0, 75.0)    

    img_ship = engine.LoadImage("example_data/ship.png")
    
    while engine.IsRunning():

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        engine.PreRender(0.2,0.2,0.2)                
        engine.SetView(view, 0.0,0.0,1.0)


        #draw the ship normaly
        engine.DrawImage(img_ship, 0,0, 10, 10, 1.0, 0)

        #We can do any openGL call we want!
        #For this example, lets change the blending for this image.

        glBlendFunc(GL_ONE, GL_ONE)
        
        engine.DrawImage(img_ship, 10,0, 20, 20, 1.0, 0)

        #Now change it back when we are done.
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        #Now, draw the Triangle
        DrawTriangle(-20,0,10,10, 0,0,1)
        
        
        engine.PostRender()



main()

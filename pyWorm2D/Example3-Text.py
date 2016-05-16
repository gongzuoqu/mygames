from worm2d import Engine, Viewport
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import OpenGL


#NOTE: After making these examples, I found that DrawString is much,
#much slower than DrawText. This is becuase DrawString renders the text
#as its called, and a text object only re-renders when changed.
#Moral: use Text object most of the time. If you are displaying something
#that changes very frequently (like, every frame), DrawString is fine.
#Also, DrawSring is handy for debug porposes, when you want to quickly
#see a variable, or something like that. 

def main():
    
    engine = Engine(640,480, 32, False, "Worm2D")
    view = Viewport(0,0,1,1, 100.0, 75.0)

    #First, we load our font from pygame
    font = pygame.font.SysFont("Arial", 60)

    #Create a new text object
    txt = engine.Text("CHANGE-ME", font)
    
    #Set the string displayed by the object
    #NOTE: you could leave the text as "CHANGE-ME", if you wanted
    engine.SetTextString(txt, "This is a text object", font)
    
    while engine.IsRunning():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
        engine.PreRender(0.2, 0.2, 0.2)
        engine.SetView(view, 0.0,0.0,1.0)

        #This call draws a string without a text object
        engine.DrawString("This Text uses the default font", 0,-32,5,5,r = 1.0, g = 1.0, b = 0)
        #This call draws a string without a text object, and uses a font
        engine.DrawString("This Text uses a loaded font", 0,-25,5,5, r = 0.0, g = 1.0, b = 0, font=font)
        #this is our text object from before
        engine.DrawText(txt, 0,-16, 5,5)
        
        
        engine.PostRender()



main()

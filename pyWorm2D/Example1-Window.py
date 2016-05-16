#import the engine
from worm2d import Engine, Viewport

#import pygame for pygame.event.get()
import pygame


def main():
    #this creates a 640x480 32bpp not fullscreen window with "Worm2D" for a caption
    engine = Engine(640,480, 32, False, "Worm2D")

    #our viewport. It tells the engine how much of the window to use
    #(in this case, all of it), and then how big it is to openGL.
    #so, this viewport takes up the whole screen, and is 100.0 openGL units
    #wide and 75.0 opengl units tall.
    view = Viewport(0,0,1,1, 100.0, 75.0)    

    #eng.IsRunning() returns false, the window has been closed.
    while engine.IsRunning():

        #use pygame to check events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #quit if escape is pressed
                    return

        #This clears the screen, sets background color, and so on.
        engine.PreRender(0.2, 0.2, 0.2)

        #This gives the viewport to OpenGL.
        #Also, you can set camera position, and zoom
        #           viewport,camx,camy,zoom.
        engine.SetView(view, 0.0, 0.0, 1.0)

        #draw your stuff in here

        #called after rendering EVERYTHING
        engine.PostRender()



main()

from worm2d import Engine, Viewport
import pygame


def DrawScene(image, engine):
    #Now, I could do this in the mainloop, But since I would have
    #the same code in to places, a function easier.
    
    engine.DrawImage(image, 0,-10, 10, 10, 1.0, 0)
    engine.DrawImage(image, 10,0, 10, 10, 1.0, 0)
    engine.DrawImage(image, -10,0, 10, 10, 1.0, 0)
    engine.DrawImage(image, 0,10, 10, 10, 1.0, 0)

def main():
    
    engine = Engine(640,480, 32, False, "Worm2D")

    #create the different viewports.
    #the first two args are postion on the screen
    #(0,0 being the top left, 1,1 being the bottom right)
    # The second two are the width and height (1,1 being all the screen,
    #0.5,0.5 being a quarter of it.
    #the last two are how big it is in opengl.
    top = Viewport(0,0,1,0.5, 100.0, 37.5)
    bottom = Viewport(0,0.5,1,0.5, 100.0, 37.5)
    hud = Viewport(0,0,1,1, 100.0, 75.0)

    #our ship image
    img_ship = engine.LoadImage("example_data/ship.png")

    #camera position
    camx, camy = 0.0,0.0
    
    while engine.IsRunning():

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                #move camera
                if event.key == pygame.K_UP:
                    camy += 2
                if event.key == pygame.K_DOWN:
                    camy -= 2
                if event.key == pygame.K_LEFT:
                    camx += 2
                if event.key == pygame.K_RIGHT:
                    camx -= 2
                    
        engine.PreRender(0.2,0.2,0.2)
        
        #render the scene from the top
        engine.SetView(top, 0.0,0.0,1.0)

        DrawScene(img_ship,engine)

        #Render the scene again, from another viewport
        #Notice I'm using (camx,camy) in here.
        #This viewport will have the movable camera
        engine.SetView(bottom, camx,camy,1.0)

        DrawScene(img_ship,engine)

        #Now Draw the HUD
        engine.SetView(hud, 0,0,1.0)
        #Draw a black line to divide the two screens
        engine.DrawQuad(0,0,100, 0.2,1,0,0,0,0)
        
        #And some text
        #NOTE: Becuase this string were drawing NEVER CHANGES,
        #This is a fine example of a place where I should use a Text
        #object. I'm leaving it as an example of what NOT to do. Be warned.
        engine.DrawString("This is text in the hud viewport", 0,0,5,5,0.5)
        
        #NOTICE!! this is not called for every PreRender, but after
        #everything is rendered
        engine.PostRender()



main()

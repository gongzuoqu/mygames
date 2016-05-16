from worm2d import Engine, Viewport

import pygame


def main():
    engine = Engine(640,480, 32, False, "Worm2D")

    view = Viewport(0,0,1,1, 100.0, 75.0)

    img_ship = engine.LoadImage("example_data/ship.png")
    img_bg = engine.LoadImage("example_data/background.png")

    Z = 0.5

    #a few text objects for later
    txt_desc = engine.Text("Use the up/down keys to raise/lower the ship",None)
    txt_one = engine.Text("Depth = 0.0",None)
    txt_two = engine.Text("Depth = X",None)
    txt_three = engine.Text("Depth = 1.0",None)

    while engine.IsRunning():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_UP:
                    Z += 0.5
                if event.key == pygame.K_DOWN:
                    Z -= 0.5

        #get mouse pos from pygame
        mx,my = pygame.mouse.get_pos()

        #this converts screen coords to world coords.
        x,y = engine.MouseCoordsToWorldCoords(mx,my,0.0,0.0,1.0,view)

        engine.PreRender(0,0,0)

        #First, Draw the background, with no depth (since we don't want anything behind it).
        engine.SetView(view, 0.0,0.0,1.0, NoDepth = True)

        #with NoDepth set to true in PreRender, Z can be anything.
        engine.DrawImage(img_bg, 0,0, 100,100,1,0, z = 10)

        #Now, depth is on with a call to SetView, and the background won't effect this.
        engine.SetView(view, 0.0,0.0,1.0)

        #set the depth with z = depth, at the end.
        engine.DrawImage(img_ship, 0,-20, 20, 20, 1.0, 90, z = 0.0)

        #each ship is below (Y-axis) the other, so we can tell them apart.
        engine.DrawImage(img_ship, x,y, 20, 20, 1.0, 90, z = Z)

        engine.DrawImage(img_ship, 0,20, 20, 20, 1.0, 90, z = 1.0)

        #Once again, turn off depth. Now, the text will always be above everything else.
        engine.SetView(view, 0.0,0.0,1.0, NoDepth = True)

        #however far up the ship is, it never comes above these.
        engine.DrawText(txt_desc, 0,-35,3,3,r=1.0,g=1.0,b=1.0,z = 0)
        
        engine.DrawText(txt_one, 15,-20,2,2,r=0.0,g=1.0,b=0.0,z = 0)
        engine.DrawText(txt_three, 15,20,2,2,r=0.0,g=1.0,b=0.0,z = 0)
        engine.DrawString("Depth = "+ str(Z), x+15,y,2,2,r=0.0,g=1.0,b=0.0,z = 0)


        
        engine.PostRender()



main()

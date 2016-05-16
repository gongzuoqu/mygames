from worm2d import Engine, Viewport
import pygame
from pygame.locals import *

SPEED = 0.05

def main():
    
    engine = Engine(640,480, 32, False, "Worm2D")
    view = Viewport(0, 0, 1, 1, 100.0, 75.0)


    #loads an image
    img_ship = engine.LoadImage("example_data/ship.png")

    #loads anouther image.
    img_bg = engine.LoadImage("example_data/background.png")

    r = 0.0
    s = 1.0
    pos_x = 0
    pos_y = 0
    ticks = engine.GetTicks()
    
    while engine.IsRunning():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                # if event.key == pygame.K_UP:
                #     pos_y += 0.5
                # if event.key == pygame.K_DOWN:
                #    pos_y -= 0.5

        key = pygame.key.get_pressed()
        dist = SPEED # distance moved in 1 frame, try changing it to 5
        inc_x = 0
        inc_y = 0
        if key[pygame.K_DOWN]: # down key
            # pos_y += dist # move down
            inc_y = 0.1
        elif key[pygame.K_UP]: # up key
            # pos_y -= dist # move up
            inc_y = -0.1
        if key[pygame.K_RIGHT]: # right key
            # pos_x += dist # move right
            inc_x = 0.1
        elif key[pygame.K_LEFT]: # left key
            # pos_x -= dist # move left
            inc_x = -0.1

        #get the time between frames for framerate independence
        delta = engine.GetTicks() - ticks
        ticks = engine.GetTicks()

        #increment rotation and scale
        r += 0.1*delta
        if r > 360:
            r = 0

        s += 0.01*delta
        if s > 20:
            s = 0

        pos_x += inc_x*delta
        pos_y += inc_y*delta

        #start rendering
        engine.PreRender(0.2, 0.2, 0.2)
        engine.SetView(view, 0.0, 0.0, 1.0)

        #draw the non-power-of-two background
        engine.DrawImage(img_bg, 0,0, 100,100,1,0)

        #draws the image:   image  x y   w  h    a  rotation
        engine.DrawImage(img_ship, pos_x, pos_y, 10, 10, 1.0, 0)

        #draw first image again, rotated by r
        engine.DrawImage(img_ship, -20, 0, 10, 10, 1.0, r)

        #draw first image again, scaled by s
        engine.DrawImage(img_ship, 20, 0, s, s, 1.0, 0)
        
        
        engine.PostRender()



main()

from worm2d import Engine, Viewport
import pygame


def main():
    engine = Engine(640,480, 32, False, "Worm2D")

    view = Viewport(0,0,1,1, 100.0, 75.0)

    #Here is the only important call. It returns a list of Image objects
    #For this example, the image had 5 frames in two rows and 4 columns. Each frame was 256x256
    #                             path,      rows,columns, total, cell width, cell height
    images = engine.LoadSequence("example_data/Robot.png", 2,     4,     5,        256,      256)

    frame = 0.0

    #pretty much pygame.get_ticks()
    ticks = engine.GetTicks()

    
    while engine.IsRunning():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        #get the delta
        delta = engine.GetTicks() - ticks
        ticks = engine.GetTicks()

        #increments frame
        frame += 0.01*delta
        if frame >= len(images):
            frame = 0

        engine.PreRender(0.2, 0.2, 0.2)
        engine.SetView(view, 0.0,0.0,1.0)

        #renders an Image out of the list
        engine.DrawImage(images[int(frame)],0,0, 40,40, 1.0, 0)
        
        engine.PostRender()



main()


import pygame
from pygame.locals import *
import sys
import time
import pyganim
import sprites
import bomberman

pygame.init()

# define some constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# set up the window
WINDOWWIDTH = 960
WINDOWHEIGHT = 832
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('My Bomberman clone')

BGCOLOR = (100, 50, 50)

mainClock = pygame.time.Clock()

game = bomberman.Bomberman(WINDOWWIDTH, WINDOWHEIGHT)
game.loadResourcesAndCreateSprites()

while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get(): # event handling loop

        # handle ending the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        game.updateEvents(event)

    game.moveSprites()
    game.render(windowSurface)

    #
    # # make sure the player does move off the screen
    # if x < 0:
    #     x = 0
    # if x > WINDOWWIDTH - playerWidth:
    #     x = WINDOWWIDTH - playerWidth
    # if y < 0:
    #     y = 0
    # if y > WINDOWHEIGHT - playerHeight:
    #     y = WINDOWHEIGHT - playerHeight

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.
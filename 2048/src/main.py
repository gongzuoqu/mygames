import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

import images

DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_RIGHT = 3

SIZE_OF_BOARD = 4
CELL_WIDTH = 128
CELL_HEIGHT = 128
CELL_BORDER = 5
CELL_COLOR = (0, 255, 128)
BORDER_COLOR = (0, 0, 0)

SPEED = 5
X_SPEED = 10
Y_SPEED = 10

class MovingTile(object):  # represents the bird, not the game
    def __init__(self, width, height):
        """ The constructor of the class """
        self.image = images.create_player_image(width, height, (255, 0, 0))
        # the tile's position
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = SPEED # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))


def main():
    pygame.init()

    screen = pygame.display.set_mode((SIZE_OF_BOARD*CELL_WIDTH, SIZE_OF_BOARD*CELL_HEIGHT))
    background_image = images.create_background_image(SIZE_OF_BOARD, CELL_WIDTH, CELL_HEIGHT, CELL_COLOR, CELL_BORDER, BORDER_COLOR)
    tile = MovingTile(64, 64)

    clock = pygame.time.Clock()

    sprite_pos = Vector2(200, 150)
    sprite_speed = 300

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        tile.handle_keys() # handle the keys

        screen.blit(background_image, (0,0))
        tile.draw(screen)

        pygame.display.update()
        # time_passed = clock.tick(25)
        clock.tick(75)


if __name__ == "__main__":
    main()

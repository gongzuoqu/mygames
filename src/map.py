
import pygame

import events
from common import *

class MapSectorSprite(pygame.sprite.Sprite):
    def __init__(self, sector):
        pygame.sprite.Sprite.__init__(self)

        self.width = sector.getRect().width
        self.height = sector.getRect().height
        self.rect = sector.getRect()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))
        pygame.draw.rect(self.image, (0, 255, 128), (5, 5, self.width-10, self.height-10))
        self.sector = sector


class Map:
    """..."""

    STATE_PREPARING = 0
    STATE_BUILT = 1

    def __init__(self, evManager):
        self.evManager = evManager
        # self.evManager.RegisterListener( self )

        self.state = Map.STATE_PREPARING
        self.startSectorIndex=0
        self.sectors = []

    def Build(self):
        # will build default or child class map
        self.buildTheMap()

        self.state = Map.STATE_BUILT
        ev = events.MapBuiltEvent(self)
        self.evManager.Post(ev)

    def buildTheMap(self):
        for i in range(9):
            self.sectors.append(Sector(pygame.Rect()))

        self.sectors[3]._neighbors[DIRECTION_UP] = self.sectors[0]
        self.sectors[4]._neighbors[DIRECTION_UP] = self.sectors[1]
        self.sectors[5]._neighbors[DIRECTION_UP] = self.sectors[2]
        self.sectors[6]._neighbors[DIRECTION_UP] = self.sectors[3]
        self.sectors[7]._neighbors[DIRECTION_UP] = self.sectors[4]
        self.sectors[8]._neighbors[DIRECTION_UP] = self.sectors[5]

        self.sectors[0]._neighbors[DIRECTION_DOWN] = self.sectors[3]
        self.sectors[1]._neighbors[DIRECTION_DOWN] = self.sectors[4]
        self.sectors[2]._neighbors[DIRECTION_DOWN] = self.sectors[5]
        self.sectors[3]._neighbors[DIRECTION_DOWN] = self.sectors[6]
        self.sectors[4]._neighbors[DIRECTION_DOWN] = self.sectors[7]
        self.sectors[5]._neighbors[DIRECTION_DOWN] = self.sectors[8]

        self.sectors[1]._neighbors[DIRECTION_LEFT] = self.sectors[0]
        self.sectors[2]._neighbors[DIRECTION_LEFT] = self.sectors[1]
        self.sectors[4]._neighbors[DIRECTION_LEFT] = self.sectors[3]
        self.sectors[5]._neighbors[DIRECTION_LEFT] = self.sectors[4]
        self.sectors[7]._neighbors[DIRECTION_LEFT] = self.sectors[6]
        self.sectors[8]._neighbors[DIRECTION_LEFT] = self.sectors[7]

        self.sectors[0]._neighbors[DIRECTION_RIGHT] = self.sectors[1]
        self.sectors[1]._neighbors[DIRECTION_RIGHT] = self.sectors[2]
        self.sectors[3]._neighbors[DIRECTION_RIGHT] = self.sectors[4]
        self.sectors[4]._neighbors[DIRECTION_RIGHT] = self.sectors[5]
        self.sectors[6]._neighbors[DIRECTION_RIGHT] = self.sectors[7]
        self.sectors[7]._neighbors[DIRECTION_RIGHT] = self.sectors[8]

    def getSectors(self):
        return self.sectors

    def createSectorSprites(self, index):
        sector = self.sectors[index]
        rect = sector.getRect()
        msp = MapSectorSprite(sector)
        return msp


class Sector:
    """..."""

    def __init__(self, rect):

        self._neighbors = [0, 0, 0, 0]

        self._neighbors[DIRECTION_UP] = None
        self._neighbors[DIRECTION_DOWN] = None
        self._neighbors[DIRECTION_LEFT] = None
        self._neighbors[DIRECTION_RIGHT] = None

        self.rect = rect

    def MovePossible(self, direction):
        if self._neighbors[direction]:
            return 1

    def getDestinationSector(self, direction):
        return self._neighbors[direction]

    def getRect(self):
        return self.rect

    def getCenter(self):
        return self.rect.center

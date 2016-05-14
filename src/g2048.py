
import pygame
from common import *
import map


class Game2048Map(map.Map):

    def __init__(self, evManager, width, height):
        super().__init__(evManager)
        self.width = width
        self.height = height

    def buildTheMap(self):
        pos_x = 0
        pos_y = 0
        for i in range(4):
            pos_x = 0
            for j in range(4):
                self.sectors.append(map.Sector(pygame.Rect(pos_x, pos_y, self.width, self.height)))
                pos_x += self.width
            pos_y += self.height

        for i in list(range(4, 16)):
            self.sectors[i]._neighbors[DIRECTION_UP] = self.sectors[i-4]

        for i in list(range(0, 12)):
            self.sectors[i]._neighbors[DIRECTION_DOWN] = self.sectors[i+4]

        for i in list(range(1, 14, 4)):
            for j in list(range(i, i+3)):
                self.sectors[j]._neighbors[DIRECTION_LEFT] = self.sectors[j-1]

        for i in list(range(0, 14, 4)):
            for j in list(range(i, i+3)):
                self.sectors[j]._neighbors[DIRECTION_RIGHT] = self.sectors[j+1]



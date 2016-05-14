import pygame
from pygame.locals import *

from common import *

import events

class CharactorSprite(pygame.sprite.Sprite):
    def __init__(self, evManager, width, height, group=None):
        pygame.sprite.Sprite.__init__(self, group)

        self.evManager = evManager
        self.width = width
        self.height = height
        self.direction_x = 0
        self.direction_y = 0
        charactorSurf = pygame.Surface((self.width, self.height))
        charactorSurf = charactorSurf.convert_alpha()
        charactorSurf.fill((0, 0, 0, 0))  # make transparent
        pygame.draw.circle(charactorSurf, (255, 0, 0), (int(self.width/2), int(self.height/2)), int(self.width/2))
        self.image = charactorSurf
        self.rect = charactorSurf.get_rect()

        self.moveTo = None

    def _find_direction(self, move_to):
        if move_to[0] > self.rect.centerx:
            self.direction_x = X_SPEED
        elif move_to[0] < self.rect.centerx:
            self.direction_x = -X_SPEED
        else:
            self.direction_x = 0

        if move_to[1] > self.rect.centery:
            self.direction_y = Y_SPEED
        elif move_to[1] < self.rect.centery:
            self.direction_y = -Y_SPEED
        else:
            self.direction_y = 0

    def update(self):
        # print("call update char [%d]:[%d] to [%d]:[%d] with [%d]:[%d]" % self.rect.center, self.moveTo, self.direction_x, self.direction_y)
        print("sprite rect [%d]:[%d]" % self.rect.center)
        if self.moveTo:
            print("move to [%d]:[%d]" % self.moveTo)
            if self.rect.center == self.moveTo:
                self.rect.center = self.moveTo
                self.moveTo = None
                self.direction_x = 0
                self.direction_y = 0
                ev = events.CharactorAtDestination()
                self.evManager.Post(ev)
            else:
                print("direction [%d]:[%d]" % (self.direction_x, self.direction_y))
                self._find_direction(self.moveTo)
                org_x = self.rect.center[0]
                org_y = self.rect.center[1]
                new_x = org_x + self.direction_x
                new_y = org_y + self.direction_y
                if (self.direction_x > 0 and new_x > self.moveTo[0]) or (self.direction_x < 0 and new_x < self.moveTo[0]):
                        new_x = self.moveTo[0]
                if (self.direction_y > 0 and new_y > self.moveTo[1]) or (self.direction_y < 0 and new_y < self.moveTo[1]):
                        new_y = self.moveTo[1]
                self.rect.center = (new_x, new_y)
                print("move rect [%d]:[%d]" % self.rect.center)


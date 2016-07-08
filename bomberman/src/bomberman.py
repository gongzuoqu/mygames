from pygame.locals import *
import pygame
import sprites

WHITE = (255, 255, 255)


class Bomberman:
    def __init__(self, w_width, w_height):
        self.allSprites = []
        self.width = w_width
        self.height = w_height
        self._createInstruction()

    def loadResourcesAndCreateSprites(self):
        self.player = sprites.Player()
        self.player.loadRsc()
        self.bomb = sprites.Bomb()
        self.flame = sprites.Flame()

        # add the player as the first sprite
        self.allSprites.append(self.player)

    def updateEvents(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self._createANewBomb()

        for s in self.allSprites:
            s.processEvents(event)

    def moveSprites(self):
        for s in self.allSprites:
            r = s.update()
            if r is not True:
                if type(s) is sprites.Bomb:
                    self.allSprites.remove(s)
                    self._createNewFlames(s.getPos())

    def render(self, windowSurface):
        for s in self.allSprites:
            s.blit(windowSurface)

        windowSurface.blit(self.instructionSurf, self.instructionRect)


    def _createANewBomb(self):
        pos = self.player.getPos()
        b = self.bomb.createCopy()
        b.setPos(pos)
        self.allSprites.append(b)

    def _createNewFlames(self, pos):
        f = self.flame.createCopy()
        f.setPos(pos)
        self.allSprites.append(f)

    def _createInstruction(self):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.instructionSurf = self.font.render('Arrow keys to move. Hold shift to run.', True, WHITE)
        self.instructionRect = self.instructionSurf.get_rect()
        self.instructionRect.bottomleft = (10, self.height - 10)

#! /usr/bin/env python
'''
Example
'''

import pygame
from pygame.locals import *

from common import *
import events
import sprites
import player
import map
import inputs

class CPUSpinnerController:
    """..."""

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.keepGoing = 1

    def Run(self):
        while self.keepGoing:
            event = events.TickEvent()
            self.evManager.Post(event)

    def Notify(self, event):
        if isinstance(event, events.QuitEvent):
            # this will stop the while loop from running
            self.keepGoing = False


class PygameView:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        pygame.init()
        self.window = pygame.display.set_mode((424, 440))
        pygame.display.set_caption('Example Game')
        self.background = pygame.Surface(self.window.get_size())
        self.background.fill((0, 0, 0))
        font = pygame.font.Font(None, 30)
        text = """Press SPACE BAR to start"""
        textImg = font.render(text, 1, (255, 0, 0))
        self.background.blit(textImg, (0, 0))
        self.window.blit(self.background, (0, 0))
        pygame.display.flip()

        self.backSprites = pygame.sprite.RenderUpdates()
        self.frontSprites = pygame.sprite.RenderUpdates()

    def ShowMap(self, gameMap):
        # clear the screen first
        self.background.fill((0, 0, 0))
        self.window.blit(self.background, (0, 0))
        pygame.display.flip()

        # use this squareRect as a cursor and go through the
        # columns and rows and assign the rect
        # positions of the SectorSprites
        squareRect = pygame.Rect((-128, 10, 128, 128))

        column = 0
        for sector in gameMap.sectors:
            if column < 3:
                squareRect = squareRect.move(138, 0)
            else:
                column = 0
                squareRect = squareRect.move(-(138 * 2), 138)
            column += 1
            newSprite = sprites.SectorSprite(sector, self.backSprites)
            newSprite.rect = squareRect
            newSprite = None

    def ShowCharactor(self, charactor):
        sector = charactor.sector
        charactorSprite = sprites.CharactorSprite(self.frontSprites)
        sectorSprite = self.GetSectorSprite(sector)
        charactorSprite.rect.center = sectorSprite.rect.center

    def MoveCharactor(self, charactor):
        charactorSprite = self.GetCharactorSprite(charactor)

        sector = charactor.sector
        sectorSprite = self.GetSectorSprite(sector)

        charactorSprite.moveTo = sectorSprite.rect.center

    def GetCharactorSprite(self, charactor):
        # there will be only one
        for s in self.frontSprites:
            return s
        return None

    def GetSectorSprite(self, sector):
        for s in self.backSprites:
            if hasattr(s, "sector") and s.sector == sector:
                return s

    def Notify(self, event):
        if isinstance(event, events.TickEvent):
            # Draw Everything
            self.backSprites.clear(self.window, self.background)
            self.frontSprites.clear(self.window, self.background)

            self.backSprites.update()
            self.frontSprites.update()

            dirtyRects1 = self.backSprites.draw(self.window)
            dirtyRects2 = self.frontSprites.draw(self.window)

            dirtyRects = dirtyRects1 + dirtyRects2
            pygame.display.update(dirtyRects)


        elif isinstance(event, events.MapBuiltEvent):
            gameMap = event.map
            self.ShowMap(gameMap)

        elif isinstance(event, events.CharactorPlaceEvent):
            self.ShowCharactor(event.charactor)

        elif isinstance(event, events.CharactorMoveEvent):
            self.MoveCharactor(event.charactor)


class Game:
    """..."""

    STATE_PREPARING = 'preparing'
    STATE_RUNNING = 'running'
    STATE_PAUSED = 'paused'

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.state = Game.STATE_PREPARING

        self.players = [player.Player(evManager)]
        self.map = map.Map(evManager)

    # ----------------------------------------------------------------------
    def Start(self):
        self.map.Build()
        self.state = Game.STATE_RUNNING
        ev = events.GameStartedEvent(self)
        self.evManager.Post(ev)

    # ----------------------------------------------------------------------
    def Notify(self, event):
        if isinstance(event, events.TickEvent):
            if self.state == Game.STATE_PREPARING:
                self.Start()


# ------------------------------------------------------------------------------
def main():
    """..."""
    evManager = events.EventManager()

    keybd = inputs.KeyboardController(evManager)
    spinner = CPUSpinnerController(evManager)
    pygameView = PygameView(evManager)
    game = Game(evManager)

    spinner.Run()


if __name__ == "__main__":
    main()

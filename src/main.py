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

    def __init__(self, evManager, clock_tick_value=40):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.keepGoing = 1
        self.clock = pygame.time.Clock()
        self.tick_value = clock_tick_value

    def Run(self):
        while self.keepGoing:
            event = events.TickEvent()
            self.evManager.Post(event)
            self.clock.tick(self.tick_value)

    def Notify(self, event):
        if isinstance(event, events.QuitEvent):
            # this will stop the while loop from running
            self.keepGoing = False


class PygameView:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.sector_width = CELL_WIDTH
        self.sector_height = CELL_WIDTH
        frame_width = self.sector_width * 4
        frame_height = self.sector_width * 4

        pygame.init()
        self.window = pygame.display.set_mode((frame_width, frame_height))

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

        for i in range(len(gameMap.getSectors())):
            msp = gameMap.createSectorSprites(i)
            msp.add((self.backSprites))

    def ShowCharactor(self, charactor):
        sector = charactor.sector
        charactorSprite = sprites.CharactorSprite(self.evManager, 64, 64, self.frontSprites)
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


import g2048

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
        self.map = g2048.Game2048Map(evManager, CELL_WIDTH, CELL_HEIGHT)

    def Start(self):
        self.map.Build()
        self.state = Game.STATE_RUNNING
        ev = events.GameStartedEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, events.TickEvent):
            if self.state == Game.STATE_PREPARING:
                self.Start()


def main():
    """..."""
    evManager = events.EventManager()

    keybd = inputs.KeyboardController(evManager)
    spinner = CPUSpinnerController(evManager, 30)
    pygameView = PygameView(evManager)
    game = Game(evManager)

    spinner.Run()


if __name__ == "__main__":
    main()

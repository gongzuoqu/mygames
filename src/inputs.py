import pygame
from pygame.locals import *

from common import *
import events

class KeyboardController:
    """KeyboardController takes Pygame events generated by the
        keyboard and uses them to control the model, by sending Requests
        or to control the Pygame display directly, as with the QuitEvent
        """

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Notify(self, event):
        if isinstance(event, events.TickEvent):
            # Handle Input Events
            for event in pygame.event.get():
                ev = None
                if event.type == QUIT:
                    ev = events.QuitEvent()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        ev = events.QuitEvent()
                    elif event.key == K_UP:
                        direction = DIRECTION_UP
                        ev = events.CharactorMoveRequestEvent(direction)
                    elif event.key == K_DOWN:
                        direction = DIRECTION_DOWN
                        ev = events.CharactorMoveRequestEvent(direction)
                    elif event.key == K_LEFT:
                        direction = DIRECTION_LEFT
                        ev = events.CharactorMoveRequestEvent(direction)
                    elif event.key == K_RIGHT:
                        direction = DIRECTION_RIGHT
                        ev = events.CharactorMoveRequestEvent(direction)

                if ev:
                    self.evManager.Post(ev)



import events

class Player(object):
    """..."""

    def __init__(self, evManager):
        self.evManager = evManager
        self.game = None
        self.name = ""
        self.evManager.RegisterListener(self)

        self.charactors = [Charactor(evManager)]

    def __str__(self):
        return '<Player %s %s>' % (self.name, id(self))

    def Notify(self, event):
        pass


class Charactor:
    """..."""

    STATE_INACTIVE = 0
    STATE_ACTIVE = 1

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.sector = None
        self.state = Charactor.STATE_INACTIVE

    def __str__(self):
        return '<Charactor %s>' % id(self)

    def Move(self, direction):
        if self.state == Charactor.STATE_INACTIVE:
            return

        if self.sector.MovePossible(direction):
            newSector = self.sector.neighbors[direction]
            self.sector = newSector
            ev = events.CharactorMoveEvent(self)
            self.evManager.Post(ev)

    def Place(self, sector):
        self.sector = sector
        self.state = Charactor.STATE_ACTIVE

        ev = events.CharactorPlaceEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, events.GameStartedEvent):
            gameMap = event.game.map
            self.Place(gameMap.sectors[gameMap.startSectorIndex])

        elif isinstance(event, events.CharactorMoveRequestEvent):
            self.Move(event.direction)



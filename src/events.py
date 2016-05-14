
def Debug(msg):
    print(msg)


class Event:
    """this is a superclass for any events that might be generated by an
    object and sent to the EventManager"""

    def __init__(self):
        self.name = "Generic Event"


class TickEvent(Event):
    def __init__(self):
        self.name = "CPU Tick Event"


class QuitEvent(Event):
    def __init__(self):
        self.name = "Program Quit Event"


class MapBuiltEvent(Event):
    def __init__(self, gameMap):
        self.name = "Map Finished Building Event"
        self.map = gameMap


class GameStartedEvent(Event):
    def __init__(self, game):
        self.name = "Game Started Event"
        self.game = game


class CharactorMoveRequestEvent(Event):
    def __init__(self, direction):
        self.name = "Charactor Move Request"
        self.direction = direction


class CharactorPlaceEvent(Event):
    """this event occurs when a Charactor is *placed* in a sector,
        ie it doesn't move there from an adjacent sector."""

    def __init__(self, charactor):
        self.name = "Charactor Placement Event"
        self.charactor = charactor


class CharactorMoveEvent(Event):
    def __init__(self, charactor):
        self.name = "Charactor Move Event"
        self.charactor = charactor


class EventManager:
    """this object is responsible for coordinating most communication
        between the Model, View, and Controller."""

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()
        self.eventQueue = []

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners:
            del self.listeners[listener]

    def Post(self, event):
        if not isinstance(event, TickEvent):
            Debug("     Message: " + event.name)
        for listener in self.listeners:
            # NOTE: If the weakref has died, it will be
            # automatically removed, so we don't have
            # to worry about it.
            listener.Notify(event)



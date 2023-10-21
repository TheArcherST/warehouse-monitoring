from typing import Callable, TypeAlias, Awaitable, TypeVar

from warehouse_monitoring.domain.gateway.events import BaseEvent


EventType = TypeVar("EventType", bound=BaseEvent)
HandlerType: TypeAlias = Callable[[EventType], Awaitable[None]]


class Handler(HandlerType):
    def __init__(self):
        self.handlers = []

    async def propagate(self, *args, **kwargs):
        for i in self.triggers:
            await i(*args, **kwargs)

    def register(self, handler: HandlerType):
        self.handlers.append(handler)

    def unregister(self, handler: HandlerType):
        self.handlers.remove(handler)

    # C# semantics
    __call__ = propagate
    __iadd__ = register
    __isub__ = unregister


class WarehouseObserver:
    """Warehouse observer object

    Object that has event handlers.  You can subscribe for some event
    types here, and then propagate events.

    """

    def __init__(self):
        self.new_task = Handler()
        self.checkpoint_triggerred = Handler()
        self.take_task = Handler()

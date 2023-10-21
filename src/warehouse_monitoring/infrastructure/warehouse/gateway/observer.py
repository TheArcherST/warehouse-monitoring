import asyncio
from typing import Callable, TypeAlias, Awaitable, TypeVar

from warehouse_monitoring.infrastructure.warehouse.gateway.events import BaseEvent


EventType = TypeVar("EventType", bound=BaseEvent)
HandlerType: TypeAlias = Callable[[EventType], Awaitable[None]]


class Handler(HandlerType):
    def __init__(self):
        self.handlers = []

    async def propagate(self, event: EventType):
        for i in self.handlers:
            await i(event)

    def propagate_lazy(self, event: EventType):
        asyncio.create_task(self.propagate(event))

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
        self.reach_point = Handler()
        self.start_task = Handler()
        self.finish_task = Handler()
        self.reach_target = Handler()

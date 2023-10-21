from warehouse_monitoring.domain.gateway.observer import WarehouseObserver
from warehouse_monitoring.domain.gateway import events


async def take_task_handler(
        event: events.TakeTaskEvent,
):
    pass


def register(observer: WarehouseObserver):
    observer.take_task += take_task_handler

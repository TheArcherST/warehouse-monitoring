from warehouse_monitoring.infrastructure.warehouse.gateway.observer import \
    WarehouseObserver
from warehouse_monitoring.infrastructure.warehouse.gateway import events


async def start_task_handler(
        event: events.StartTaskEvent,
):
    pass


def register(observer: WarehouseObserver):
    observer.start_task += start_task_handler

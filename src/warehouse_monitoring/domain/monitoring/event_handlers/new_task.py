from warehouse_monitoring.domain.gateway.observer import WarehouseObserver
from warehouse_monitoring.domain.gateway import events


async def new_task_handler(
        event: events.NewTaskEvent,
):
    pass


def register(observer: WarehouseObserver):
    observer.new_task += new_task_handler

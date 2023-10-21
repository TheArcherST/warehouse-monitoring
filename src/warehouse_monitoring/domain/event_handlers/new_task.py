from warehouse_monitoring.infrastructure.warehouse.gateway import \
    WarehouseObserver, events


async def new_task_handler(
        event: events.NewTaskEvent,
):
    pass


def register(observer: WarehouseObserver):
    observer.new_task += new_task_handler

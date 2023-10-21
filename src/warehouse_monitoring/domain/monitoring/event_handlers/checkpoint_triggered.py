from warehouse_monitoring.domain.gateway.observer import WarehouseObserver
from warehouse_monitoring.domain.gateway import events


async def checkpoint_triggerred_handler(
        event: events.CheckpointTriggeredEvent,
):
    pass


def register(observer: WarehouseObserver):
    observer.checkpoint_triggerred += checkpoint_triggerred_handler

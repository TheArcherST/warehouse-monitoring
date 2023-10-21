from warehouse_monitoring.infrastructure.warehouse.gateway.observer import WarehouseObserver

from . import (
    start_task,
    new_task,
    reach_point,
)


def register(observer: WarehouseObserver):
    start_task.register(observer)
    new_task.register(observer)
    reach_point.register(observer)

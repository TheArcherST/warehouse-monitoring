from warehouse_monitoring.infrastructure.warehouse.gateway import dtos

from .base import BaseEvent


class NewWarehouseEvent(BaseEvent):
    new_warehouse: dtos.WarehouseDTO

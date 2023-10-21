from warehouse_monitoring.domain.gateway import dtos

from .base import BaseEvent


class NewWarehouseEvent(BaseEvent):
    new_warehouse: dtos.WarehouseDTO

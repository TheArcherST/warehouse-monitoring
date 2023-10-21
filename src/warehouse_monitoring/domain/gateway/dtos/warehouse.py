from warehouse_monitoring.infrastructure.bases.dto import BaseDTO

from .checkpoit import CheckpointDTO


class WarehouseDTO(BaseDTO):
    id: int
    checkpoints: list[CheckpointDTO]

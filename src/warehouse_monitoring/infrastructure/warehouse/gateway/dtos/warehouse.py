from warehouse_monitoring.infrastructure.bases.dto import BaseDTO

from .checkpoit import CheckpointDTO
from .forklift import ForkliftDTO


class WarehouseDTO(BaseDTO):
    id: int
    checkpoints: list[CheckpointDTO]
    forklifts: list[ForkliftDTO]

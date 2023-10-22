from warehouse_monitoring.infrastructure.bases.dto import BaseDTO

from .checkpoit import CheckpointDTO
from .forklift import ForkliftDTO
from .path import PathDTO


class WarehouseDTO(BaseDTO):
    id: int
    city_name: str
    checkpoints: list[CheckpointDTO]
    forklifts: list[ForkliftDTO]
    paths: list[PathDTO]

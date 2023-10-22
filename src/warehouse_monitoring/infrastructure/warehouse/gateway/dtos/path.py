from __future__ import annotations

from typing import TYPE_CHECKING


from warehouse_monitoring.infrastructure.bases.dto import BaseDTO

from .checkpoit import CheckpointDTO
from .rack import RackDTO


class PathDTO(BaseDTO):
    id: int
    warehouse_id: int
    checkpoints: list[CheckpointDTO]
    rack: RackDTO
    length: int

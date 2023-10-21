from typing import Optional

from warehouse_monitoring.infrastructure.bases.dto import BaseDTO


class TaskDTO(BaseDTO):
    id: int
    warehouse_id: int
    forklift_id: Optional[int]
    path_id: int

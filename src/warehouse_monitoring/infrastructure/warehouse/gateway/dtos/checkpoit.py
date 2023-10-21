from warehouse_monitoring.infrastructure.bases.dto import BaseDTO


class CheckpointDTO(BaseDTO):
    id: int
    warehouse_id: int
    location_x: int
    location_y: int

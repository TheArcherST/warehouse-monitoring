from warehouse_monitoring.infrastructure.bases.dto import BaseDTO


class RackDTO(BaseDTO):
    id: int
    location_x: int
    location_y: int

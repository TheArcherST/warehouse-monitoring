from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository,
)
from warehouse_monitoring.domain.monitoring import models


class CheckpointRepository(BaseRepository):
    async def create_checkpoint(
            self,
            id_: int,
            location_x: int,
            location_y: int,
    ):
        checkpoint = models.CheckpointStatus

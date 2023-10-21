from typing import Iterable
from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository,
)
from warehouse_monitoring.domain.monitoring import models


class WarehouseRepo(BaseRepository):
    async def create_warehouse(
            self,
            city: str,
            forklifts: list[models.Forklift],
            checkpoints: list[models.Checkpoint],
            task_queue: models.TasksQueue,
    ) -> models.Warehouse:
        pass

    async def get_warehouse_by_id(
            self,
            id_: int,
    ) -> models.Warehouse:
        pass

    async def search_warehouse_by_city(
            self,
            id_: int,
    ) -> Iterable[models.Warehouse]:
        pass

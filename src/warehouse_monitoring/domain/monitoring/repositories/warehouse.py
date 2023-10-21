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
            warehouse_id: int,
    ) -> models.Warehouse:
        stmt = (select(models.Warehouse).where(models.Warehouse.id == warehouse_id))
        return await self.session.scalar(stmt)

    # мы просто сравнили на равенство строк
    async def search_warehouse_by_city(
            self,
            city_name: str,
    ) -> Iterable[models.Warehouse]:
        stmt = (select(models.Warehouse).where(models.Warehouse.city == city_name))
        return await self.session.scalar(stmt)


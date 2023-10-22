from typing import Iterable
from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository,
)
from warehouse_monitoring.domain import models


class WarehouseRepo(BaseRepository):
    async def create_warehouse(
            self,
            id_: int,
            city_name: str,
            forklifts: list[models.Forklift],
            checkpoints: list[models.Checkpoint],
            task_queue: models.TaskQueue,
    ) -> models.Warehouse:
        obj = models.Warehouse(
            id=id_,
            city_name=city_name,
            forklifts=forklifts,
            checkpoints=checkpoints,
            task_queue=task_queue,
        )
        self.session.add(obj)
        await self.session.flush()

        return obj

    async def get_warehouse_by_id(
            self,
            warehouse_id: int,
    ) -> models.Warehouse:
        stmt = (select(models.Warehouse).where(
            models.Warehouse.id == warehouse_id))
        return await self.session.scalar(stmt)

    async def search_warehouse_by_city(
            self,
            city_name: str,
    ) -> Iterable[models.Warehouse]:
        stmt = (select(models.Warehouse)
                .where(models.Warehouse.city_name == city_name))
        return [await self.session.scalar(stmt)]

    async def get_all_warehouses(
            self,
    ) -> Iterable[models.Warehouse]:
        stmt = (select(models.Warehouse))
        return await self.session.scalars(stmt)

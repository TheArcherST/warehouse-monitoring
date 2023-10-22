from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository,
)
from warehouse_monitoring.domain import models


class CheckpointRepo(BaseRepository):
    async def create_checkpoint(
            self,
            local_id: int,
            warehouse_id: int,
            location_x: int,
            location_y: int,
    ) -> models.Checkpoint:
        obj = models.Checkpoint(
            local_id=local_id,
            warehouse_id=warehouse_id,
            location_x=location_x,
            location_y=location_y
        )
        self.session.add(obj)
        await self.session.flush()
        return obj

    async def get_checkpoint_by_id(
            self,
            checkpoint_id: int,
    ) -> models.Checkpoint:
        stmt = (select(models.Checkpoint)
                .where(models.Checkpoint.id == checkpoint_id))
        return await self.session.scalar(stmt)

    async def get_checkpoint_by_local_id(
            self,
            local_id: int,
            warehouse_id: int,
    ) -> models.Checkpoint:
        stmt = (select(models.Checkpoint)
                .where(models.Checkpoint.local_id == local_id)
                .where(models.Checkpoint.warehouse_id == warehouse_id))
        return await self.session.scalar(stmt)

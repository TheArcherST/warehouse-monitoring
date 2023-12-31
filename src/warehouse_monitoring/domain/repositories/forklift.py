from __future__ import annotations

from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository, )
from warehouse_monitoring.domain import models


class ForkliftRepo(BaseRepository):
    async def create_forklift(
            self,
            warehouse_id: int,
            local_id: int,
    ) -> models.Forklift:
        obj = models.Forklift(
            warehouse_id=warehouse_id,
            local_id=local_id,
        )
        self.session.add(obj)
        await self.session.flush()
        return obj

    async def get_forklift_by_id(
            self, id_: int,
    ) -> models.Forklift:
        stmt = (select(models.Forklift).where(models.Forklift.id == id_))
        return await self.session.scalar(stmt)

    async def get_forklift_by_local_id(
            self,
            local_id: int,
            warehouse_id: int,
    ) -> models.Forklift:
        stmt = (select(models.Forklift)
                .where(models.Forklift.local_id == local_id)
                .where(models.Forklift.warehouse_id == warehouse_id))
        return await self.session.scalar(stmt)

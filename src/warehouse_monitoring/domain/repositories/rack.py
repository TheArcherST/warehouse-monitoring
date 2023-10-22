from __future__ import annotations

from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository, )
from warehouse_monitoring.domain import models


class RackRepo(BaseRepository):
    async def create_rack(
            self,
            warehouse_id: int,
            local_id: int,
    ) -> models.Rack:
        obj = models.Rack(
            warehouse_id=warehouse_id,
            local_id=local_id,
        )
        self.session.add(obj)
        await self.session.flush()
        return obj

    async def get_rack_by_id(
            self, id_: int,
    ) -> models.Rack:
        stmt = ((select(models.Rack)
                 .where(models.Rack.id == id_)))
        return await self.session.scalar(stmt)

    async def get_rack_by_local_id(
            self,
            local_id: int,
            warehouse_id: int,
    ) -> models.Rack:
        stmt = (select(models.Rack)
                .where(models.Rack.local_id == local_id)
                .where(models.Rack.warehouse_id == warehouse_id))
        return await self.session.scalar(stmt)

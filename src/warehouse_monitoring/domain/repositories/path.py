from __future__ import annotations

from sqlalchemy import select

from warehouse_monitoring.domain.models import Path, Rack, Checkpoint
from warehouse_monitoring.infrastructure.bases.repository import BaseRepository
from warehouse_monitoring.infrastructure.warehouse.emulator.config import get_path_length


class PathRepo(BaseRepository):
    async def create_path(
            self,
            local_id: int,
            rack: Rack,
            checkpoints: list[Checkpoint],
            length: int, warehouse_id: int,
    ):
        obj = Path(
            local_id=local_id,
            length=length,
            rack=rack,
            checkpoints=checkpoints,
            warehouse_id=warehouse_id,
        )
        self.session.add(obj)
        await self.session.flush()

    async def get_path_by_id(
            self,
            path_id: int,
    ) -> Path:
        stmt = (select(Path)
                .where(Path.id == path_id))
        obj = await self.session.scalar(stmt)
        return obj

    async def get_path_by_local_id(
            self,
            local_id: int,
            warehouse_id: int,
    ):
        stmt = (select(Path)
                .where(Path.local_id == local_id)
                .where(Path.warehouse_id == warehouse_id))
        return await self.session.scalar(stmt)

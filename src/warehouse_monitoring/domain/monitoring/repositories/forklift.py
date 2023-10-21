from sqlalchemy import select, text

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository, )
from warehouse_monitoring.domain.monitoring import models


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
            self, internal_id: int,
    ) -> models.Forklift:
        pass

    async def get_forklift_by_internal_id(
            self,
            warehouse_id: int,
            internal_id: int,
    ) -> models.Forklift:
        pass

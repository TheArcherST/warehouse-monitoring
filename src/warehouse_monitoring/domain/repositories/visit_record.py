from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository, )
from warehouse_monitoring.domain import models


class VisitRecordRepo(BaseRepository):
    async def create_(
            self,
            checkpoint: models.Checkpoint,
            forklift: models.Forklift,
    ) -> models.VisitRecord:
        pass

    async def search_visit_records_by_forklift(
            self, forklift: models.Forklift,
    ) -> models.VisitRecord:
        stmt = (select(models.VisitRecord)
                .where(models.VisitRecord.forklift == forklift))
        return await self.session.scalar(stmt)

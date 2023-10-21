from sqlalchemy import select, text

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository, )
from warehouse_monitoring.domain.monitoring import models


class VisitRecordRepo(BaseRepository):
    async def create_visit_record(
            self,
            checkpoint: models.Checkpoint,
            forklift: models.Forklift,
    ) -> models.VisitRecord:
        pass

    async def search_visit_records_by_forklift(
            self, forklift: models.Forklift,
    ) -> models.VisitRecord:
        pass

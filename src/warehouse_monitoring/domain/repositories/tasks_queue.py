from sqlalchemy import select

from warehouse_monitoring.infrastructure.bases.repository import (
    BaseRepository, )
from warehouse_monitoring.domain import models


class TaskQueueRepo(BaseRepository):
    async def create_tasks_queue(
            self,
    ) -> models.TaskQueue:
        obj = models.TaskQueue(
        )
        self.session.add(obj)
        await self.session.flush()
        return obj

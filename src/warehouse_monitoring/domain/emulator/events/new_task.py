from src.warehouse_monitoring.domain.monitoring.dtos import TaskDTO

from .base import BaseEvent


class NewTaskEvent(BaseEvent):
    """New task event

    This event means that some new task has arrived to the warehouse,
    and was added to its tasks query.

    """

    def __init__(
            self,
            new_task: TaskDTO
    ):
        self.task = new_task

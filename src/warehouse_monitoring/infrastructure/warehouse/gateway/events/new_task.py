from warehouse_monitoring.infrastructure.warehouse.gateway.dtos import TaskDTO

from .base import BaseEvent


class NewTaskEvent(BaseEvent):
    """New task event

    This event means that some new task has arrived to the warehouse,
    and was added to its tasks query.

    """

    new_task: TaskDTO

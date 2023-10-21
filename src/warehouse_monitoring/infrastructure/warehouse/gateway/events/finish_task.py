from .base import BaseEvent


class FinishTaskEvent(BaseEvent):
    task_id: int
    forklift_id: int
    warehouse_id: int

from .base import BaseEvent


class StartTaskEvent(BaseEvent):
    """Start task event

    This event means that task performing is started by some forklift.

    """

    task_id: int
    warehouse_id: int
    forklift_id: int

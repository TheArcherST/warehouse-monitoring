from .base import BaseEvent


class TakeTaskEvent(BaseEvent):
    """Take task event

    This event means that task performing is started by some forklift.

    """

    task_id: int
    forklift_id: int

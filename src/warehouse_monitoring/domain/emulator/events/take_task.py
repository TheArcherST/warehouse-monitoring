from .base import BaseEvent


class TakeTaskEvent(BaseEvent):
    """Take task event

    This event means that task performing is started by some forklift.

    """

    def __init__(
            self,
            task_id: int,
            forklift_id: int,
    ):
        self.task_id = task_id
        self.forklift_id = forklift_id

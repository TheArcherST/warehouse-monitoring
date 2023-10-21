from .base import BaseEvent


class ReachPoint(BaseEvent):
    warehouse_id: int
    checkpoint_id: int
    forklift_id: int

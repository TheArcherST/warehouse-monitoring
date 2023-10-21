from .base import BaseEvent


class VisitPointEvent(BaseEvent):
    warehouse_id: int
    checkpoint_id: int
    forklift_id: int

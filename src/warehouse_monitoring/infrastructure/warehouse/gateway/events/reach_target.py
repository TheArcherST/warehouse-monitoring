from .base import BaseEvent


class ReachTargetEvent(BaseEvent):
    forklift_id: int
    warehouse_id: int
    target_rack_id: int

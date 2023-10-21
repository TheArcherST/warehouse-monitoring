from .base import BaseEvent


class CheckpointTriggeredEvent(BaseEvent):
    checkpoint_id: int

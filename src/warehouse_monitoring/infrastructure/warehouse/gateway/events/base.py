from datetime import datetime

from warehouse_monitoring.infrastructure.bases.dto import BaseDTO


class BaseEvent(BaseDTO):
    at: datetime


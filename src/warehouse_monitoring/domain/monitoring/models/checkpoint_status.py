from enum import Enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base


class CheckpointStatusValueEnum(Enum):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'


class CheckpointStatus(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[CheckpointStatusValueEnum] = mapped_column()
    created_at: Mapped[datetime] = mapped_column()

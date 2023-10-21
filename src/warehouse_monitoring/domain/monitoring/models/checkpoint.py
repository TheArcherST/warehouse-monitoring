from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.domain.monitoring.models import (
    CheckpointStatus,
    CheckpointStatusValueEnum,
)


class Checkpoint(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status_id: Mapped[int] = mapped_column(ForeignKey(""))
    status: Mapped[CheckpointStatus] = relationship()
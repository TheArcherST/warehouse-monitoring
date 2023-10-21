from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base


if TYPE_CHECKING:
    from warehouse_monitoring.domain.models import Checkpoint, Forklift


class VisitRecord(Base):
    __tablename__ = 'visit_record'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    checkpoint_id: Mapped[int] = mapped_column(ForeignKey("checkpoint.id"))
    forklift_id: Mapped[int] = mapped_column(ForeignKey("forklift.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    checkpoint: Mapped[Checkpoint] = relationship()
    forklift: Mapped[Forklift] = relationship()

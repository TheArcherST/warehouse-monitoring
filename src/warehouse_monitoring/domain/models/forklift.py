from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.domain.models import Warehouse


class Forklift(Base):
    __tablename__ = 'forklift'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouse.id"))
    local_id: Mapped[int] = mapped_column()

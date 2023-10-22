from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base

if TYPE_CHECKING:
    from warehouse_monitoring.domain.models import Path


class Rack(Base):
    __tablename__ = 'rack'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    local_id: Mapped[int] = mapped_column()
    warehouse_id: Mapped[int] = mapped_column()

    @property
    def unified_identifier(self):
        return 'X{}'.format(self.local_id)

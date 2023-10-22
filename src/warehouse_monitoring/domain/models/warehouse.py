from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos

if TYPE_CHECKING:
    from warehouse_monitoring.domain.models import (
        Forklift, Checkpoint, TaskQueue, Path,
    )


class Warehouse(Base):
    __tablename__ = 'warehouse'

    # note: warehouse is aggregate root, so, has not local id
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_name: Mapped[str] = mapped_column()
    task_queue_id: Mapped[int] = mapped_column(ForeignKey("task_queue.id"))

    forklifts: Mapped[list[Forklift]] = relationship(
        lazy='selectin',
    )
    checkpoints: Mapped[list[Checkpoint]] = relationship(
        lazy='selectin',
    )
    paths: Mapped[list[Path]] = relationship(
        lazy='selectin',
    )
    task_queue: Mapped[TaskQueue] = relationship(
        lazy='selectin'
    )

    def to_dto(self) -> dtos.WarehouseDTO:
        return dtos.WarehouseDTO(
            id=self.id,
            forklifts=[i.to_dto() for i in self.forklifts],
            checkpoints=[i.to_dto() for i in self.checkpoints],
            paths=[i.to_dto() for i in self.paths],
        )

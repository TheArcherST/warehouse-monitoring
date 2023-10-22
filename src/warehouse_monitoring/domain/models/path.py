from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos


if TYPE_CHECKING:
    from warehouse_monitoring.domain.models import Checkpoint, Rack


class CheckpointRelPath(Base):
    __tablename__ = 'checkpoint_rel_path'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    checkpoint_id: Mapped[int] = mapped_column(ForeignKey("checkpoint.id"))
    path_id: Mapped[int] = mapped_column(ForeignKey("path.id"))


class Path(Base):
    __tablename__ = 'path'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    local_id: Mapped[int] = mapped_column()
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouse.id"))
    length: Mapped[float] = mapped_column()
    rack_id: Mapped[int] = mapped_column(ForeignKey("rack.id"))

    rack: Mapped[Rack] = relationship()
    checkpoints: Mapped[list[Checkpoint]] = relationship(
        secondary=CheckpointRelPath.__table__,
    )

    def to_dto(self) -> dtos.PathDTO:
        return dtos.PathDTO(
            checkpoints=[i.to_dto() for i in self.checkpoints],
            rack=self.rack.to_dto(),
            length=self.length,
        )

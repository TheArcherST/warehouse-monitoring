from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos


class Checkpoint(Base):
    __tablename__ = 'checkpoint'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouse.id'))
    local_id: Mapped[int] = mapped_column()
    location_x: Mapped[int] = mapped_column()
    location_y: Mapped[int] = mapped_column()

    def to_dto(self) -> dtos.CheckpointDTO:
        return dtos.CheckpointDTO(
            id=self.local_id,
            warehouse_id=self.warehouse_id,
            location_x=self.location_x,
            location_y=self.location_y,
        )

    @property
    def unified_identifier(self):
        return 'K{}'.format(self.local_id)

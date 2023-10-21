from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base


class Checkpoint(Base):
    __tablename__ = 'checkpoint'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouse.id'))
    local_id: Mapped[int] = mapped_column()
    location_x: Mapped[int] = mapped_column()
    location_y: Mapped[int] = mapped_column()

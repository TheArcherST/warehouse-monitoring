from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base


class CheckpointRelPath(Base):
    __tablename__ = 'checkpoint_rel_path__ordered'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    checkpoint_id: Mapped[int] = mapped_column(ForeignKey("checkpoint.id"))
    path_id: Mapped[int] = mapped_column(ForeignKey("path.id"))
    index: Mapped[int] = mapped_column()


class Path(Base):
    __tablename__ = 'path'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    location_x: Mapped[int] = mapped_column()
    location_y: Mapped[int] = mapped_column()

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.domain import models


class CheckpointRelPath_Ordered(Base):
    __tablename__ = 'checkpoint_rel_path__ordered'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    checkpoint_id: Mapped[int] = mapped_column(ForeignKey("checkpoint.id"))
    path_id: Mapped[int] = mapped_column(ForeignKey("path.id"))
    index: Mapped[int] = mapped_column()


class Path(Base):
    __tablename__ = 'path'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # note: paths are common for all warehouses, because room plans are
    # identical

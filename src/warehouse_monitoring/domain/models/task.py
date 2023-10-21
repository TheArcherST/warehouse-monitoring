from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    path_id: Mapped[int] = mapped_column(ForeignKey("path.id"))

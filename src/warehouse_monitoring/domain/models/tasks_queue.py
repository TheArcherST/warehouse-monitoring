from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base


class TaskQueue(Base):
    __tablename__ = 'task_queue'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base


class TasksQueue(Base):
    __tablename__ = 'tasks_queue'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouse.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

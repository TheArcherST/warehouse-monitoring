from sqlalchemy.orm import Mapped, mapped_column, relationship

from warehouse_monitoring.infrastructure.database import Base
from warehouse_monitoring.domain.monitoring import models


class Warehouse(Base):
    # note: warehouse is aggregate root, so, has not local id
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[str] = mapped_column()

    forklifts: Mapped[list[models.Forklift]] = relationship(
        back_populates='warehouse', lazy='selectin',
    )
    checkpoints: Mapped[list[models.Checkpoint]] = relationship(
        back_populates='warehouse', lazy='selectin',
    )
    task_queue: Mapped[models.TasksQueue] = relationship(
        back_populates='warehouse', lazy='selectin'
    )

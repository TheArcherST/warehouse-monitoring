from sqlalchemy.orm import Mapped, mapped_column

from warehouse_monitoring.infrastructure.database import Base


class Path(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

from typing import Annotated

from fastapi import Depends
from warehouse_monitoring.infrastructure.database import (
    inject_database_session,
    DatabaseSession,
)


SessionDep = Annotated[DatabaseSession, Depends(inject_database_session)]

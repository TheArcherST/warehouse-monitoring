from typing import Annotated
from fastapi import Depends

from warehouse_monitoring.domain import services

from . import repositories


async def get_movement_service(
        checkpoint_repo: repositories.CheckpointRepoDep,
        visit_record_repo: repositories.VisitRecordRepoDep,
        forklift_repo: repositories.ForkliftRepoDep,
):
    yield services.MovementService(
        checkpoint_repo=checkpoint_repo,
        visit_record_repo=visit_record_repo,
        forklift_repo=forklift_repo,
    )


ForkliftRepoDep = Annotated[
    services.MovementService,
    Depends(get_movement_service)
]

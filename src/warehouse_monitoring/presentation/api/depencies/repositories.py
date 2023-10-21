from typing import Annotated
from fastapi import Depends

from warehouse_monitoring.domain import repositories

from .session import SessionDep


async def get_forklift_repo(session: SessionDep):
    yield repositories.ForkliftRepo(
        session=session,
    )


async def get_checkpoint_repo(session: SessionDep):
    yield repositories.CheckpointRepo(
        session=session,
    )


async def get_warehouse_repo(session: SessionDep):
    yield repositories.WarehouseRepo(
        session=session,
    )


async def get_visit_record_repo(session: SessionDep):
    yield repositories.VisitRecordRepo(
        session=session,
    )


ForkliftRepoDep = Annotated[
    repositories.ForkliftRepo,
    Depends(get_forklift_repo)
]

CheckpointRepoDep = Annotated[
    repositories.CheckpointRepo,
    Depends(get_checkpoint_repo)
]

WarehouseRepoDep = Annotated[
    repositories.WarehouseRepo,
    Depends(get_warehouse_repo)
]

VisitRecordRepoDep = Annotated[
    repositories.VisitRecordRepo,
    Depends(get_visit_record_repo)
]

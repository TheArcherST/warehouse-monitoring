from contextlib import asynccontextmanager

from warehouse_monitoring.infrastructure.database import inject_database_session
from warehouse_monitoring.domain import repositories, services

session_injection_manager = asynccontextmanager(inject_database_session)


class ServiceInteractorFactory:
    @asynccontextmanager
    async def movement_service(self):
        async with session_injection_manager() as session:
            checkpoint_repo = repositories.CheckpointRepo(
                session=session,
            )
            visit_record_repo = repositories.VisitRecordRepo(
                session=session,
            )
            forklift_repo = repositories.ForkliftRepo(
                session=session,
            )
            service = services.MovementService(
                checkpoint_repo=checkpoint_repo,
                visit_record_repo=visit_record_repo,
                forklift_repo=forklift_repo,
            )
            yield service

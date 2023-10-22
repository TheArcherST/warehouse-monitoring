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

    @asynccontextmanager
    async def configuration_merge_service(self):
        async with session_injection_manager() as session:
            checkpoint_repo = repositories.CheckpointRepo(
                session=session,
            )
            forklift_repo = repositories.ForkliftRepo(
                session=session,
            )
            path_repo = repositories.PathRepo(
                session=session,
            )
            warehouse_repo = repositories.WarehouseRepo(
                session=session,
            )
            rack_repo = repositories.RackRepo(
                session=session,
            )
            task_queue_repo = repositories.TaskQueueRepo(
                session=session,
            )
            service = services.ConfigurationMergeService(
                checkpoint_repo=checkpoint_repo,
                forklift_repo=forklift_repo,
                path_repo=path_repo,
                warehouse_repo=warehouse_repo,
                rack_repo=rack_repo,
                task_queue_repo=task_queue_repo,
            )
            yield service

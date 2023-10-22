from warehouse_monitoring.domain import repositories


class MovementService:
    def __init__(
            self,
            checkpoint_repo: repositories.CheckpointRepo,
            visit_record_repo: repositories.VisitRecordRepo,
            forklift_repo: repositories.ForkliftRepo,
    ):
        self.checkpoint_repo = checkpoint_repo
        self.visit_record_repo = visit_record_repo
        self.forklift_repo = forklift_repo

    async def notify_checkpoint_visit(
            self,
            warehouse_id: int,
            local_checkpoint_id: int,
            local_forklift_id: int,
    ) -> None:
        checkpoint = await self.checkpoint_repo.get_checkpoint_by_local_id(
            warehouse_id=warehouse_id,
            local_id=local_checkpoint_id,
        )
        forklift = await self.forklift_repo.get_forklift_by_local_id(
            warehouse_id=warehouse_id,
            local_id=local_forklift_id,
        )
        await self.visit_record_repo.create_visit_record(
            checkpoint=checkpoint,
            forklift=forklift,
        )

from warehouse_monitoring.infrastructure.bases.service import BaseService
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos

from warehouse_monitoring.domain import repositories


class ConfigurationMergeService(BaseService):
    def __init__(
            self,
            path_repo: repositories.PathRepo,
            warehouse_repo: repositories.WarehouseRepo,
            checkpoint_repo: repositories.CheckpointRepo,
            forklift_repo: repositories.ForkliftRepo,
            rack_repo: repositories.RackRepo,
            task_queue_repo: repositories.TaskQueueRepo,
    ):
        self.path_repo = path_repo
        self.warehouse_repo = warehouse_repo
        self.checkpoint_repo = checkpoint_repo
        self.forklift_repo = forklift_repo
        self.rack_repo = rack_repo
        self.task_queue_repo = task_queue_repo

    async def merge_configuration(
            self,
            configuration: dtos.Configuration,
    ):
        for i in configuration.warehouses:
            warehouse = await self.warehouse_repo.get_warehouse_by_id(
                warehouse_id=i.id,
            )
            if warehouse is None:
                warehouse = await self.warehouse_repo.create_warehouse(
                    id_=i.id,
                    city_name=i.city_name,
                    forklifts=[],
                    checkpoints=[],
                    task_queue=await self.task_queue_repo.create_tasks_queue(),
                )
            for j in i.forklifts:
                forklift = await self.forklift_repo.get_forklift_by_local_id(
                    local_id=j.id,
                    warehouse_id=j.warehouse_id,
                )
                if forklift is None:
                    await self.forklift_repo.create_forklift(
                        warehouse_id=j.warehouse_id,
                        local_id=j.id,
                    )
            for j in i.paths:
                path = await self.path_repo.get_path_by_local_id(
                    local_id=j.id,
                    warehouse_id=j.warehouse_id,
                )
                if path is None:
                    rack = await self.rack_repo.get_rack_by_local_id(
                        local_id=j.rack.id,
                        warehouse_id=j.warehouse_id,
                    )
                    if rack is None:
                        rack = await self.rack_repo.create_rack(
                            local_id=j.rack.id,
                            warehouse_id=j.warehouse_id,
                        )
                    checkpoints = []
                    for k in j.checkpoints:
                        checkpoint = await self.checkpoint_repo.get_checkpoint_by_local_id(
                            local_id=k.id,
                            warehouse_id=k.warehouse_id,
                        )
                        if checkpoint is None:
                            checkpoint = await self.checkpoint_repo.create_checkpoint(
                                local_id=k.id,
                                warehouse_id=k.warehouse_id,
                                location_x=k.location_x,
                                location_y=k.location_y,
                            )
                        checkpoints.append(checkpoint)
                    await self.path_repo.create_path(
                        j.id,
                        rack=rack,
                        checkpoints=checkpoints,
                        length=j.length,
                        warehouse_id=i.id,
                    )

from fastapi import APIRouter

from warehouse_monitoring.domain.monitoring import dtos


router = APIRouter(tags=["Data API"])


@router.get(
    "/warehouses/{warehouse_id}/tasks/{task_id}",
    response_model=dtos.TaskDTO,
)
async def get_warehouse(warehouse_id: int, task_id: int):
    # the pumpkin.  please adjust
    return dtos.TaskDTO(
        id=task_id,
        warehouse_id=warehouse_id,
        forklift_id=None,
        path_id=1,
    )

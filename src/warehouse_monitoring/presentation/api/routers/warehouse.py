from fastapi import APIRouter

from warehouse_monitoring.infrastructure.warehouse.gateway import dtos
from ..depencies import repositories


router = APIRouter(tags=["Data API"])


@router.get(
    "/warehouses",
    response_model=list[dtos.WarehouseDTO],
)
async def get_warehouses(
        warehouse_repo: repositories.WarehouseRepoDep,
):
    warehouses = await warehouse_repo.get_all_warehouses()
    return [dtos.WarehouseDTO(
        id=0, checkpoints=[dtos.CheckpointDTO(
            id=0, warehouse_id=0, location_x=1, location_y=2, )],
        forklifts=[dtos.ForkliftDTO(
            id=1
        ), ]
    ), dtos.WarehouseDTO(
            id=1, checkpoints=[dtos.CheckpointDTO(
                id=1, warehouse_id=2, location_x=2, location_y=3, )],
            forklifts=[dtos.ForkliftDTO(
                id=2
            ), ]
        ),
    ]


@router.get(
    "/warehouses/{warehouse_id}",
    response_model=dtos.WarehouseDTO,
)
async def get_warehouse(
        warehouse_repo: repositories.WarehouseRepoDep,
        warehouse_id: int,
):
    warehouse = await warehouse_repo.get_warehouse_by_id(
        warehouse_id=warehouse_id,
    )
    return dtos.WarehouseDTO(
            id=1, checkpoints=[dtos.CheckpointDTO(
                id=1, warehouse_id=2, location_x=2, location_y=3, )],
            forklifts=[dtos.ForkliftDTO(
                id=2
            ), ]
        )

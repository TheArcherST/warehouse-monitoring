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
    return [i.to_dto() for i in warehouses]


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
    return warehouse.to_dto()

from fastapi import APIRouter

from warehouse_monitoring.domain.application import dtos


router = APIRouter(tags=["Data API"])


@router.get(
    "/warehouses/{warehouse_id}",
    response_model=dtos.WarehouseDTO,
)
async def get_warehouse(warehouse_id: int):
    # the pumpkin.  please adjust
    return dtos.WarehouseDTO(
        id=warehouse_id,
    )

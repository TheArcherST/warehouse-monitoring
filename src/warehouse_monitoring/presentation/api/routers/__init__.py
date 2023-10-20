from fastapi import APIRouter


from . import (
    warehouse,
    task,
    events,
)


router = APIRouter()

router.include_router(warehouse.router)
router.include_router(task.router)
router.include_router(events.router)

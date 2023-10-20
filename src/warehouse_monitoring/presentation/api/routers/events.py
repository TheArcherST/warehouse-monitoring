import asyncio

from fastapi import APIRouter, WebSocket


router = APIRouter(tags=["Events API"])


@router.websocket(
    "/warehouses/{warehouse_id}/events/listen",
)
async def listen_for_warehouse_events(
        websocket: WebSocket,
):
    """Listen for warehouse events

    This endpoint allows to connect to some warehouse's events.

    There are following events are available:

    forklift.movement event
    -----------------------

    * current location of the forklift.
    * inferred value of a next location of the forklift.
    * current speed of a forklift.

    The purpose of this event is to achieve dynamic animation
    on the user interface.

    """

    # the pumpkin.  please adjust
    while True:
        await websocket.send({
            "event": "forklift.movement",
            "data": {
                "current_location": {"x": 10, "y": 20},
                "inferred_location": {"x": 10, "y": 20},
                "speed": 10,
            }
        })
        await asyncio.sleep(1)

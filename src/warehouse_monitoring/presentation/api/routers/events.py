import asyncio

from fastapi import APIRouter, WebSocket
import itertools


router = APIRouter(tags=["Events API"])

demo_coords = [(25, 0), (25, 5), (25, 10), (15, 10),]
demo_iterator = itertools.cycle(demo_coords)


@router.websocket(
    "/warehouses/{warehouse_id}/events/listen",
)
async def listen_for_warehouse_events(
        websocket: WebSocket,
        warehouse_id: int,
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
    await websocket.accept()
    current = next(demo_iterator)
    next_ = next(demo_iterator)
    while True:
        await websocket.send_json({
            "event": "forklift.movement",
            "data": {
                "current_location": {"x": current[0], "y": current[1]},
                "inferred_location": {"x": next_[0], "y": next_[1]},
                "speed": 2.5,
            }
        })
        current = next_
        next_ = next(demo_iterator)
        await asyncio.sleep(2)

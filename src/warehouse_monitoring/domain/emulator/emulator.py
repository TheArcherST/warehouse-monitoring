import asyncio
from random import randint

from warehouse_monitoring.domain import gateway
from warehouse_monitoring.domain.emulator.core import (
    Warehouse,
)
from warehouse_monitoring.domain.emulator.config import cities


class Emulator(gateway.protocol.WarehouseGatewayProto):
    def __init__(
            self,
            observer: gateway.observer.WarehouseObserver,
            warehouses_count: int,
    ):
        self._observer = observer
        self._warehouses: list[Warehouse] = []
        self._warehouses_count = warehouses_count

        # todo: implement stable state of the emulation.  maybe, to
        # simplify implementation, just pickle executor?  it's seems
        # like author of the first version of code hinted that we
        # can use pickle for this :)

        self._random_fill()

    def _random_fill(self):
        for i in range(self._warehouses_count):
            self._warehouses.append(
                Warehouse(
                    warehouse_id=i,
                    city=cities[randint(0, len(cities) - 1)]
                )
            )

    def start(self) -> None:
        for i in self._warehouses:
            asyncio.create_task(i.execution_loop())

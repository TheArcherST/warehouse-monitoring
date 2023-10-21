from typing import Protocol

from warehouse_monitoring.domain.gateway.observer import (
    WarehouseObserver,
)
from warehouse_monitoring.domain.gateway.dtos.configuration import (
    Configuration,
)


class WarehouseGatewayProto(Protocol):
    """Warehouse gateway protocol

    Represents abstract interface of communication with some
    system, that keeps states and adapting emulated or physical
    warehouse.

    """

    def set_observer(self, observer: WarehouseObserver):
        raise NotImplementedError()

    def get_configuration(self) -> Configuration:
        raise NotImplementedError()

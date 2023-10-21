from typing import Protocol

from warehouse_monitoring.infrastructure.warehouse.gateway.observer import (
    WarehouseObserver,
)


class WarehouseGatewayProto(Protocol):
    """Warehouse gateway protocol

    Represents abstract interface of communication with some
    system, that keeps states and adapting emulated or physical
    warehouse.

    """

    def set_observer(self, observer: WarehouseObserver):
        """Set observer method

        This method allows you to inject some observer to the warehouse,
        and warehouse will trigger events, enumerated within observer.

        """

        raise NotImplementedError()

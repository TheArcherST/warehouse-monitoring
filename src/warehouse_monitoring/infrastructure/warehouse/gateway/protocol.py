from typing import Protocol

from warehouse_monitoring.infrastructure.warehouse.gateway.observer import (
    WarehouseObserver,
)
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos


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

    def get_configuration(self) -> dtos.Configuration:
        """Get configuration method

        This method fetches configuration from the warehouse.  You can
        use this information to access base system element at any point
        of time.  Gateway implementation must know about agents that
        propagates underlying event.

        """

        raise NotImplementedError()

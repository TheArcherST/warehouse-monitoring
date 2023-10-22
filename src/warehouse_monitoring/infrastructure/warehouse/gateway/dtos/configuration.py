from __future__ import annotations

from warehouse_monitoring.infrastructure.bases.dto import BaseDTO
from warehouse_monitoring.infrastructure.warehouse.gateway import dtos


class Configuration(BaseDTO):
    """Warehouses configuration object

    Contain warehouses configuration.  Please, note that it mustn't
    be used to restore some gateway implementation, it doesn't keep
    all implementation details.  Use it to check abstract state of
    the warehouses.

    """

    warehouses: list[dtos.WarehouseDTO]

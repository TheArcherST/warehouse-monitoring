from __future__ import annotations

from warehouse_monitoring.domain.gateway import dtos


# class WarehouseConfiguration(BaseDTO):
#     id: int
#
#
# class PathConfiguration(BaseDTO):
#     pass
#
#
# class CheckpointConfiguration(BaseDTO):
#     pass
#
#
# class TaskConfiguration(BaseDTO):
#     pass


class Configuration:
    """Warehouses configuration object

    Contain warehouses configuration.  Please, note that it mustn't
    be used to restore some gateway implementation, it doesn't keep
    all implementation details.  Use it to check abstract state of
    the warehouses.

    """

    warehouses: list[dtos.WarehouseDTO]
    path: list[dtos.PathDTO]
    task_configuration: list[dtos.TaskDTO]
    checkpoints: list[dtos.CheckpointDTO]

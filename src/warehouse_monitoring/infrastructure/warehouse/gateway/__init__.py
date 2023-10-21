"""Gateway infrastructure module

This module defines communication interface between any warehouse
environment and monitoring system.  Now, there is only one warehouse
environment -- warehouse emulator.

"""


from . import (
    events,
    observer,
    protocol,
)

from .observer import WarehouseObserver


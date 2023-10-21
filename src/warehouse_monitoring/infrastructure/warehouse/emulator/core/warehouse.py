import asyncio

from .task import TaskQueue
from random import randint
from warehouse_monitoring.infrastructure.warehouse import gateway
from warehouse_monitoring.infrastructure.warehouse.emulator.core.forklift import Forklift


class Warehouse:
    """
    Warehouse class.
    It represents works of onw warehouse in given city

    Each warehouse object contains its identifier, city, tasks queue,
    and the list of forklifts (forklift part).

    Forklift park includes 6-15 forklifts.  This count is fixed.
    Tasks queue is dynamic.  Initial count of tasks is based on tasks
    queue length: the random count in range from forklifts * 2 to
    forklifts * 4.

    """

    def __init__(
            self,
            observer: gateway.observer.WarehouseObserver,
            warehouse_id: int,
            city: str,
    ):
        self.observer = observer
        self.id = warehouse_id
        self.city = city
        # queue for all task of this warehouse instance
        self.task_queue = TaskQueue(self.id)
        # list of all forklifts belongs to this warehouse instance
        self.forklift_park = []
        self.forklift_count = 0  # just counter to know next forklift id

        self._fill_forklift_park()
        self._fill_tasks_queue()

    def _fill_forklift_park(self):
        # init random number of workers
        for _ in range(randint(6, 15)):
            self.add_new_forklift()

    def _fill_tasks_queue(self):
        # init basic queue with random number of tasks, depends on
        # forklifts number
        for _ in range(randint(self.forklift_count * 2,
                               self.forklift_count * 4)):
            self.task_queue.create_new_task()

    def add_new_forklift(self):
        # create new forklift with next id from forklift_count
        # with current warehouse id
        # and it's tasks queue
        self.forklift_park.append(
            Forklift(
                observer=self.observer,
                forklift_id=self.forklift_count,
                warehouse_id=self.id,
                task_queue=self.task_queue,
            )
        )
        self.forklift_count += 1

    async def execution_loop(self):
        # infinite loop with warehouse works
        current = 0
        while True:
            # iterate over forklifts and make them work =)
            for forklift in self.forklift_park:
                forklift.work()
            if current % 10 == 1:
                for _ in range(randint(0, self.forklift_count)):
                    self.task_queue.create_new_task()

            # the pumpkin.  please adjust
            # need some algorithm to some forklifts were inactive,
            # just to demonstrate how application handles this case.
            # maybe, event implement different behaviour
            # for warehouses.

            await asyncio.sleep(0.1)
            current += 1

from Task import TaskQueue
from random import randint
from warehouse_monitoring.domain.emulator.core.Forklift import Forklift


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
            warehouse_id: int,
            city: str
    ):
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
                forklift_id=self.forklift_count,
                warehouse_id=self.id,
                task_queue=self.task_queue
            )
        )
        self.forklift_count += 1

    def work(self):
        # infinite loop with warehouse works
        while True:
            # iterate over forklifts and make them work =)
            for forklift in self.forklift_park:
                forklift.work()
            # and sometimes add new tasks to queue
            # upd: sometimes?))))
            for _ in range(randint(0, self.forklift_count)):
                self.task_queue.create_new_task()

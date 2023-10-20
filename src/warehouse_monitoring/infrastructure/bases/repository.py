from warehouse_monitoring.infrastructure.database import DatabaseSession


class BaseRepository:
    """Base repository class

    Method naming conventions:
    * method names must contain full model name in the snake_case,
      to avoid name conflicts.
    * prefix `get` refers to operation, that must exactly return
      an object. if object not found, error will be raised
    * prefix `find` refers to `get` method, that returns None
      on error.
    * prefix `search` refers to method, that returns an iterable.

    """

    def __init__(self, session: DatabaseSession):
        self.session = session

    async def commit(self):
        await self.session.commit()

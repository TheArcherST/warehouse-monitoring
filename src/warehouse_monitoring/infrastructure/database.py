from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from warehouse_monitoring.infrastructure.config import environment


def _create_engine(driver: str, is_async: bool):
    if is_async:
        create = create_async_engine
    else:
        create = create_engine

    engine_ = create(
        'postgresql+{}://{}:{}@{}:{}/{}'.format(
            driver,
            environment.postgres_user,
            environment.postgres_password,
            environment.postgres_host,
            environment.postgres_port,
            environment.postgres_db
        )
    )

    return engine_


try:
    engine = _create_engine('asyncpg', is_async=True)
except ImportError:
    engine = None

try:
    sync_engine = _create_engine('psycopg2', is_async=False)
except ImportError:
    sync_engine = None


async def inject_database_session():
    async with DatabaseSession(engine, expire_on_commit=False) as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        else:
            await session.commit()


DatabaseSession = AsyncSession


class Base(DeclarativeBase):
    pass


async def init_db():
    async with engine.begin() as session:
        # await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)

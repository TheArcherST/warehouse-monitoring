import locale

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from warehouse_monitoring.infrastructure.database import init_db

from warehouse_monitoring.presentation.api.routers import (
    router as root_router
)

from warehouse_monitoring.infrastructure.config import environment


from warehouse_monitoring.infrastructure.warehouse.emulator import Emulator
from warehouse_monitoring.infrastructure.warehouse.gateway.observer import WarehouseObserver
from warehouse_monitoring.domain import event_handlers

from warehouse_monitoring.domain import services
from warehouse_monitoring.presentation.interactor_factory.service import ServiceInteractorFactory

app = FastAPI(title="Warehouse monitoring API")


origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
    "https://localhost:3000",
]

if environment.allowed_origin:
    origins.append(environment.allowed_origin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(root_router)


@app.on_event("startup")
async def on_application_startup():
    await init_db()
    await start_emulator()


async def start_emulator():
    observer = WarehouseObserver()
    event_handlers.register(observer)
    emulator = Emulator(
        observer=observer,
        warehouses_count=10,
    )
    conf = emulator.get_configuration()
    ioc = ServiceInteractorFactory()
    async with ioc.configuration_merge_service() as service:
        service: services.ConfigurationMergeService
        await service.merge_configuration(conf)
    emulator.start()


def main():
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

    if environment.application_protocol == 'HTTP':
        uvicorn.run(
            app=app,
            host="0.0.0.0",
            port=8000,
        )
    elif environment.application_protocol == 'HTTPS':
        uvicorn.run(
            app=app,
            host="0.0.0.0",
            port=8000,
            ssl_certfile=environment.application_ssl_certfile,
            ssl_keyfile=environment.application_ssl_keyfile
        )
    else:
        raise KeyError(f"Unknown protocol `{environment.application_protocol}`")


if __name__ == "__main__":
    main()

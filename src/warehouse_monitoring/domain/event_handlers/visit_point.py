from warehouse_monitoring.infrastructure.warehouse.gateway import \
    WarehouseObserver, events
from warehouse_monitoring.domain import services
from warehouse_monitoring.presentation.interactor_factory.service import ServiceInteractorFactory


async def visit_point_handler(
        event: events.VisitPointEvent,
):
    ioc = ServiceInteractorFactory()
    print(event)
    async with ioc.movement_service() as service:
        service: services.MovementService
        await service.notify_checkpoint_visit(
            warehouse_id=event.warehouse_id,
            local_checkpoint_id=event.checkpoint_id,
            forklift_id=event.forklift_id,
        )


def register(observer: WarehouseObserver):
    observer.visit_point += visit_point_handler

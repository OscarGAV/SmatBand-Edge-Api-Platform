from typing import List
from core_context.domain.events.domain_event import DomainEvent
from core_context.infrastructure.event_bus import IEventBus


class InMemoryEventBus(IEventBus):
    def __init__(self):
        self._events: List[DomainEvent] = []

    async def publish(self, event: DomainEvent) -> None:
        self._events.append(event)
        # In production, this would publish to message queue
        print(f"[EVENT] {event.__class__.__name__}: {vars(event)}")
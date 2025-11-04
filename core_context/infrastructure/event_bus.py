# Event Bus Interface
from abc import abstractmethod, ABC
from core_context.domain.events.domain_event import DomainEvent


class IEventBus(ABC):
    @abstractmethod
    async def publish(self, event: DomainEvent) -> None:
        pass
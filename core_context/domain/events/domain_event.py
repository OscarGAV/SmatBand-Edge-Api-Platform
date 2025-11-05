from datetime import datetime, UTC
from uuid import uuid4
from abc import ABC


class DomainEvent(ABC):
    """Base class for domain events"""
    def __init__(self):
        self.occurred_at = datetime.now(UTC)
        self.event_id = uuid4()
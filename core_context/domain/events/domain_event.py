from datetime import datetime
from uuid import uuid4
from abc import ABC


class DomainEvent(ABC):
    """Base class for domain events"""
    def __init__(self):
        self.occurred_at = datetime.utcnow()
        self.event_id = uuid4()
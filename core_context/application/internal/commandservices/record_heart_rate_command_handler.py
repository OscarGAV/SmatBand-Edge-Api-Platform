from uuid import UUID
from core_context.domain.model.aggregates.heart_rate_reading import HeartRateReading
from core_context.domain.model.commands.record_heart_rate_command import RecordHeartRateCommand


class RecordHeartRateCommandHandler:
    """Handler for RecordHeartRateCommand"""

    def __init__(self, repository: 'IHeartRateRepository', event_bus: 'IEventBus'):
        self.repository = repository
        self.event_bus = event_bus

    async def handle(self, command: RecordHeartRateCommand) -> UUID:
        # Create domain entity (applies business rules)
        reading = HeartRateReading.create(
            smart_band_id=command.smart_band_id,
            pulse=command.pulse
        )

        # Persist
        await self.repository.save(reading)

        # Publish domain events
        for event in reading.get_domain_events():
            await self.event_bus.publish(event)

        reading.clear_domain_events()

        return reading.id
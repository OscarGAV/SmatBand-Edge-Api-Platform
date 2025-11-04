from pydantic import BaseModel, Field, field_validator


class RecordHeartRateRequestDTO(BaseModel):
    smartBandId: int = Field(..., alias="smartBandId", ge=1)
    pulse: str = Field(..., description="Heart rate as string (matching ESP32 format)")

    @field_validator('pulse')
    def validate_pulse(cls, v):
        try:
            pulse_int = int(v)
            if pulse_int < 0 or pulse_int > 300:
                raise ValueError("Pulse must be between 0 and 300")
            return v
        except ValueError:
            raise ValueError("Pulse must be a valid integer string")

    class Config:
        populate_by_name = True
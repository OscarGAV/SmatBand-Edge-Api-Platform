class RecordHeartRateCommand:
    """Command for recording heart rate data"""
    def __init__(self, smart_band_id: int, pulse: int):
        self.smart_band_id = smart_band_id
        self.pulse = pulse
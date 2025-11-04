class GetHeartRateHistoryQuery:
    """Query for retrieving heart rate history"""
    def __init__(self, smart_band_id: int, limit: int = 10):
        self.smart_band_id = smart_band_id
        self.limit = limit
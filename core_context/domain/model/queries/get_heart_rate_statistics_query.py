class GetHeartRateStatisticsQuery:
    """Query for retrieving statistics"""
    def __init__(self, smart_band_id: int):
        self.smart_band_id = smart_band_id
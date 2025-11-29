from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.passengers_active = {}
        self.time_totals = defaultdict(int)
        self.ride_counts = defaultdict(int)

    def checkIn(self, passenger, start_station, entry_time):
        self.passengers_active[passenger] = (start_station, entry_time)

    def checkOut(self, passenger, end_station, exit_time):
        start_station, entry_time = self.passengers_active.pop(passenger)
        pair = (start_station, end_station)
        travel_duration = exit_time - entry_time
        self.time_totals[pair] += travel_duration
        self.ride_counts[pair] += 1

    def getAverageTime(self, start_station, end_station):
        pair = (start_station, end_station)
        return self.time_totals[pair] / self.ride_counts[pair]

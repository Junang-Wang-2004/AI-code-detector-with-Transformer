from collections import defaultdict

class C1:

    def __init__(self):
        self.passengers_active = {}
        self.time_totals = defaultdict(int)
        self.ride_counts = defaultdict(int)

    def checkIn(self, a1, a2, a3):
        self.passengers_active[a1] = (a2, a3)

    def checkOut(self, a1, a2, a3):
        v1, v2 = self.passengers_active.pop(a1)
        v3 = (v1, a2)
        v4 = a3 - v2
        self.time_totals[v3] += v4
        self.ride_counts[v3] += 1

    def getAverageTime(self, a1, a2):
        v1 = (a1, a2)
        return self.time_totals[v1] / self.ride_counts[v1]
